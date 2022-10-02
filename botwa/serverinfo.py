import discord
from discord.colour import Color
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self, client):
          self.client = client


    @commands.command()
    async def serverinfo(self, ctx):
        name = str(ctx.guild.name)
        owner = str(ctx.guild.owner)
        memberCount = str(ctx.guild.member_count)
        icon = str(ctx.guild.icon_url)
        
        embed = discord.Embed(
            title=name + " Server Info",
            description='The test server of Sir Liege Maximo, Legion Commander of the Primes!',
            color=discord.Color.dark_gold())

        embed.set_thumbnail(url=icon)
        embed.add_field(name='Owner', value=owner, inline=True)
        embed.add_field(name='Region' , value=' Global!' , inline=True)
        embed.add_field(name='Member Count' , value = memberCount, inline=False)
        embed.description="[`xyz`](https://www.google.com)\n[`xz`](https://www.google.com)"
        
        embed.set_footer(text="Information from IACON HALL requested by: {}".format(ctx.author.display_name))

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Example(client))
