import discord
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self, client):
          self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def kick(self, ctx, member:commands.MemberConverter, *, reason=None): 
      await ctx.channel.purge(limit=1)  
      await member.create_dm()
      await member.dm_channel.send(content=f"You have been kicked from {ctx.guild} by {ctx.message.author}\nReason: {reason} " )
      await member.kick(reason=reason)

    @kick.error
    async def clear_error(self, ctx, error):
     if isinstance(error, commands.MissingPermissions):  
        await ctx.send("{}".format(ctx.author.mention) + " can't kick. Reason = Low Rank", delete_after=3)


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, user:commands.MemberConverter, *, reason=None):
      await user.create_dm()
      await ctx.channel.purge(limit=1) 
      await user.dm_channel.send(content=f"You have been banned from {ctx.guild} by {ctx.message.author}\nReason: {reason} ")
      await user.ban(reason=reason)  

    @ban.error
    async def clear_error(self, ctx, error):
     if isinstance(error, commands.MissingPermissions):
        await ctx.channel.purge(limit=1)  
        await ctx.send("{}".format(ctx.author.mention) + " can't ban. Reason = Low Rank", delete_after=3)      

def setup(client):
    client.add_cog(Example(client))         