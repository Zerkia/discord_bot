import asyncio
import math
import os

import discord
from role_layout import RoleLayout
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

@bot.tree.command(name="hello", description="Says Hello World Back to you!")
async def hello_world(interaction: discord.Interaction):

    await interaction.response.send_message(content="Hello, world!")

@bot.tree.command(name="rolelayout", description="tests layout components")
async def rolelayout(interaction: discord.Interaction):

    await interaction.response.defer(ephemeral=True)
    view = RoleLayout()
    await interaction.followup.send(view=view)

async def main():

    async with bot:
        await bot.start(os.environ["BOT_TOKEN_ID"])


if __name__ == "__main__":
    asyncio.run(main())
