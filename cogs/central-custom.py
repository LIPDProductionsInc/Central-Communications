import discord
import asyncio
import datetime
import random

from discord.ext import commands

bot = commands.Bot

bot.sasp = 'open'
bot.safr = 'open'
bot.sadot = 'open'
bot.sadoj = 'open'
bot.rosa = 'open'
bot.sarcc = 'closed'

class CustomCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='cogtest')
    @commands.is_owner()
    async def only_me(self, ctx):
        await ctx.send(f'{ctx.author.mention} the cog is working as expected')
        pass
    
    @commands.command(name='open')
    @commands.has_permissions(manage_guild=True)
    async def _open(self, ctx, arg = None):
        if arg == None:
            await ctx.send("Please re-do the command with the department application you want to mark as open.")
        if arg == 'sasp':
            bot.sasp = 'open'
            await asyncio.sleep(0.1)
            await ctx.send("Opened SASP apps successfully!")
        if arg == 'safr':
            bot.safr = 'open'
            await asyncio.sleep(0.1)
            await ctx.send("Opened SAFR apps successfully!")
        if arg == 'sadot':
            bot.sadot = 'open'
            await asyncio.sleep(0.1)
            await ctx.send("Opened SADOT apps successfully!")
        if arg == 'sadoj':
            bot.sadoj = 'open'
            await asyncio.sleep(0.1)
            await ctx.send("Opened SADoJ apps successfully!")
        if arg == 'rosa':
            bot.rosa = 'open'
            await asyncio.sleep(0.1)
            await ctx.send("Opened RoSA apps successfully!")
        if arg == 'sarcc':
            bot.sarcc = 'open'
            await asyncio.sleep(0.1)
            await ctx.send("Opened SARCC apps successfully!")
            pass
        pass
    
    @commands.command(name='close')
    @commands.has_permissions(manage_guild=True)
    async def _close(self, ctx, arg = None):
        if arg == None:
            await ctx.send("Please re-do the command with the department application you want to mark as closed.")
        if arg == 'sasp':
            bot.sasp = 'closed'
            await asyncio.sleep(0.1)
            await ctx.send("Closed SASP apps successfully!")
        if arg == 'safr':
            bot.safr = 'closed'
            await asyncio.sleep(0.1)
            await ctx.send("Closed SAFR apps successfully!")
        if arg == 'sadot':
            bot.sadot = 'closed'
            await asyncio.sleep(0.1)
            await ctx.send("Closed SADOT apps successfully!")
        if arg == 'sadoj':
            bot.sadoj = 'closed'
            await asyncio.sleep(0.1)
            await ctx.send("Closed SADoJ apps successfully!")
        if arg == 'rosa':
            bot.rosa = 'closed'
            await asyncio.sleep(0.1)
            await ctx.send("Closed RoSA apps successfully!")
        if arg == 'sarcc':
            bot.sarcc = 'closed'
            await asyncio.sleep(0.1)
            await ctx.send("Closed SARCC apps successfully!")
            pass
        pass

    @commands.command(name='juju')
    async def _juju(self, ctx):
        print('Someone be getting that sweet Juju')
        await ctx.send("Get your Juju Energy and find your new go to fore the BEST energy drink can guzzle! Use code TROOPERK at checkout or hit the link below <http://www.jujuenergy.com/>")
        pass

    @commands.command(name='sync')
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

    @commands.command(name='service')
    async def _service(self, ctx):
        print('Kallams LEO service requested...')
        await ctx.send("Kallam has 16 years in law enforcement with several different agencies; time in SWAT, K-9 training and FTO")
        pass

    @commands.command(name='saltychat')
    async def _toko(self, ctx):
        print('SaltyChat requested...')
        await ctx.send("Revival RP utilizes SaltyChat, a Team Speak 3 plugin, for in-game communication. Download the plugin here: <https://gaming.v10networks.com/saltychat/download/stable>")
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
        await ctx.send("Running 0.0.7.0")
        pass

    @commands.command(name='streamlist')
    async def _streamlist(self, ctx):
        print('HasRoot link requested...')
        await ctx.send("Here's an automatically updated list of people who stream on Revival RP: <https://revivalrp.hasroot.com/>")
        pass
    
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
    
    @commands.command(name='rcore')
    async def _rcore(self, ctx):
        await ctx.send("Revival RP is proud to partner with rcore. They have developed the pool script seen in stream as well some other scripts. Check them out at <http://rcore.cz/>")
        print('rcore command ran...')
        pass
    
    
    @commands.command(name='sasp')
    async def _sasp(self, ctx):
        if bot.sasp == 'open':
            print('SASP Application link requested...')
            await ctx.send("Applications to be a State Trooper are open! Join San Andreas's finest. Must have a minimum of 10 hours in server and be 18 y/o. Click the link. <https://revivalrp.com/index.php?/forum/18-sasp-applications/>")
        if bot.sasp == 'closed':
            print('SASP Application link requested...')
            await ctx.send("Applications to be a State Trooper are currently closed! Stay tuned to when they open back up!")
            pass
        pass
    
    @commands.command(name='safr')
    async def _safr(self, ctx):
        if bot.safr == 'open':
            print('SAFR Application Link requested...')
            await ctx.send("Applications to be a Firefighter/EMT are open! Join San Andreas's bravest. Must have a minimum of one week in server and be 18 y/o. Click the link. <https://revivalrp.com/index.php?/forum/19-safr-applications/>")
        if bot.safr == 'closed':
            print('SAFR Application link requested...')
            await ctx.send("Applications to be a Firefighter/EMT are currently closed! Stay tuned to when they open back up!")
            pass
        pass
    
    @commands.command(name='sadot')
    async def _sadot(self, ctx):
        if bot.sadot == 'open':
            print('SADOT Application Link requested...')
            await ctx.send("Applications to be a Transportation Worker are open! Join San Andreas's friendliest. Must have a minimum of one week in server and be 18 y/o. Click the link. <https://revivalrp.com/index.php?/forum/45-sadot-applications/>")
        if bot.sadot == 'closed':
            print('SADOT Application link requested...')
            await ctx.send("Applications to be a Transportation Worker are currently closed! Stay tuned to when they open back up!")
            pass
        pass
    
    @commands.command(name='sadoj')
    async def _sadoj(self, ctx):
        if bot.sadoj == 'open':
            print('SADoJ Application Link requested...')
            await ctx.send("Applications to be a Judge or Lawyer are open! Join San Andreas's lawful. Must have a minimum of 2 months in server and be 18 y/o. Click the link. <https://revivalrp.com/index.php?/forum/77-department-of-justice-applications/>")
        if bot.sadoj == 'closed':
            print('SADoJ Application link requested...')
            await ctx.send("Applications to be a Judge or Lawyer are currently closed! Stay tuned to when they open back up!")
            pass
        pass
    
    @commands.command(name='rosa')
    async def _rosa(self, ctx):
        if bot.rosa == 'open':
            print('RoSA Application Link requested...')
            await ctx.send("Applications to be a Realtor are open! Join San Andreas's realtors. Must have a minimum of 10 hours in server and be 18 y/o. Click the link. <https://revivalrp.com/index.php?/forum/48-rosa-applications/>")
        if bot.rosa == 'closed':
            print('RoSA Application link requested...')
            await ctx.send("Applications to be a Realtor are currently closed! Stay tuned to when they open back up!")
            pass
        pass
    
    @commands.command(name='sarcc')
    async def _sarcc(self, ctx):
        if bot.sarcc == 'open':
            print('SARCC Application Link requested...')
            await ctx.send("Applications to be a Dispatcher are open! Join San Andreas's calmest. Must have a minimum of 10 hours in server and be 18 y/o. Click the link. <https://revivalrp.com/index.php?/forum/48-rosa-applications/>")
        if bot.sarcc == 'closed':
            print('SARCC Application link requested...')
            await ctx.send("Applications to be a Dispatcher are currently closed! Stay tuned to when they open back up!")
            pass
        pass
    
    @commands.command(name='time')
    async def _time(self, ctx):
        time = datetime.datetime.utcnow() - datetime.timedelta(hours=7)
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

def setup(bot):
    bot.add_cog(CustomCog(bot))