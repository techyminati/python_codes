import asyncio
import discord
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self, client):
          self.client = client

    class DurationConverter(commands.Converter):
        async def convert(self, ctx, argument):
            amount = argument[:-1]
            unit = argument[-1]

            if amount.isdigit() and unit in ['h']:
                return (int(amount), unit)

            raise commands.BadArgument(message='Not a valid duration sire!')


    @commands.command()   
    @commands.has_permissions(manage_messages=True) 
    async def tempban(self, ctx, member: commands.MemberConverter, duration: DurationConverter, *, reason=None,):

        multiplier = {'h':3600}
        amount, unit = duration

        await ctx.channel.purge(limit=1)  
        await member.create_dm()
        await member.dm_channel.send(content=f"You have been temporarily banned from {ctx.guild} by {ctx.message.author}\nReason: {reason} \nBanned for : {amount}{unit}. " )
        await ctx.guild.ban(member)
        await asyncio.sleep(amount * multiplier[unit])
        await ctx.guild.unban(member)
        
    @tempban.error
    async def clear_error(self, ctx, error):
     if isinstance(error, commands.MissingPermissions):
        await ctx.channel.purge(limit=1)  
        await ctx.send("{}".format(ctx.author.mention) + " can't do temporary ban. Reason = Low Rank", delete_after=3)   


def setup(client):
    client.add_cog(Example(client))                 