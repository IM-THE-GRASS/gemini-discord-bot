import gemini
import discord
import config
from discord.ext import commands

token = config.get_config("discord_token")

class client(discord.Client):
    async def on_ready(self):
        print(self.user)

    async def on_message(self, message):
        if message.author.bot or message.channel.type != discord.ChannelType.private:
            return
        print(f'Message from {message.author}: {message.content}')
        response = gemini.generate(message.content)
        await message.channel.send(response)

intents = discord.Intents.default()
intents.message_content = True
intents.dm_messages = True

client = client(intents=intents)
client.run(token)