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
from narrator import narr


class BotMain:
    def __init__(self):
        self.intents = discord.Intents.default()
        self.intents.message_content = True
        self.bot = commands.Bot(command_prefix="!", intents=self.intents)
        load_dotenv()
        self.STEVE_TOKEN = os.getenv('STEVE_TOKEN')
        self.users = {}
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
            elif message.content.lower()[0] != '!':
                await message.channel.send("water bucket... RELEASE!!")
            await self.bot.process_commands(message)

        # Command example: !hello
        @self.bot.command()
        async def hello(ctx):
            await ctx.send("Flint and Steeeel!")

        @self.bot.command()
        async def ping(ctx):
            await ctx.send("ping")

        @self.bot.command()
        async def begin(ctx):
            if ctx.author in self.users:
                return
            else:
                player_dict = {ctx.author: [Narr(), playerData()]}
                self.users.update({player_dict})
                # initate the game
        
        @self.bot.command()
        async def end(ctx):
            if ctx.author in self.users:
                # end the game
                pass

        @self.bot.command()
        async def quest(ctx):
            pass

        @self.bot.command()
        async def inventory(ctx):
            await ctx.send(self.users[ctx.author][playerData.view_inventory()])

        @self.bot.command()
        async def equip(ctx, parameter):
           await ctx.send(self.users[ctx.author][playerData.view_inventory()])

    def run(self):
        # Run the bot with the token

        self.bot.run(self.STEVE_TOKEN)
