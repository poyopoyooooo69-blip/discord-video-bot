import discord
import subprocess
import re
import os

TOKEN = "MTQ4MDI4NzU3NjczNTYxMzE3Mg.GuR1Fc.KU_Ser_Lh1Qgc83apzf6La48v2CS68qr5EWz10"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

url_pattern = re.compile(r'https?://\S+')

@client.event
async def on_ready():
    print("Bot起動:", client.user)

@client.event
async def on_message(message):

    if message.author.bot:
        return

    urls = url_pattern.findall(message.content)

    if not urls:
        return

    for url in urls:

        try:
            result = subprocess.check_output(
                ["yt-dlp", "-f", "best", "--get-url", url],
                text=True
            ).strip()

            if result:
                await message.reply(f"🎬 Direct URL\n{result}")

        except:
            await message.reply("⚠️ URL変換失敗")

client.run(TOKEN)
