import discord
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv(".env")
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
OPENROUTER_API = os.getenv('OPENROUTER_API')

# Connect open router api using OpenAI
ai_client = OpenAI(
    base_url = "https://openrouter.ai/api/v1",
    api_key = OPENROUTER_API
)

# completion = ai_client.chat.completions.create(
#   model="deepseek/deepseek-chat-v3.1:free",
#   messages=[
#     {
#       "role": "user",
#       "content": "What is the meaning of life?"
#     }
#   ]
# )

# print(completion)

class MyCilent(discord.Client):
    # on_ready -> built-in method in discord.Cilent, handles base connection to discord
    async def on_ready(self):
        # Gets the information of the user that logs in
        print("Logged on as {0}".format(self.user))
    
    async def on_message(self, message):
        # Check if the bot is sending a message, if it is sending a message return null
        if message.author == self.user:
            return 
        if message.content.startswith("$haii"):
            # debugprint(message.content)
            # print(message.mentions)
            await message.channel.send("Hello :3")

intents = discord.Intents.default()
intents.message_content = True

#Instantiate Client Class
discordClient = MyCilent(intents=intents)
discordClient.run(DISCORD_TOKEN)

