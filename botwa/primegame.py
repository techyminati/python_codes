import discord 
import random
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self, client):
          self.client = client

    @commands.command(aliases=['primes'])
    async def _13primes(self, ctx , *, HUH):
       response= ['Thirteen',
                  'Prima (presumed deceased)',
                  'Megatronus (presumed deceased)',
                  'Alpha Trion (deceased)',
                  'Vector Prime (unknown)',
                  'Quintus Prime (presumed deceased)',
                  'Nexus Prime (alive)',
                  'Solus Prime (deceased)',
                  'Liege Maximo (deceased)',
                  'Alchemist Prime (unknown)',
                  'Amalgamous Prime (unknown)',
                  'Onyx Prime (merged with Primus)',
                  'Micronus Prime (in the Realm of the Primes)',
                  'Optimus Prime (alive)',
                  'Sentinel Zeta Prime (deceased)']

       await ctx.send(f'What do you seek? : {HUH}\nAnswer: {random.choice(response)}')    

def setup(client):
    client.add_cog(Example(client))          