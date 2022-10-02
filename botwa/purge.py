import discord
from discord.ext import commands
from discord.ext.commands.core import command

class Example(commands.Cog):

    def __init__(self, client):
          self.client = client

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount =1):
        await ctx.channel.purge(limit=amount+1)
        await ctx.send('Context removed sir! {}'.format(ctx.author.mention), delete_after=2)
        await ctx.message.delete()
 
        
    @purge.error
    async def clear_error(self, ctx, error):
     if isinstance(error, commands.MissingPermissions):
        await ctx.channel.purge(limit=1)
        await ctx.send("You do not have permission to do so {}".format(ctx.author.mention), delete_after=3)

    def is_it_liege(ctx):
        return ctx.author.id == 328131534894661634

    @commands.command()        
    @commands.check(is_it_liege)
    async def respect(self, ctx):
        await ctx.send(f"It is an **Honour** to serve you **Legion Commander** {ctx.author.mention}")

def setup(client):
    client.add_cog(Example(client))        