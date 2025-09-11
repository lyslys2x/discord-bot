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

intents = discord.Intents.default()
intents.message_content = True

#Instantiate Client Class and 
discordClient = MyCilent(intents=intents)
discordClient.run(DISCORD_TOKEN)
