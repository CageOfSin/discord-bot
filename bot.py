import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

bot.run(os.getenv("DISCORD_TOKEN"))


bot.run(os.getenv("MTQzMTAyMjc5MjE4NjI2OTc5OQ.GOLwmc.aDpbNS8Tlo6TLFFH51mMor5fn4PLPqWz5JHbgI"))
