import asyncio
import math
import os

import discord
import roles
from components.role_layout import RoleLayout
from discord import app_commands
from discord.ext import commands, tasks

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

async def main():

    async with bot:
        await bot.start(os.environ["BOT_TOKEN_ID"])


if __name__ == "__main__":
    asyncio.run(main())
