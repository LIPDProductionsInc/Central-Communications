import discord
import asyncio
import datetime
import random

from discord.ext import commands

bot = commands.Bot

class CustomCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='cogtest')
    @commands.is_owner()
    async def only_me(self, ctx):
        await ctx.send(f'{ctx.author.mention} the cog is working as expected')
        pass

    @commands.command(name='juju')
    async def _juju(self, ctx):
        print('Someone be getting that sweet Juju')
        await ctx.send("Get your Juju Energy and find your new go to fore the BEST energy drink can guzzle! Use code TROOPERK at checkout or hit the link below <http://www.jujuenergy.com/>")
        pass

    @commands.command(name='twitch-sync')
    async def _sync(self, ctx):
        print('Discord and Twitch sync tutorial requested...')
        await ctx.send("How to sync your Discord and Twitch: https://discord.com/channels/731391566945714226/731391903580291103/732081933286244402")
        pass

    @commands.command(name='sound')
    async def _siren(self, ctx):
        print('Siren pack requested...')
        await ctx.send("The siren and weapon sounds that Kallam uses can be found here! https://drive.google.com/drive/folders/1aXMXE6QOFklWsOqKLirPpMYUc0a8HyaI?usp=sharing")
        pass

    @commands.command(name='graphics')
    async def _graphics(self, ctx):
        print('Visiual pack requested...')
        await ctx.send("The graphics mod is a remake of QuantV merged with Natural Vision Evolved, with a custom ENB and reshade made by Tiessen. If you are interested in learning more about it, open a ticket under <#944466196663775262>")
        pass

    @commands.command(name='map')
    async def _map(self, ctx):
        print('Map mod requested...')
        await ctx.send("This is the map Kallam currently uses: <https://dielikekane.com/tag/gta-v-mod-map-street-names/>")
        pass

    @commands.command(name='prime')
    async def _prime(self, ctx):
        print('Prime subscription help command ran...')
        await ctx.send("You can sub FOR FREE if you have Amazon Prime! Simply click the Subscribe button and select “Twitch Prime” after connecting your accounts - More Info here - <https://twitch.amazon.com/prime>")
        pass

    @commands.command(name='specs')
    async def _specs(self, ctx):
        print('PC specs requested')
        await ctx.send("Coming Soon")
        pass

    @commands.command(name='merch')
    async def _merch(self, ctx):
        print('Merch requested')
        await ctx.send("Wanna feel cozy? Get some Trooper Kallam merch today!: <http://trooperkallam.com/>")
        pass
    
    @commands.command(name='arrest')
    async def _arrest(self, ctx, member: discord.Member):
        min = 1
        max = 9999
        if member == ctx.author:
            await ctx.send(f'Now {ctx.author.mention}, why would you want to do that???')
        else:
            print(f'{member} has been placed under arrest')
            otcm = random.randint(min, max)
            await ctx.send(f'*watches {ctx.author.mention} place {member.mention} under arrest and escorts them to Mission Row for processing. They\'ve been sentenced for a period of {otcm} months.*')
            pass
        pass

    @commands.command(name='version')
    async def _version(self, ctx):
        print('Merch requested')
        await ctx.send("Running 0.0.8.0")
        pass

    #@commands.command(name='streamlist', enabled=False)
    #async def _streamlist(self, ctx):
    #    print('HasRoot link requested...')
    #    await ctx.send("Here's an automatically updated list of people who stream on Revival RP: <https://revivalrp.hasroot.com/>")
    #    pass
    
    @commands.command(name='po-box')
    async def _pobox(self, ctx):
        print('PO Box requested...')
        await ctx.send("""Kallam's PO Box:
P. O. Box 4182
Cheyenne, WY 82003""")
        pass
        
    @commands.command(name='secretlab')
    async def _secretlab(self, ctx):
        print('Secret Lab command ran...')
        await ctx.send("TrooperKallam is sitting in a Secretlab Titan gaming chair. You can get your own and game in style and comfort by clicking this link! <https://bit.ly/3r0wV8v>")
        pass
    
    @commands.command(name='time')
    async def _time(self, ctx):
        time = datetime.datetime.utcnow() - datetime.timedelta(hours=6)
        await ctx.send(f"Kallam\'s current time: **{time.strftime('%I:%M %p')}**")
        pass
    
    @commands.command(name='vote')
    async def _vote(self, ctx):
        print('Server Vote Command ran...')
        await ctx.send("Vote for the server here and recieve a cool role as well as some awesome perks! (Perks coming soon!) <https://top.gg/servers/731391566945714226/vote>")
        pass

    @commands.command(name='avatarsubmission')
    async def _avtarsubmission(self, ctx):
        print('Someone is submitting an avatar...')
        await ctx.send("Submit your avatar here! <https://form.gle/XAmL5MordR6RccJC9>")
        pass

    @commands.command(name='source')
    async def _source(self, ctx):
        print('Someone is requesting the source code...')
        await ctx.send("The source code for this bot can be found here: <http://github.com/LIPDProductionsInc/Central-Communications>")
        pass

def setup(bot):
    bot.add_cog(CustomCog(bot))
