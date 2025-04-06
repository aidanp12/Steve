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
from narrator import Narr
from Player import Player


class BotMain:
    def __init__(self):
        self.intents = discord.Intents.default()
        self.intents.message_content = True
        self.bot = commands.Bot(command_prefix="!", intents=self.intents)
        load_dotenv()
        self.STEVE_TOKEN = os.getenv('STEVE_TOKEN')
        self.users = {}
        self.player_dict = {}

        # initialize
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

            elif message.content[0] != '!' and message.author in self.player_dict:
                try:
                    narrator = self.player_dict[message.author][0]
                    response = narrator.progress_story(message.content)

                    # If the result is a list, join it
                    if isinstance(response, list):
                        response = "\n".join(response)

                    # Replace {player} placeholder with author's display name
                    if isinstance(response, str):
                        response = response.replace("{player}", message.author.display_name)

                    await message.channel.send(response)

                except Exception as e:
                    await message.channel.send("If you're seeing this blame Aidan.")
                    print(f"[ERROR] on_message: {e}")

            elif message.content[0] != '!':
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
                self.player_dict = {ctx.author: [Narr(), Player()]}
                self.player_dict.get(ctx.author)[0].initiate_story(self.player_dict.get(ctx.author)[1])
                await ctx.send("Your adventure has begun!")
                # initate the game

        @self.bot.command()
        async def end(ctx):
            if ctx.author in self.users:
                # end the game
                pass

        @self.bot.command()
        async def inventory(ctx):
            await ctx.send(self.users[ctx.author][self.player_dict.view_inventory()])

        @self.bot.command()
        async def equip(ctx, parameter):
            await ctx.send(self.users[ctx.author][self.player_dict.equip_weapon(parameter)])

    def run(self):
        # Run the bot with the token

        self.bot.run(self.STEVE_TOKEN)
