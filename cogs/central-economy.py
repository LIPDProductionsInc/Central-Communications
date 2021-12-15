import discord
import aiosqlite
import asyncio
import datetime
import random

from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType

class EconomyCog(commands.Cog, name = "Economy Cog"):
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='register')
    async def _register(self, ctx):
        if all(ctx.author._roles.has(_id) for _id in [794387448222318615, 732002571580997732]):
            async with aiosqlite.connect('D:\Central_Communications\database\economy.db') as db:
                await db.execute(f"INSERT INTO economy values({ctx.author.id},'{ctx.author}',4000,'Unemployed','None')")
                print(f'{ctx.author} added to the database!')
                await db.commit()
                print('Saved!')
                pass
        elif ctx.author._roles.has(794387448222318615):
            async with aiosqlite.connect('D:\Central_Communications\database\economy.db') as db:
                await db.execute(f"INSERT INTO economy values({ctx.author.id},'{ctx.author}',2000,'Unemployed','None')")
                print(f'{ctx.author} added to the database!')
                await db.commit()
                print('Saved!')
                pass
        elif ctx.author._roles.has(732002571580997732):
            async with aiosqlite.connect('D:\Central_Communications\database\economy.db') as db:
                await db.execute(f"INSERT INTO economy values({ctx.author.id},'{ctx.author}',2000,'Unemployed','None')")
                print(f'{ctx.author} added to the database!')
                await db.commit()
                print('Saved!')
                pass
        else:
            async with aiosqlite.connect('D:\Central_Communications\database\economy.db') as db:
                await db.execute(f"INSERT INTO economy values({ctx.author.id},'{ctx.author}',1000,'Unemployed','None')")
                print(f'{ctx.author} added to the database!')
                await db.commit()
                print('Saved!')
                pass
            pass
        async with aiosqlite.connect('D:\Central_Communications\database\economy.db') as db:
            cursor = await db.execute(f"SELECT money FROM economy WHERE user_id = {ctx.author.id}")
            balance = await cursor.fetchone()
            embed=discord.Embed(
                type='rich',
                colour=discord.Color.dark_green(),
                description=f'{ctx.author.mention}: You have been given {balance[0]} <:kbucks:816469503365480498>K-Bucks for registering!'
                )
            embed.set_author(name=ctx.author, icon_url=str(ctx.author.avatar_url))
            embed.set_footer(text="Developed by LIPD Productions Inc.#1205", icon_url=str(ctx.guild.icon_url))
            embed.timestamp=datetime.datetime.utcnow()
            await ctx.send(embed=embed)
        pass
    
    @commands.command(name='daily')
    @commands.cooldown(1,86400,type=BucketType.member)
    async def _daily(self, ctx):
        if all(ctx.author._roles.has(_id) for _id in [794387448222318615, 732002571580997732]):
            async with aiosqlite.connect('D:\Central_Communications\database\economy.db') as db:
                await db.execute(f"SELECT money FROM economy WHERE user_id = {ctx.author.id}")
                await db.execute(f"UPDATE economy SET money = money + 1000 WHERE user_id = {ctx.author.id}")
                print(f'Gave {ctx.author} 1,000 K-Bucks for the daily check in')
                await db.commit()
                print('Saved!')
                embed=discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_green(),
                    description=f'{ctx.author.mention}: You have been given 1,000 <:kbucks:816469503365480498>K-Bucks for your daily check-in!'
                    )
                pass
        elif ctx.author._roles.has(794387448222318615):
            async with aiosqlite.connect('D:\Central_Communications\database\economy.db') as db:
                await db.execute(f"SELECT money FROM economy WHERE user_id = {ctx.author.id}")
                await db.execute(f"UPDATE economy SET money = money + 500 WHERE user_id = {ctx.author.id}")
                print(f'Gave {ctx.author} 500 K-Bucks for the daily check in')
                await db.commit()
                print('Saved!')
                embed=discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_green(),
                    description=f'{ctx.author.mention}: You have been given 500 <:kbucks:816469503365480498>K-Bucks for your daily check-in!'
                    )
                pass
        elif ctx.author._roles.has(732002571580997732):
            async with aiosqlite.connect('D:\Central_Communications\database\economy.db') as db:
                await db.execute(f"SELECT money FROM economy WHERE user_id = {ctx.author.id}")
                await db.execute(f"UPDATE economy SET money = money + 500 WHERE user_id = {ctx.author.id}")
                print(f'Gave {ctx.author} 500 K-Bucks for the daily check in')
                await db.commit()
                print('Saved!')
                embed=discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_green(),
                    description=f'{ctx.author.mention}: You have been given 500 <:kbucks:816469503365480498>K-Bucks for your daily check-in!'
                    )
                pass
        else:
            async with aiosqlite.connect('D:\Central_Communications\database\economy.db') as db:
                await db.execute(f"SELECT money FROM economy WHERE user_id = {ctx.author.id}")
                await db.execute(f"UPDATE economy SET money = money + 250 WHERE user_id = {ctx.author.id}")
                print(f'Gave {ctx.author} 250 K-Bucks for the daily check in')
                await db.commit()
                print('Saved!')
                embed=discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_green(),
                    description=f'{ctx.author.mention}: You have been given 250 <:kbucks:816469503365480498>K-Bucks for your daily check-in!'
                    )
                pass
            pass
        embed.set_author(name=ctx.author, icon_url=str(ctx.author.avatar_url))
        embed.set_footer(text="Developed by LIPD Productions Inc.#1205", icon_url=str(ctx.guild.icon_url))
        embed.timestamp=datetime.datetime.utcnow()
        await ctx.send(embed=embed)
        pass
    
    @commands.command(name='work')
    @commands.cooldown(1,3600,type=BucketType.member)
    async def _work(self, ctx):
        if all(ctx.author._roles.has(_id) for _id in [794387448222318615, 732002571580997732]):
            async with aiosqlite.connect('D:\Central_Communications\database\economy.db') as db:
                await db.execute(f"SELECT money FROM economy WHERE user_id = {ctx.author.id}")
                await db.execute(f"UPDATE economy SET money = money + 1200 WHERE user_id = {ctx.author.id}")
                print(f'Gave {ctx.author} 1,200 K-Bucks for the daily check in')
                await db.commit()
                print('Saved!')
                embed=discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_green(),
                    description=f'{ctx.author.mention}: You have been given 1,200 <:kbucks:816469503365480498>K-Bucks for collecting your unemployment benefit!'
                    )
                pass
        elif ctx.author._roles.has(794387448222318615):
            async with aiosqlite.connect('D:\Central_Communications\database\economy.db') as db:
                await db.execute(f"SELECT money FROM economy WHERE user_id = {ctx.author.id}")
                await db.execute(f"UPDATE economy SET money = money + 600 WHERE user_id = {ctx.author.id}")
                print(f'Gave {ctx.author} 600 K-Bucks for working')
                await db.commit()
                print('Saved!')
                embed=discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_green(),
                    description=f'{ctx.author.mention}: You have been given 600 <:kbucks:816469503365480498>K-Bucks for collecting your unemployment benefit!'
                    )
                pass
        elif ctx.author._roles.has(732002571580997732):
            async with aiosqlite.connect('D:\Central_Communications\database\economy.db') as db:
                await db.execute(f"SELECT money FROM economy WHERE user_id = {ctx.author.id}")
                await db.execute(f"UPDATE economy SET money = money + 600 WHERE user_id = {ctx.author.id}")
                print(f'Gave {ctx.author} 600 K-Bucks for working')
                await db.commit()
                print('Saved!')
                embed=discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_green(),
                    description=f'{ctx.author.mention}: You have been given 600 <:kbucks:816469503365480498>K-Bucks for collecting your unemployment benefit!'
                    )
                pass
        else:
            async with aiosqlite.connect('D:\Central_Communications\database\economy.db') as db:
                await db.execute(f"SELECT money FROM economy WHERE user_id = {ctx.author.id}")
                await db.execute(f"UPDATE economy SET money = money + 300 WHERE user_id = {ctx.author.id}")
                print(f'Gave {ctx.author} 300 K-Bucks for working')
                await db.commit()
                print('Saved!')
                embed=discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_green(),
                    description=f'{ctx.author.mention}: You have been given 300 <:kbucks:816469503365480498>K-Bucks for collecting your unemployment benefit!'
                    )
                pass
            pass
        embed.set_author(name=ctx.author, icon_url=str(ctx.author.avatar_url))
        embed.set_footer(text="Developed by LIPD Productions Inc.#1205", icon_url=str(ctx.guild.icon_url))
        embed.timestamp=datetime.datetime.utcnow()
        await ctx.send(embed=embed)
        pass
    
    @commands.command(name='flipcoin', aliases=['coinflip'])
    async def flipcoin(self, ctx, side, amount):
        amount = int(amount)
        if side == 'heads' or side == 'tails':
            otcm = random.choice(['heads', 'tails'])
            if side != otcm:
                async with aiosqlite.connect('D:\Central_Communications\database\economy.db') as db:
                    cursor = await db.execute(f"SELECT money FROM economy WHERE user_id = {ctx.author.id}")
                    currentbalance = await cursor.fetchone()
                    await db.execute(f"UPDATE economy SET money = money - {amount} WHERE user_id = {ctx.author.id}")
                    print(f'{ctx.author} lost {amount} K-Bucks')
                    await db.commit()
                    print('Saved!')
                    pass
                embed=discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description=f'''{ctx.author.mention}'s Guess: {side.title()}
Result: {''.join(otcm).title()}
{ctx.author.mention} lost {amount} <:kbucks:816469503365480498>K-Bucks!'''
                    )
                embed.set_author(name=ctx.author, icon_url=str(ctx.author.avatar_url))
                embed.set_footer(text="Developed by LIPD Productions Inc.#1205", icon_url=str(ctx.guild.icon_url))
                embed.timestamp=datetime.datetime.utcnow()
            else:
                async with aiosqlite.connect('D:\Central_Communications\database\economy.db') as db:
                    cursor = await db.execute(f"SELECT money FROM economy WHERE user_id = {ctx.author.id}")
                    currentbalance = await cursor.fetchone()
                    await db.execute(f"UPDATE economy SET money = money + {amount} WHERE user_id = {ctx.author.id}")
                    print(f'{ctx.author} won {amount} K-Bucks')
                    await db.commit()
                    print('Saved!')
                    pass
                embed=discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_green(),
                    description=f'''{ctx.author.mention}'s Guess: {side.title()}
Result: {''.join(otcm).title()}
{ctx.author.mention} won {amount} <:kbucks:816469503365480498>K-Bucks!'''
                    )
                embed.set_author(name=ctx.author, icon_url=str(ctx.author.avatar_url))
                embed.set_footer(text="Developed by LIPD Productions Inc.#1205", icon_url=str(ctx.guild.icon_url))
                embed.timestamp=datetime.datetime.utcnow()
                pass
            await ctx.send(embed=embed)
        else:
            await ctx.send(f':x: | {ctx.author.mention}: Only heads or tails, please!')
            pass
        pass
    
    @commands.command(name='bountycheck')
    @commands.guild_only()
    async def _bountycheck(self, ctx):
        async with aiosqlite.connect('D:\Central_Communications\database\economy.db') as db:
            cursor = await db.execute(f"SELECT bounty FROM economy WHERE user_id = {ctx.author.id}")
            bounty = await cursor.fetchone()
            bountycheck = bounty[0]
            if bountycheck ==  '0':
                embed=discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_green(),
                    description=f'{ctx.author.mention}: You do not have a bounty placed on you!'
                    )
                embed.set_author(name=ctx.author, icon_url=str(ctx.author.avatar_url))
                embed.set_footer(text="Developed by LIPD Productions Inc.#1205", icon_url=str(ctx.guild.icon_url))
                embed.timestamp=datetime.datetime.utcnow()
                await ctx.send(embed=embed)
            else:
                embed=discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description=f'{ctx.author.mention}: You have a {bounty[0]} bounty placed on you!'
                    )
                embed.set_author(name=ctx.author, icon_url=str(ctx.author.avatar_url))
                embed.set_footer(text="Developed by LIPD Productions Inc.#1205", icon_url=str(ctx.guild.icon_url))
                embed.timestamp=datetime.datetime.utcnow()
                await ctx.send(embed=embed)
                pass
            pass
        pass
    
    @commands.command(name='bounty')
    @commands.guild_only()
    async def _bounty(self, ctx, amount, member: discord.Member):
        print(f'Bounty on {member}')
        user = ctx.bot.get_user(id=(ctx.author.id))
        bountyperson = ctx.bot.get_user(id=(member.id))
        async with aiosqlite.connect('D:\Central_Communications\database\economy.db') as db:
            await db.execute(f"UPDATE economy SET bounty = bounty + {amount} WHERE user_id = {member.id}")
            print(f'Placed a {amount} bounty on {member}')
            await db.execute(f"UPDATE economy SET money = money - {amount} WHERE user_id = {ctx.author.id}")
            print(f'{ctx.author} paid for bounty')
            await db.commit()
            print('Saved!')
            pass
        await ctx.message.delete()
        await user.send(f'I have placed the {amount} bounty on {member.mention} successfully!')
        await bountyperson.send(f'''
Hello {member}!

I'm hearing chatter that someone has placed a {amount} bounty on you. I do not know who placed it , but you might want to hang low for a bit. Please note that you cannot claim this bounty yourself. Any attempt to do so will result in the bounty being added back, and the credit being taken from your account.

Good luck!
''')
        pass
    
    @commands.command(name='balance', aliases=['bal'])
    async def _balance(self, ctx):
        async with aiosqlite.connect('D:\Central_Communications\database\economy.db') as db:
            cursor = await db.execute(f"SELECT money FROM economy WHERE user_id = {ctx.author.id}")
            balance = await cursor.fetchone()
            await ctx.send(f'**You have {balance[0]} <:kbucks:816469503365480498>K-Bucks in your bank!**')
            pass
    
    @commands.command(name='remove')
    @commands.has_permissions(manage_guild=True)
    async def _remove(self, ctx, member: discord.Member):
        async with aiosqlite.connect('D:\Central_Communications\database\economy.db') as db:
            await db.execute(f"DELETE FROM economy WHERE user_id = {member.id}")
            print(f'{ctx.author} removed the database!')
            await db.commit()
            print('Saved!')
            await ctx.send('Removed {member.mention} from the database!')
            pass
        pass
    
    @commands.command(name='give')
    @commands.has_permissions(manage_guild=True)
    async def _give(self, ctx, amount, member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.author  # set member as the author
            
        async with aiosqlite.connect('D:\Central_Communications\database\economy.db') as db:
            cursor = await db.execute(f"SELECT money FROM economy WHERE user_id = {member.id}")
            currentbalance = await cursor.fetchone()
            await db.execute(f"UPDATE economy SET money = money + {amount} WHERE user_id = {member.id}")
            print(f'Gave {member} {amount} K-Bucks')
            await db.commit()
            print('Saved!')
            pass
        embed=discord.Embed(
                type='rich',
                colour=discord.Color.dark_green(),
                description=f'{ctx.author.mention}: Gave {amount} <:kbucks:816469503365480498>K-Bucks to {member.mention}!'
                )
        embed.set_author(name=ctx.author, icon_url=str(ctx.author.avatar_url))
        embed.set_footer(text="Developed by LIPD Productions Inc.#1205", icon_url=str(ctx.guild.icon_url))
        embed.timestamp=datetime.datetime.utcnow()
        await ctx.send(embed=embed)
        pass
    
    pass

def setup(bot):
    bot.add_cog(EconomyCog(bot))