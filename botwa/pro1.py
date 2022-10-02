import discord
from discord.colour import Color
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self, client):
          self.client = client


    @commands.command()      
    async def transformerswfc(self, ctx):
        
        embed = discord.Embed(
            title="Transformers - War for Cybertron",url="https://anime-world.in/series/transformers-war-for-cybertron/",
            description='`Search Results-`',
            color=discord.Color.dark_red())

        embed.description="`Siege 👉`\n[`S1E1`](https://anime-world.in/episode/transformers-war-for-cybertron-1x1/)\n[`S1E2`](https://anime-world.in/episode/transformers-war-for-cybertron-1x2/)\n[`S1E3`](https://anime-world.in/episode/transformers-war-for-cybertron-1x3/)\n[`S1E4`](https://anime-world.in/episode/transformers-war-for-cybertron-1x4/)\n[`S1E5`](https://anime-world.in/episode/transformers-war-for-cybertron-1x5/)\n[`S1E6`](https://anime-world.in/episode/transformers-war-for-cybertron-1x6/)\n`Earthrise 👉 `\n[`S2E1`](https://anime-world.in/episode/transformers-war-for-cybertron-2x1/)\n[`S2E2`](https://anime-world.in/episode/transformers-war-for-cybertron-2x2/)\n[`S2E3`](https://anime-world.in/episode/transformers-war-for-cybertron-2x3/)\n[`S2E4`](https://anime-world.in/episode/transformers-war-for-cybertron-2x4/)\n[`S2E5`](https://anime-world.in/episode/transformers-war-for-cybertron-2x5/)\n[`S2E6`](https://anime-world.in/episode/transformers-war-for-cybertron-2x6/)\n`Kingdom 👉  SOON`"             

        embed.set_footer(text="Information from IACON HALL requested by: {}".format(ctx.author.display_name))

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Example(client))        