import discord
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self, client):
          self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def unban(self, ctx, *, member):
      banned_users = await ctx.guild.bans()
      member_name, member_discriminator = member.split("#")
      await ctx.channel.purge(limit=1)
    
      for ban_entry in banned_users:

            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.channel.send(f'Exile of {user.mention}' + 'is over. They can join the legion!', delete_after=5)
                return
            
    @unban.error
    async def clear_error(self, ctx, error):
     if isinstance(error, commands.MissingPermissions):
        await ctx.channel.purge(limit=1)  
        await ctx.send("{}".format(ctx.author.mention) + " can't unban. Reason = Low Rank", delete_after=3)      

def setup(client):
    client.add_cog(Example(client))              