import discord
import google.generativeai as genai

# Your Discord bot token
DISCORD_TOKEN = 'MTM1Nzk1NjE4MzY2MjUyNjY1MQ.Gx4MPy.NVgjMoS2MEDLx8Qt5pn-Drmgdv0yEKsInvLEDU'

# Your Gemini API key
GOOGLE_API_KEY = 'AIzaSyCJJDqLc6DTiQZpHXB0OG22yhBtp'

# Configure the Gemini API
genai.configure(api_key=GOOGLE_API_KEY)

# Select the Gemini model you want to use (e.g., gemini-pro for text)
model = genai.GenerativeModel('gemini-pro')

intents = discord.Intents.default()
intents.message_content = True  # Enable reading message content

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if client.user.mentioned_in(message):
        prompt = message.content.replace(f'<@{client.user.id}>', '').strip()

        if prompt:
            try:
                response = model.generate_content(prompt)
                await message.reply(response.text)
            except Exception as e:
                await message.reply(f"An error occurred: {e}")
        else:
            await message.reply("You mentioned me, but didn't ask anything!")

client.run(DISCORD_TOKEN)
