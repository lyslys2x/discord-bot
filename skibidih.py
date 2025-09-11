import discord
import os
from dotenv import load_dotenv

load_dotenv(".env")
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

class MyCilent(discord.Client):
    # on_ready -> built-in method in discord.Cilent, handles base connection to discord
    async def on_ready(self):
        # Gets the information of the user that logs in
        print("Logged on as {0}".format(self.user))
    
    async def on_message(self, message):
        # Check if the bot is sending a message, if it is sending a message return null
        if message.on_author == self.user:
            return 
        if message.content.startswith("$haii"):
            await message.channel.senf("Hello :3")

intents = discord.Intents.default()
intents.message_content = True

#Instantiate Client Class and 
discordClient = MyCilent(intents=intents)
discordClient.run(DISCORD_TOKEN)

