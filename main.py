from keep_alive import keep_alive
import discord
from discord.ext import commands
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot is online as {bot.user}")

@bot.command()
async def start(ctx):
    await ctx.send("🟢 Server start command sent!")
    await ctx.send("⌛ Waiting for server to come online...")

    # Example: Future server logic
    # try:
    #     response = requests.post("http://192.168.1.10:5000/start")
    #     if response.ok:
    #         await ctx.send("✅ Server started.")
    #     else:
    #         await ctx.send("❌ Failed to start server.")
    # except Exception as e:
    #     await ctx.send(f"⚠️ Error: {e}")

@bot.command()
async def end(ctx):
    await ctx.send("🔴 Server stop command sent!")
    await ctx.send("💤 Server is now shutting down.")

    # Example: Future server logic
    # try:
    #     response = requests.post("http://192.168.1.10:5000/stop")
    #     if response.ok:
    #         await ctx.send("✅ Server stopped.")
    #     else:
    #         await ctx.send("❌ Failed to stop server.")
    # except Exception as e:
    #     await ctx.send(f"⚠️ Error: {e}")

@bot.command()
async def status(ctx):
    await ctx.send("📡 Server is currently **offline** (or being set up).")

@bot.command()
async def credits(ctx):
    await ctx.send("🤖 Bot made by **Lord Sudeep 👑**, server integration by his buddy 💻")


keep_alive()

# 🔐 Paste your token between the quotes below
bot.run("MTM4NjM3MzU1MzM5NzY5ODcwMw.GdnCVM.ikNqqypBAVqNl4k8cvo_zTsvR2CGZ9zQ-fzY1k")
