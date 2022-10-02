import discord
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self, client):
          self.client = client
    

    @commands.command()
    async def ping(self, ctx, *, arg=None):
          if arg == None:
                await ctx.send(f'Prima says {round(self.client.latency*1000)}ms.')
          else:
             await ctx.channel.purge(limit=1)                    
             await ctx.send(f"You cannot add anything after the command **ping**, {ctx.author.mention}", delete_after=5)

    @commands.command()  
    async def gn(self, ctx):
          await ctx.send(f"CYA!!! Chau!!! 👋  {ctx.author.mention}")


def setup(client):
    client.add_cog(Example(client))         