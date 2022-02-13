from discord import FFmpegPCMAudio
from discord.ext import commands
from discord.utils import get
from gtts import gTTS
import json

f = open('config.json')
config = json.load(f)
f.close()

prefix = config["prefix"]
token = config["token"]

bot = commands.Bot(command_prefix=prefix)

async def join(ctx, voice):
    channel = ctx.author.voice.channel
    if channel != None:
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()
    else:
        await bot.say('User is not in a channel.')

def convertTTStr(query):
    tts = gTTS(text=query, lang='tr')
    tts.save('temp.mp3')

def convertTTSen(query):
    tts = gTTS(text=query, lang='en')
    tts.save('temp.mp3')

@bot.command()
async def saytr(ctx, *, query):
    FFMPEG_OPTS = {'options': '-vn'}
    voice = get(bot.voice_clients, guild=ctx.guild)
    convertTTStr(query)
    await join(ctx, voice)
    voice_channel = ctx.author.voice.channel
    if voice_channel != None:
        voice.play(FFmpegPCMAudio('temp.mp3', **FFMPEG_OPTS), after=lambda e: print('done', e))
        voice.is_playing()
    else:
        await bot.say('User is not in a channel.')

@bot.command()
async def sayen(ctx, *, query):
    FFMPEG_OPTS = {'options': '-vn'}
    voice = get(bot.voice_clients, guild=ctx.guild)
    convertTTSen(query)
    await join(ctx, voice)
    voice_channel = ctx.author.voice.channel
    if voice_channel != None:
        voice.play(FFmpegPCMAudio('temp.mp3', **FFMPEG_OPTS), after=lambda e: print('done', e))
        voice.is_playing()
    else:
        await bot.say('User is not in a channel.')

bot.run("TOKEN")
