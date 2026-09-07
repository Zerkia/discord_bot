import asyncio
import math
import os
import discord
import roles

from discord import app_commands
from discord.ext import commands, tasks
from components.role_layout import RoleLayout
from components.card_layout import create_card_embed
from duema_api import get_card

from config import APPLICATION_ID, BOT_TOKEN_ID, CHANNEL_ID

intents = discord.Intents.default()
intents.guilds = True
intents.members = True

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("!"),
    intents=intents,
    application_id=APPLICATION_ID,
    channel_id=CHANNEL_ID,
)

_synced = False

@bot.event
async def on_ready():
    global _synced
    if not _synced:
        await bot.tree.sync()
        _synced = True

    print(f"Logged in as {bot.user}")

# Hello World Command
@bot.tree.command(name="hello", description="Says Hello World Back to you!")
async def hello_world(interaction: discord.Interaction):

    await interaction.response.send_message(content="Hello, world!")

# Color Roles Command
@bot.tree.command(name="color-roles", description="Shows list of color roles to choose from")
async def color_roles(interaction: discord.Interaction):

    await interaction.response.send_message(content="Color Roles Layout Set Up", ephemeral=True)
    view = RoleLayout(
        title="**Choose Your Color Role**",
        description="All Oath members can claim one of these base colors to make your name stand out:",
        role_data=roles.ROLE_GROUPS["color"]
    )

    await interaction.channel.send(view=view)

# Social Roles Command
@bot.tree.command(name="social-roles", description="Shows list of social roles to choose from")
async def social_roles(interaction: discord.Interaction):

    await interaction.response.send_message(content="Social Roles Layout Set Up", ephemeral=True)
    view = RoleLayout(
        title="**Social Activities**",
        subtitle="Want to socialize with the guildies? :oath:",
        description="Click to opt in for notifications based on which social activity you want to be notified about. You can always opt out later!",
        role_data=roles.ROLE_GROUPS["social"]
    )

    await interaction.channel.send(view=view)

# Social Roles Command
@bot.tree.command(name="notification-roles", description="Shows list of notification roles to choose from")
async def notification_roles(interaction: discord.Interaction):

    await interaction.response.send_message(content="Notification Roles Layout Set Up", ephemeral=True)
    view = RoleLayout(
        title="**Opt Out of Notifications**",
        subtitle="Getting too many notifications?",
        description="Just remove any roles you don't want notifications from. You can always add them back later!",
        role_data=roles.ROLE_GROUPS["notification"]
    )

    await interaction.channel.send(view=view)

# Duel MastersCard Lookup Command
@bot.tree.command(name="card", description="Look up a Duel Masters card")
async def card(interaction: discord.Interaction, card_name: str):
  card = get_card(card_name)

  if card is None:
      await interaction.response.send_message(
          f'Could not find a card named "{card_name}".'
      )
      return

  embed = create_card_embed(card)

  await interaction.response.send_message(embed=embed)

async def main():

    async with bot:
        await bot.start(os.environ["BOT_TOKEN_ID"])


if __name__ == "__main__":
    asyncio.run(main())
