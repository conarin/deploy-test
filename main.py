import os

import discord


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author.bot:
            return

        if message.content == 'ping':
            await message.channel.send('pong')
        elif message.content == 'neko':
            await message.channel.send('にゃーん')


client = MyClient()
client.run(os.environ['TOKEN'])