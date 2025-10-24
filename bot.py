import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="?", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.name}! 👋")

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"{member.name} has been kicked. 🚫")

bot.run(os.getenv("MTQzMTAyMjc5MjE4NjI2OTc5OQ.GOLwmc.aDpbNS8Tlo6TLFFH51mMor5fn4PLPqWz5JHbgI"))
