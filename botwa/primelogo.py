import discord
from discord.colour import Color
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self, client):
          self.client = client


    @commands.command()
    async def liege(self, ctx):  

        embed = discord.Embed(
            title="Prime Cores - Liege Maximo",
            url='https://transformers.fandom.com/wiki/Liege_Maximo',
            description='Liege Maximo is one of the Thirteen original Primes and the manipulator. He was among the Thirteen created by Primus to battle and defeat Unicron and witnessed the activation of the Well of Allsparks.',
            color=discord.Color.dark_green())           

        embed.set_thumbnail(url='http://t-rex.wdfiles.com/local--files/wiki:powercores/liege_maximo.png')

        await ctx.send(embed=embed)
        
    @commands.command()
    async def prima(self, ctx):  

        embed = discord.Embed(
            title="Prime Cores - Prima",
            url='https://transformers.fandom.com/wiki/Prima',
            description='Prima was the first Transformer born on Cybertron and the leader of the Thirteen. He was a warrior of light who used the Star Saber with the Matrix of Leadership as its hilt.',
            color=discord.Color.dark_gray())           

        embed.set_thumbnail(url='http://t-rex.wdfiles.com/local--files/wiki:powercores/primaPrime.png')

        await ctx.send(embed=embed)

    @commands.command()
    async def alpha(self, ctx):  

        embed = discord.Embed(
            title="Prime Cores - Alpha Trion",
            url='https://transformers.fandom.com/wiki/Alpha_Trion_(G1)',
            description='Alpha Trion Prime is one of the oldest living Transformers, and with that age comes a nuanced understanding of his race and their place within the universe',
            color=discord.Color.red())           

        embed.set_thumbnail(url='http://t-rex.wdfiles.com/local--files/wiki:powercores/Alpha_Trion_Prime_Core.png')

        await ctx.send(embed=embed)    

    @commands.command()
    async def megatronus(self, ctx):  

        embed = discord.Embed(
            title="Prime Cores - Megatronus",
            url='https://transformers.fandom.com/wiki/Megatronus',
            description='Megatronus Prime, also known as the Fallen, is one of the Thirteen original Primes, the first Decepticon, and the true main antagonist.',
            color=discord.Color.dark_red())           

        embed.set_thumbnail(url='http://t-rex.wdfiles.com/local--files/wiki:powercores/megatronus.png')

        await ctx.send(embed=embed)    
 
    @commands.command()
    async def vector(self, ctx):  

        embed = discord.Embed(
            title="Prime Cores - Vector Prime",
            url='https://transformers.fandom.com/wiki/Vector_Prime',
            description='Vector Prime is one of the Thirteen and is the interdimensional traveler who spent most of his life in the multiverse, observing it, and occasionally stepping in to help. It is said that as Guardian of Space and Time, he can access to every alternate reality and could reverse/stop time itself.',
            color=discord.Color.dark_blue())           

        embed.set_thumbnail(url='http://t-rex.wdfiles.com/local--files/wiki:powercores/Vector_Prime_Core.JPG')

        await ctx.send(embed=embed)


    @commands.command()
    async def quintus(self, ctx):  

        embed = discord.Embed(
            title="Prime Cores - Quintus Prime",
            url='https://transformers.fandom.com/wiki/Quintus_Prime',
            description='Quintus was an innocent daydreamer, with a strong tendency toward perfectionism and idealism. He constantly sought expression of his ideas and was driven to prove his theories correct by an experimental invention. ',
            color=discord.Color.green())           

        embed.set_thumbnail(url='http://t-rex.wdfiles.com/local--files/wiki:powercores/quintus_prime.png')

        await ctx.send(embed=embed)  

    @commands.command()
    async def alchemist(self, ctx):  

        embed = discord.Embed(
            title="Prime Cores - Alchemist Prime",
            url='https://transformers.fandom.com/wiki/Alchemist_Prime',
            description='Alchemist Prime is one of the Thirteen and is the co-founder of the early Cybertronian civilization with Alpha Trion, while the other Primes separated across space and time after their great schism.',
            color=discord.Color.darker_gray())           

        embed.set_thumbnail(url='http://t-rex.wdfiles.com/local--files/wiki:powercores/alchemist.png')

        await ctx.send(embed=embed)          

    @commands.command()
    async def nexus(self, ctx):  

        embed = discord.Embed(
            title="Prime Cores - Nexus Prime",
            url='https://transformers.fandom.com/wiki/Nexus_Prime',
            description='Nexus Prime, known as the Wizard of Forms, is one of the Thirteen and is the first and greatest combiner. Unpredictable, he was fascinated by change and was a light-headed prankster. He is also a wielder of the Omni Saber and Cyber Caliber.',
            color=discord.Color.lighter_gray())           

        embed.set_thumbnail(url='http://t-rex.wdfiles.com/local--files/wiki:powercores/nexus_prime.png')

        await ctx.send(embed=embed)   

    @commands.command()
    async def solus(self, ctx):  

        embed = discord.Embed(
            title="Prime Cores - Solus Prime",
            url='https://transformers.fandom.com/wiki/Solus_Prime',
            description='Solus Prime is one of the Thirteen created by Primus. Solus is a female Prime and is the maker of ancient Cybertronian weapons and relics. The arsenal of magnificent weaponry and icons wielded by the original Primes are her most impressive handiwork, created by an icon of her own, the Forge of Solus Prime.',
            color=discord.Color.blue())           

        embed.set_thumbnail(url='http://t-rex.wdfiles.com/local--files/wiki:powercores/solus_prime.png')

        await ctx.send(embed=embed)   

    @commands.command()
    async def amalgamous(self, ctx):  

        embed = discord.Embed(
            title="Prime Cores - Amalgamous Prime",
            url='https://transformers.fandom.com/wiki/Amalgamous_Prime',
            description="Amalgamous Prime was one of the Original Thirteen Primes. He was the trickster of the Primes, also had quite a short fuse and was easily frustrated. His artifact was the Transformation Cog, from which all later T-Cogs would be modeled. His however was far adavncer than any other's; he was also the first Shifter, a subclass of cybertranians with particularly advanced T-cogs, which enable them to assume a far greater variety of forms, including even other cybertronians.",
            color=discord.Color.teal())           

        embed.set_thumbnail(url='http://t-rex.wdfiles.com/local--files/wiki:powercores/amalgamous_Prime_core.png')

        await ctx.send(embed=embed)                   

    @commands.command()
    async def onyx(self, ctx):  

        embed = discord.Embed(
            title="Prime Cores - Onyx Prime",
            url='https://transformers.fandom.com/wiki/Onyx_Prime',
            description='Onyx Prime is the first of the Cybertronians with a Beast Mode and thus the ancestor of the Predacons and one of the Thirteen. He is not known to have wielded any weapons, but possessed the Triptych Mask as his personal artifact.',
            color=discord.Color.dark_orange())           

        embed.set_thumbnail(url='http://t-rex.wdfiles.com/local--files/wiki:powercores/Onyx_Prime.JPG')

        await ctx.send(embed=embed)   


    @commands.command()
    async def micronus(self, ctx):  

        embed = discord.Embed(
            title="Prime Cores - Micronus Prime",
            url='https://transformers.fandom.com/wiki/Micronus_Prime',
            description="Micronus Prime is the first Mini-con and one of the Thirteen. By coming in contact with the other members of the Thirteen he could enhance their skills and powers. Notably, he assisted Solus Prime in the creation of many of the Thirteen's artifacts. Following the War of the Primes, he chose to join with the AllSpark.",
            color=discord.Color.dark_teal())           

        embed.set_thumbnail(url='http://t-rex.wdfiles.com/local--files/wiki:powercores/micronus.png')

        await ctx.send(embed=embed)   


    @commands.command()
    async def optimus(self, ctx):  

        embed = discord.Embed(
            title="Prime Cores - Optimus Prime",
            url='https://transformers.fandom.com/wiki/Optimus_Prime_(Primax)',
            description="Optimus Prime is the awe inspiring, powerful and compassionate leader of the Autobot forces. Originally a working-class civilian, he was chosen by the Matrix to command the Autobots, which was merely the first of a number of burdens he would be forced to bear — another being his unintentional relocation of the Transformers' age-old conflict to Earth. He believes that 'freedom is the right of all sentient beings', and has fought for thousands of years against the bellicose Decepticons.",
            color=discord.Color.dark_red())           

        embed.set_thumbnail(url='https://static.wikia.nocookie.net/transformers/images/b/b7/Prime-matrix-s01e26-1.jpg/revision/latest?cb=20190726223712')

        await ctx.send(embed=embed)   



def setup(client):
    client.add_cog(Example(client))        