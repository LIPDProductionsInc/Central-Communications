import discord
import asyncio
import datetime
import random

from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType

class EjectCog(commands.Cog, name="Eject Command"):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='eject')
    async def _eject(self, ctx, member: discord.Member):
        options = [
         'was an Imposter',
         'was not an Imposter',
         'was the Imposter',
         'was not the Imposter']
        imposters = [
            '0 Imposters remain...',
            '1 Imposter remains...',
            '2 Imposters remain...',
            '3 Imposters remain...']
        if member == ctx.author:
            await ctx.send(f'Now {ctx.author.mention}, why would you want to do that???')
        elif member == self.bot.user:
            await ctx.send(f'{ctx.author.mention}: YOU CAN\'T EJECT ME! I\'M RUNNING THIS THING!!!')
        else:
            option = random.choice(options)
            imposter = random.randint(0, 3)
            print(f'Ejected {member}')
            print(f'{member} {option}')
            if imposter == 2 or imposter == 0 or imposter == 3:
                print(f'{imposter} Imposters remain...')
                embed = discord.Embed(
                    title='VOTE THE IMPOSTER OUT!',
                    type='rich',
                    description=f'''
{ctx.author.mention} ejected {member.mention}
\n
*{member} {option}*
\n
**{imposter} Imposters remain...**
''')
                embed.set_author(name=ctx.author, icon_url=str(ctx.author.avatar_url))
                embed.set_footer(text="Developed by LIPD Productions Inc.#1205", icon_url=str(ctx.guild.icon_url))
                embed.timestamp=datetime.datetime.utcnow()
                await ctx.send(embed=embed)
            else:
                print(f'{imposter} Imposter remains...')
                embed = discord.Embed(
                    title='VOTE THE IMPOSTER OUT!',
                    type='rich',
                    description=f'''
{ctx.author.mention} ejected {member.mention}
\n
*{member} {option}*
\n
**{imposter} Imposter remains...**
''')
                embed.set_author(name=ctx.author, icon_url=str(ctx.author.avatar_url))
                embed.set_footer(text="Developed by LIPD Productions Inc.#1205", icon_url=str(ctx.guild.icon_url))
                embed.timestamp=datetime.datetime.utcnow()
                await ctx.send(embed=embed)
                pass
            pass
        pass
    
    pass

def setup(bot):
    bot.add_cog(EjectCog(bot))