"""
Purpose:
Input:
Output:
Created: 04/05/2025
Last Edited: 04/05/2025
Contributors:
"""

import discord
from discord.ext import commands

class botMain:
    def __init__(self):
        self.intents = discord.Intents.default()
        self.intents.message_content = True
        self.initialize()

    def initialize(self):
        bot = commands.Bot(command_prefix="!", intents=self.intents)

        # Event when the bot has successfully connected
        @bot.event
        async def on_ready():
            print(f"Bot connected as {bot.user}")

        # Command example: !hello
        @bot.command()
        async def hello(ctx):
            await ctx.send("Flint and Steeeel!")

        # Run the bot with the token
        bot.run("MTM1Nzk1NjE4MzY2MjUyNjY1MQ.Gx4MPy.NVgjMoS2MEDLx8Qt5pn-Drmgdv0yEKsInvLEDU")


