import discord
from discord import app_commands
from discord.ext import commands
from playsound import playsound
import os
from gtts import gTTS
import time
import winsound

bot = commands.Bot(command_prefix="!", intents= discord.Intents.all())


@bot.event
async def on_ready():
    print("[LOG]: Started")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e)

@bot.tree.command(name="t")
@app_commands.describe(desc = "runs a tts on the hosted side")
async def tts(interaction: discord.Interaction, desc: str):
    language = 'en'
    myobj = gTTS(text=desc, lang=language, slow=False)
    myobj.save("audio.mp3")
    time.sleep(0.1)
    playsound("audio.mp3")
    print("[LOG]: Playing 'audio.mp3' from cache!")
    time.sleep(0.1)
    winsound.PlaySound(None, winsound.SND_PURGE)
    os.system("del audio.mp3")
    await interaction.response.send_message("Played Audio with the string '{}'".format(desc))


bot.run("TOKEN")
