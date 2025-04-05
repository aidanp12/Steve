"""
Purpose: run the bot
Input:
Output:
Created: 04/05/2025
Last Edited: 04/05/2025
Contributors:
"""

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

class BotMain:
    def __init__(self):
        self.intents = discord.Intents.default()
        self.intents.message_content = True
        self.bot = commands.Bot(command_prefix="!", intents = self.intents)
        load_dotenv()
        self.STEVE_TOKEN = os.getenv('STEVE_TOKEN')

        self.initialize()



    def initialize(self):

        # Event when the bot has successfully connected
        @self.bot.event
        async def on_ready():
            print(f"Bot connected as {self.bot.user}")

        @self.bot.event
        async def on_message(message):
            if message.author == self.bot.user:
                return
            if message.content.lower() == 'this':
                await message.channel.send('is a CRAFTING table')
            await self.bot.process_commands(message)

        # Command example: !hello
        @self.bot.command()
        async def hello(ctx):
            await ctx.send("Flint and Steeeel!")
        @self.bot.command()
        async def ping(ctx):
            await ctx.send("ping")
    def run(self):
        # Run the bot with the token

        self.bot.run(self.STEVE_TOKEN)


