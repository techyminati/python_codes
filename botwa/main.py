import discord
import os
from discord import message
from discord import user
from discord.ext import commands, tasks
import random
from itertools import cycle
from discord.ext.commands import has_permissions, CheckFailure, BadArgument
from dotenv import load_dotenv
import youtube_dl

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix = '//')

intents = discord.Intents.default()  
intents.members = True  
client = commands.Bot(command_prefix="//", intents=intents)

class BotData:
        def __init__(self):
            self.welcome_channel = None
            self.goodbye_channel = None

botdata = BotData()  

status = cycle(['1st Prime:PRIMA','2nd Prime:LIEGE MAXIMO','3rd Prime:ALPHA TRION','4th Prime:VECTOR PRIME','5th Prime:MEGATRONUS','6th Prime:SOLUS PRIME','7th Prime:OPTIMUS PRIME','8th Prime:QUINTUS PRIME','9th Prime:NEXUS PRIME','10th Prime:ALCHEMIST PRIME','11th Prime:MICRONUS PRIME','12th Prime:SENTINEL PRIME','13th Prime:AMALGAMOUS PRIME','14th prime:ZETA PRIME','15th Prime:RACHEL❤️'])

@client.event
async def on_ready():
    change_status.start()
    print('Bot is ready')
        
@tasks.loop(seconds=10)
async def change_status():
     await client.change_presence(activity=discord.Game(next(status)))
 

@client.event
async def on_member_join(member):
        if botdata.welcome_channel != None:
            await botdata.welcome_channel.send(f'**Welcome to The THIRTEENS Legion! {member.mention}**')

        else:  
          print('Welcome channel is not set')


@client.event
async def on_member_remove(member):
        if botdata.goodbye_channel != None:
            await botdata.goodbye_channel.send(f'*{member.mention} has left the Legion!' + f' Their id : {member.id}*')
 
        else:
            print('Leaving channel is not set')

@client.command()
async def set_welcome_channel(ctx, channel_name=None):
        if channel_name != None:
            for channel in ctx.guild.channels:
                if channel.name == channel_name:
                    botdata.welcome_channel = channel
                    await ctx.channel.send(f'Welcome panel has been set to - {channel.name}')
                    await channel.send("This is the welcome screen")
 

        else:
            await ctx.channel.send("Channel name is incorrect...")

    
@client.command()
async def set_goodbye_channel(ctx, channel_name=None):
        if channel_name != None:
            for channel in ctx.guild.channels:
                if channel.name == channel_name:
                    botdata.goodbye_channel = channel
                    await ctx.channel.send(f'Leaving panel has been set to - {channel.name}')
                    await channel.send("This is the leaving screen")
 

        else:
            await ctx.channel.send("Channel name is incorrect...")  


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.channel.purge(limit=1)
        await ctx.send(f'{ctx.author.mention} ' + "Entered command wasn't found in the IACON-Hall of Records", delete_after=5)


@client.command()
@commands.has_permissions(manage_messages=True)
async def load(ctx, extension):
    await ctx.channel.purge(limit=1)
    client.load_extension(f'cogs.{extension}')
    await ctx.channel.send("Package loaded!", delete_after=5)

@load.error
async def clear_error(ctx, error):
     if isinstance(error, commands.MissingPermissions):
        await ctx.channel.purge(limit=1)  
        await ctx.send("{}".format(ctx.author.mention) + " doesn't have the permission to load package.", delete_after=3)    



@client.command()
@commands.has_permissions(manage_messages=True)
async def unload(ctx, extension):
    await ctx.channel.purge(limit=1)
    client.unload_extension(f'cogs.{extension}')   
    await ctx.channel.send("Package unloaded!", delete_after=5)
    

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@unload.error
async def clear_error(ctx, error):
     if isinstance(error, commands.MissingPermissions):
        await ctx.channel.purge(limit=1)  
        await ctx.send("{}".format(ctx.author.mention) + " doesn't have the permission to unload package.", delete_after=3)

@client.command()
@commands.has_permissions(manage_messages=True)
async def reload(ctx, extension):
    await ctx.channel.purge(limit=1) 
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.channel.send("Package reloaded!", delete_after=5)

@reload.error
async def clear_error(ctx, error):
     if isinstance(error, commands.MissingPermissions):
        await ctx.channel.purge(limit=1)  
        await ctx.send("{}".format(ctx.author.mention) + " doesn't have the permission to reload package.", delete_after=3)


@client.command()    
async def play(ctx, url : str):
        song_there = os.path.isfile('song.mp3')
        try:
            if song_there:
                os.remove('song.mp3')
        except PermissionError:
            await ctx.send(f"Let the song get over or use //stop: {ctx.message.author.mention}") 
            return

        voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='Music')
        await voiceChannel.connect()
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

        ydl_opts = {
          'format': 'bestaudio/best',
          'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '256',
          }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
          ydl.download([url])
        for file in os.listdir("./"):
         if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
        voice.play(discord.FFmpegPCMAudio("song.mp3"))

@client.command()    
async def leave(ctx):            
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()

    else:
        await ctx.send(f"First connect me to a voice channel: {ctx.message.author.mention}")    

@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
         voice.pause()

    else:
        await ctx.send(f"First add a song, then try to pause it: {ctx.message.author.mention}")

@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
         voice.resume()

    else:
        await ctx.send(f"Some audio is already playing, so you can't resume it: {ctx.message.author.mention}")        


@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()
    await ctx.channel.purge(limit=1)

client.run(token)