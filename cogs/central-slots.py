import discord
import aiosqlite
import asyncio
import datetime
import random

from discord.ext import commands

bot = commands.Bot
min = 0
max = 174

class SlotsCog(commands.Cog, name="Slot Machine Cog"):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='slots')
    @commands.guild_only()
    async def _slots(self, ctx, amount):
        money = int(amount)
        async with aiosqlite.connect('D:\Central_Communications\database\economy.db') as db:
            cursor = await db.execute(f"SELECT money FROM economy WHERE user_id = {ctx.author.id}")
            currentbalance = await cursor.fetchone()
            balance = int(str(currentbalance[0]))
            if balance < money:
                await ctx.send(f':x: | {ctx.author.mention} You don\'t have enough <:kbucks:816469503365480498>K-Bucks in your account to make that bet!')
            else:
                otcm = random.randint(min, max)
                print('Pulling an outcome...')
        #Bell and Cherry
                if (otcm == 0):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_green(),
                    description="""**RESULT**:
        :bell: **|** :bell: **|** :bell:
        \u200b""")
                    embed.add_field(name='**WIN**', value=f'{money *2} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money + {money *2} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Bell, Bell, Bell')
                elif (otcm == 1):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :bell: **|** :bell: **|** :cherries:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Bell, Bell, Cherry')
                elif (otcm == 2):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :bell: **|** :cherries: **|** :cherries:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Bell, Cherry, Cherry')
                elif (otcm == 3):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :bell: **|** :cherries: **|** :bell:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Bell, Cherry, Bell')
                elif (otcm == 4):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :cherries: **|** :cherries: **|** :bell:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Cherry, Cherry, Bell')
                elif (otcm == 5):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :cherries: **|** :bell: **|** :bell:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Cherry, Bell, Bell')
                elif (otcm == 6):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :cherries: **|** :bell: **|** :cherries:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Cherry, Bell, Cherry')
        #Bell and Grape
                elif (otcm == 7):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_green(),
                    description="""RESULT:
        :grapes: **|** :grapes: **|** :grapes:
        \u200b""")
                    embed.add_field(name='**WIN**', value=f'{money *2} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money *2} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Grape, Grape, Grape')
                elif (otcm == 8):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :bell: **|** :bell: **|** :grapes:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Bell, Bell, Grape')
                elif (otcm == 9):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :bell: **|** :grapes: **|** :grapes:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Bell, Grape, Grape')
                elif (otcm == 10):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :bell: **|** :grapes: **|** :bell:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Bell, Grape, Bell')
                elif (otcm == 11):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :grapes: **|** :grapes: **|** :bell:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Grape, Grape, Bell')
                elif (otcm == 12):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :grapes: **|** :bell: **|** :bell:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Grape, Bell, Bell')
                elif (otcm == 13):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :grapes: **|** :bell: **|** :grapes:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Grape, Bell, Grape')
        #Bell and 7
                elif (otcm == 14):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_green(),
                    description="""RESULT:
        :seven: **|** :seven: **|** :seven:
        \u200b""")
                    embed.add_field(name='**JACKPOT**', value=f'{money *100} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money + {money *100} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 7, 7, 7')
                elif (otcm == 15):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :bell: **|** :bell: **|** :seven:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Bell, Bell, 7')
                elif (otcm == 16):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :bell: **|** :seven: **|** :seven:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Bell, 7, 7')
                elif (otcm == 17):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :bell: **|** :seven: **|** :bell:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Bell, 7, Bell')
                elif (otcm == 18):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :seven: **|** :seven: **|** :bell:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 7, 7, Bell')
                elif (otcm == 19):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :seven: **|** :bell: **|** :bell:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 7, Bell, Bell')
                elif (otcm == 20):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :seven: **|** :bell: **|** :seven:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 7, Bell, 7')
        # Bell and Clover
                elif (otcm == 21):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_green(),
                    description="""RESULT:
        :four_leaf_clover: **|** :four_leaf_clover: **|** :four_leaf_clover:
        \u200b""")
                    embed.add_field(name='**WIN**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Clover, Clover, Clover')
                elif (otcm == 22):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :bell: **|** :bell: **|** :four_leaf_clover:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Bell, Bell, Clover')
                elif (otcm == 23):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :bell: **|** :four_leaf_clover: **|** :four_leaf_clover:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Bell, Clover, Clover')
                elif (otcm == 24):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :bell: **|** :four_leaf_clover: **|** :bell:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Bell, Clover, Bell')
                elif (otcm == 25):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :four_leaf_clover: **|** :four_leaf_clover: **|** :bell:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Clover, Clover, Bell')
                elif (otcm == 26):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :four_leaf_clover: **|** :bell: **|** :bell:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Clover, Bell, Bell')
                elif (otcm == 27):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :four_leaf_clover: **|** :bell: **|** :four_leaf_clover:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Clover, Bell, Clover')
        #Bell and Bar
                elif (otcm == 28):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_green(),
                    description="""RESULT:
        <:bar:760572063139758090> **|** <:bar:760572063139758090> **|** <:bar:760572063139758090>
    \u200b""")
                    embed.add_field(name='**WIN**', value=f'{money *4} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money + {money *4} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Bar, Bar, Bar')
                elif (otcm == 29):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :bell: **|** :bell: **|** <:bar:760572063139758090>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Bell, Bell, Bar')
                elif (otcm == 30):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :bell: **|** <:bar:760572063139758090> **|** <:bar:760572063139758090>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Bell, Bar, Bar')
                elif (otcm == 31):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :bell: **|** <:bar:760572063139758090> **|** :bell:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Bell, Bar, Bell')
                elif (otcm == 32):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:bar:760572063139758090> **|** <:bar:760572063139758090> **|** :bell:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Bar, Bar, Bell')
                elif (otcm == 33):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:bar:760572063139758090> **|** :bell: **|** :bell:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Bar, Bell, Bell')
                elif (otcm == 34):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:bar:760572063139758090> **|** :bell: **|** <:bar:760572063139758090>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Bar, Bell, Bar')
        #Bell and 2 Bar
                elif (otcm == 35):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_green(),
                    description="""RESULT:
        <:2bar:760572097306689576> **|** <:2bar:760572097306689576> **|** <:2bar:760572097306689576>
        \u200b""")
                    embed.add_field(name='**WIN**', value=f'{money *8} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money + {money *8} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    await ctx.send("WIN x4!")
                    print('RESULT: 2Bar, 2Bar, 2Bar')
                elif (otcm == 36):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :bell: **|** :bell: **|** <:2bar:760572097306689576>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Bell, Bell, 2Bar')
                elif (otcm == 37):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :bell: **|** <:2bar:760572097306689576> **|** <:2bar:760572097306689576>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Bell, 2Bar, 2Bar')
                elif (otcm == 38):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :bell: **|** <:2bar:760572097306689576> **|** :bell:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Bell, 2Bar, Bell')
                elif (otcm == 39):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:2bar:760572097306689576> **|** <:2bar:760572097306689576> **|** :bell:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 2Bar, 2Bar, Bell')
                elif (otcm == 40):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:2bar:760572097306689576> **|** :bell: **|** :bell:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 2Bar, Bell, Bell')
                elif (otcm == 41):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:2bar:760572097306689576> **|** :bell: **|** <:2bar:760572097306689576>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 2Bar, Bell, 2Bar')
        #Bell and 3 Bar
                elif (otcm == 42):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_green(),
                    description="""RESULT:
        <:3bar:760572136384364585> **|** <:3bar:760572136384364585> **|** <:3bar:760572136384364585>
    \u200b""")
                    embed.add_field(name='**WIN**', value=f'{money *16} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money + {money *16} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 3Bar, 3Bar, 3Bar')
                elif (otcm == 43):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :bell: **|** :bell: **|** <:3bar:760572136384364585>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Bell, Bell, 3Bar')
                elif (otcm == 44):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :bell: **|** <:3bar:760572136384364585> **|** <:3bar:760572136384364585>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Bell, 3Bar, 3Bar')
                elif (otcm == 45):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :bell: **|** <:3bar:760572136384364585> **|** :bell:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Bell, 3Bar, Bell')
                elif (otcm == 46):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:3bar:760572136384364585> **|** <:3bar:760572136384364585> **|** :bell:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 3Bar, 3Bar, Bell')
                elif (otcm == 47):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:3bar:760572136384364585> **|** :bell: **|** :bell:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 3Bar, Bell, Bell')
                elif (otcm == 48):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:3bar:760572136384364585> **|** :bell: **|** <:3bar:760572136384364585>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 3Bar, Bell, 3Bar')                
        #Cherry and Grape
                elif (otcm == 49):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :cherries: **|** :cherries: **|** :grapes:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Cherry, Cherry, Grape')
                elif (otcm == 50):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :cherries: **|** :grapes: **|** :grapes:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Cherry, Grape, Grape')
                elif (otcm == 51):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :cherries: **|** :grapes: **|** :cherries:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Cherry, Grape, Cherry')
                elif (otcm == 52):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :grapes: **|** :grapes: **|** :cherries:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Grape, Grape, Cherry')
                elif (otcm == 53):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :grapes: **|** :cherries: **|** :cherries:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Grape, Cherry, Cherry')
                elif (otcm == 54):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :grapes: **|** :cherries: **|** :grapes:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Grape, Cherry, Grape')
        #Cherry and 7
                elif (otcm == 55):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :cherries: **|** :cherries: **|** :seven:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Cherry, Cherry, 7')
                elif (otcm == 56):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :cherries: **|** :seven: **|** :seven:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Cherry, 7, 7')
                elif (otcm == 57):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :cherries: **|** :seven: **|** :cherries:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Cherry, 7, Cherry')
                elif (otcm == 58):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :seven: **|** :seven: **|** :cherries:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 7, 7, Cherry')
                elif (otcm == 59):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :seven: **|** :cherries: **|** :cherries:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 7, Cherry, Cherry')
                elif (otcm == 60):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :seven: **|** :cherries: **|** :seven:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 7, Cherry, 7')
        #Cherry and Clover
                elif (otcm == 61):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :cherries: **|** :cherries: **|** :four_leaf_clover:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Cherry, Cherry, Clover')
                elif (otcm == 62):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :cherries: **|** :four_leaf_clover: **|** :four_leaf_clover:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Cherry, Clover, Clover')
                elif (otcm == 63):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :cherries: **|** :four_leaf_clover: **|** :cherries:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Cherry, Clover, Cherry')
                elif (otcm == 64):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :four_leaf_clover: **|** :four_leaf_clover: **|** :cherries:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Clover, Clover, Cherry')
                elif (otcm == 65):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :four_leaf_clover: **|** :cherries: **|** :cherries:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Clover, Cherry, Cherry')
                elif (otcm == 66):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :four_leaf_clover: **|** :cherries: **|** :four_leaf_clover:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Clover, Cherry, Clover')
        #Cherry and Bar
                elif (otcm == 67):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :cherries: **|** :cherries: **|** <:bar:760572063139758090>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Cherry, Cherry, Bar')
                elif (otcm == 68):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :cherries: **|** <:bar:760572063139758090> **|** <:bar:760572063139758090>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Cherry, Bar, Bar')
                elif (otcm == 69):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :cherries: **|** <:bar:760572063139758090> **|** :cherries:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Cherry, Bar, Cherry')
                elif (otcm == 70):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:bar:760572063139758090> **|** <:bar:760572063139758090> **|** :cherries:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Bar, Bar, Cherry')
                elif (otcm == 71):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:bar:760572063139758090> **|** :cherries: **|** :cherries:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Bar, Cherry, Cherry')
                elif (otcm == 72):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:bar:760572063139758090> **|** :cherries: **|** <:bar:760572063139758090>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Bar, Cherry, Bar')
        #Cherry and 2 Bar
                elif (otcm == 73):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :cherries: **|** :cherries: **|** <:2bar:760572097306689576>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Cherry, Cherry, 2Bar')
                elif (otcm == 74):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :cherries: **|** <:2bar:760572097306689576> **|** <:2bar:760572097306689576>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Cherry, 2Bar, 2Bar')
                elif (otcm == 75):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :cherries: **|** <:2bar:760572097306689576> **|** :cherries:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Cherry, 2Bar, Cherry')
                elif (otcm == 76):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:2bar:760572097306689576> **|** <:2bar:760572097306689576> **|** :cherries:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 2Bar, 2Bar, Cherry')
                elif (otcm == 77):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:2bar:760572097306689576> **|** :cherries: **|** :cherries:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 2Bar, Cherry, Cherry')
                elif (otcm == 78):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:2bar:760572097306689576> **|** :cherries: **|** <:2bar:760572097306689576>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 2Bar, Cherry, 2Bar')
        #Cherry and 3 Bar
                elif (otcm == 79):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :cherries: **|** :cherries: **|** <:3bar:760572136384364585>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Cherry, Cherry, 3Bar')
                elif (otcm == 80):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :cherries: **|** <:3bar:760572136384364585> **|** <:3bar:760572136384364585>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Cherry, 3Bar, 3Bar')
                elif (otcm == 81):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :cherries: **|** <:3bar:760572136384364585> **|** :cherries:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Cherry, 3Bar, Cherry')
                elif (otcm == 82):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:3bar:760572136384364585> **|** <:3bar:760572136384364585> **|** :cherries:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 3Bar, 3Bar, Cherry')
                elif (otcm == 83):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:3bar:760572136384364585> **|** :cherries: **|** :cherries:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 3Bar, Cherry, Cherry')
                elif (otcm == 84):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:3bar:760572136384364585> **|** :cherries: **|** <:3bar:760572136384364585>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 3Bar, Cherry, 3Bar')
        #Grape and 7
                elif (otcm == 85):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :grapes: **|** :grapes: **|** :seven:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Grape, Grape, 7')
                elif (otcm == 86):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :grape: **|** :seven: **|** :seven:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Grape, 7, 7')
                elif (otcm == 87):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :grapes: **|** :seven: **|** :grapes:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Grape, 7, Grape')
                elif (otcm == 88):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :seven: **|** :seven: **|** :grapes:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 7, 7, Grape')
                elif (otcm == 89):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :seven: **|** :grapes: **|** :grapes:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 7, Grape, Grape')
                elif (otcm == 90):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :seven: **|** :grapes: **|** :seven:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 7, Grape, 7')
        #Grape and Clover
                elif (otcm == 91):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :grapes: **|** :grapes: **|** :four_leaf_clover:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Grape, Grape, Clover')
                elif (otcm == 92):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :grapes: **|** :four_leaf_clover: **|** :four_leaf_clover:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Grape, Clover, Clover')
                elif (otcm == 93):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :grapes: **|** :four_leaf_clover: **|** :grapes:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Grape, Clover, Grape')
                elif (otcm == 94):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :four_leaf_clover: **|** :four_leaf_clover: **|** :grapes:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Clover, Clover, Grape')
                elif (otcm == 95):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :four_leaf_clover: **|** :grapes: **|** :grapes:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Clover, Grape, Grape')
                elif (otcm == 96):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :four_leaf_clover: **|** :grapes: **|** :four_leaf_clover:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Clover, Grape, Clover')
        #Grape and Bar
                elif (otcm == 97):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :grapes: **|** :grapes: **|** <:bar:760572063139758090>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Grape, Grape, Bar')
                elif (otcm == 98):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :grapes: **|** <:bar:760572063139758090> **|** <:bar:760572063139758090>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Grape, Bar, Bar')
                elif (otcm == 99):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :grapes: **|** <:bar:760572063139758090> **|** :grapes:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Grape, Bar, Grape')
                elif (otcm == 100):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:bar:760572063139758090> **|** <:bar:760572063139758090> **|** :grapes:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Bar, Bar, Grape')
                elif (otcm == 101):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:bar:760572063139758090> **|** :cherries: **|** :cherries:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Bar, Cherry, Cherry')
                elif (otcm == 102):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:bar:760572063139758090> **|** :grapes: **|** <:bar:760572063139758090>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Bar, Grape, Bar')
        #Grape and 2 Bar
                elif (otcm == 103):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :grapes: **|** :grapes: **|** <:2bar:760572097306689576>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Grape, Grape, 2Bar')
                elif (otcm == 104):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :grapes: **|** <:2bar:760572097306689576> **|** <:2bar:760572097306689576>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Grape, 2Bar, 2Bar')
                elif (otcm == 105):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :grapes: **|** <:2bar:760572097306689576> **|** :grapes:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Grape, 2Bar, Grape')
                elif (otcm == 106):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:2bar:760572097306689576> **|** <:2bar:760572097306689576> **|** :grapes:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 2Bar, 2Bar, Grape')
                elif (otcm == 107):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:2bar:760572097306689576> **|** :grapes: **|** :grapes:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 2Bar, Grape, Grape')
                elif (otcm == 108):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:2bar:760572097306689576> **|** :grapes: **|** <:2bar:760572097306689576>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 2Bar, Grape, 2Bar')
        #Grape and 3 Bar
                elif (otcm == 109):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :grapes: **|** :grapes: **|** <:3bar:760572136384364585>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Grape, Grape, 3Bar')
                elif (otcm == 110):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :grapes: **|** <:3bar:760572136384364585> **|** <:3bar:760572136384364585>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Grape, 3Bar, 3Bar')
                elif (otcm == 111):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :grapes: **|** <:3bar:760572136384364585> **|** :grapes:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Grape, 3Bar, Grape')
                elif (otcm == 112):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:3bar:760572136384364585> **|** <:3bar:760572136384364585> **|** :grapes:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 3Bar, 3Bar, Grape')
                elif (otcm == 113):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:3bar:760572136384364585> **|** :grapes: **|** :grapes:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 3Bar, Grape, Grape')
                elif (otcm == 114):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:3bar:760572136384364585> **|** :grapes: **|** <:3bar:760572136384364585>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 3Bar, Grape, 3Bar')
        #7 and Clover
                elif (otcm == 115):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :seven: **|** :seven: **|** :four_leaf_clover:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 7, 7, Clover')
                elif (otcm == 116):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :seven: **|** :four_leaf_clover: **|** :four_leaf_clover:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 7, Clover, Clover')
                elif (otcm == 117):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :seven: **|** :four_leaf_clover: **|** :seven:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 7, Clover, 7')
                elif (otcm == 118):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :four_leaf_clover: **|** :four_leaf_clover: **|** :seven:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Clover, Clover, 7')
                elif (otcm == 119):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :four_leaf_clover: **|** :seven: **|** :seven:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Clover, 7, 7')
                elif (otcm == 120):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :four_leaf_clover: **|** :seven: **|** :four_leaf_clover:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Clover, 7, Clover')
        #7 and Bar
                elif (otcm == 121):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :seven: **|** :seven: **|** <:bar:760572063139758090>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 7, 7, Bar')
                elif (otcm == 122):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :seven: **|** <:bar:760572063139758090> **|** <:bar:760572063139758090>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 7, Bar, Bar')
                elif (otcm == 123):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :seven: **|** <:bar:760572063139758090> **|** :seven:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 7, Bar, 7')
                elif (otcm == 124):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:bar:760572063139758090> **|** <:bar:760572063139758090> **|** :seven:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Bar, Bar, 7')
                elif (otcm == 125):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:bar:760572063139758090> **|** :seven: **|** :seven:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Bar, 7, 7')
                elif (otcm == 126):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:bar:760572063139758090> **|** :seven: **|** <:bar:760572063139758090>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Bar, 7, Bar')
        #7 and 2 Bar
                elif (otcm == 127):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :seven: **|** :seven: **|** <:2bar:760572097306689576>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 7, 7, 2Bar')
                elif (otcm == 128):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :seven: **|** <:2bar:760572097306689576> **|** <:2bar:760572097306689576>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 7, 2Bar, 2Bar')
                elif (otcm == 129):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :seven: **|** <:2bar:760572097306689576> **|** :seven:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 7, 2Bar, 7')
                elif (otcm == 130):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:2bar:760572097306689576> **|** <:2bar:760572097306689576> **|** :seven:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 2Bar, 2Bar, 7')
                elif (otcm == 131):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:2bar:760572097306689576> **|** :seven: **|** :seven:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 2Bar, 7, 7')
                elif (otcm == 132):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:2bar:760572097306689576> **|** :seven: **|** <:2bar:760572097306689576>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 2Bar, 7, 2Bar')
        #7 and 3 Bar
                elif (otcm == 133):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :seven: **|** :seven: **|** <:3bar:760572136384364585>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 7, 7, 3Bar')
                elif (otcm == 134):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :seven: **|** <:3bar:760572136384364585> **|** <:3bar:760572136384364585>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 7, 3Bar, 3Bar')
                elif (otcm == 135):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :seven: **|** <:3bar:760572136384364585> **|** :seven:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 7, 3Bar, 7')
                elif (otcm == 136):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:3bar:760572136384364585> **|** <:3bar:760572136384364585> **|** :seven:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 3Bar, 3Bar, 7')
                elif (otcm == 137):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:3bar:760572136384364585> **|** :seven: **|** :seven:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 3Bar, 7, 7')
                elif (otcm == 138):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:3bar:760572136384364585> **|** :seven: **|** <:3bar:760572136384364585>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 3Bar, 7, 3Bar')
        #Clover and Bar
                elif (otcm == 139):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :four_leaf_clover: **|** :four_leaf_clover: **|** <:bar:760572063139758090>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Clover, Clover, Bar')
                elif (otcm == 140):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :four_leaf_clover: **|** <:bar:760572063139758090> **|** <:bar:760572063139758090>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Clover, Bar, Bar')
                elif (otcm == 141):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :four_leaf_clover: **|** <:bar:760572063139758090> **|** :four_leaf_clover:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Clover, Bar, Clover')
                elif (otcm == 142):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:bar:760572063139758090> **|** <:bar:760572063139758090> **|** :four_leaf_clover:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Bar, Bar, Clover')
                elif (otcm == 143):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:bar:760572063139758090> **|** :four_leaf_clover: **|** :four_leaf_clover:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Bar, Clover, Clover')
                elif (otcm == 144):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:bar:760572063139758090> **|** :four_leaf_clover: **|** <:bar:760572063139758090>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Bar, Clover, Bar')
        #Clover and 2 Bar
                elif (otcm == 145):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :four_leaf_clover: **|** :four_leaf_clover: **|** <:2bar:760572097306689576>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Clover, Clover, 2Bar')
                elif (otcm == 146):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :four_leaf_clover: **|** <:2bar:760572097306689576> **|** <:2bar:760572097306689576>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Clover, 2Bar, 2Bar')
                elif (otcm == 147):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :four_leaf_clover: **|** <:2bar:760572097306689576> **|** :four_leaf_clover:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Clover, 2Bar, Clover')
                elif (otcm == 148):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:2bar:760572097306689576> **|** <:2bar:760572097306689576> **|** :four_leaf_clover:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 2Bar, 2Bar, Clover')
                elif (otcm == 149):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:2bar:760572097306689576> **|** :four_leaf_clover: **|** :four_leaf_clover:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 2Bar, Clover, Clover')
                elif (otcm == 150):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:2bar:760572097306689576> **|** :four_leaf_clover: **|** <:2bar:760572097306689576>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 2Bar, Clover, 2Bar')
        #Clover and 3 Bar
                elif (otcm == 151):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :four_leaf_clover: **|** :four_leaf_clover: **|** <:3bar:760572136384364585>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Clover, Clover, 3Bar')
                elif (otcm == 152):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :four_leaf_clover: **|** <:3bar:760572136384364585> **|** <:3bar:760572136384364585>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Clover, 3Bar, 3Bar')
                elif (otcm == 153):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        :four_leaf_clover: **|** <:3bar:760572136384364585> **|** :four_leaf_clover:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Clover, 3Bar, Clover')
                elif (otcm == 154):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:3bar:760572136384364585> **|** <:3bar:760572136384364585> **|** :four_leaf_clover:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 3Bar, 3Bar, Clover')
                elif (otcm == 155):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:3bar:760572136384364585> **|** :four_leaf_clover: **|** :four_leaf_clover:
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 3Bar, Clover, Clover')
                elif (otcm == 156):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:3bar:760572136384364585> **|** :four_leaf_clover: **|** <:3bar:760572136384364585>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 3Bar, Clover, 3Bar')
        #Bar and 2 Bar
                elif (otcm == 157):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:bar:760572063139758090> **|** <:bar:760572063139758090> **|** <:2bar:760572097306689576>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Bar, Bar, 2Bar')
                elif (otcm == 158):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:bar:760572063139758090> **|** <:2bar:760572097306689576> **|** <:2bar:760572097306689576>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Bar, 2Bar, 2Bar')
                elif (otcm == 159):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:bar:760572063139758090> **|** <:2bar:760572097306689576> **|** <:bar:760572063139758090>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Bar, 2Bar, Bar')
                elif (otcm == 160):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:2bar:760572097306689576> **|** <:2bar:760572097306689576> **|** <:bar:760572063139758090>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 2Bar, 2Bar, Bar')
                elif (otcm == 161):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:2bar:760572097306689576> **|** <:bar:760572063139758090> **|** <:bar:760572063139758090>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 2Bar, Bar, Bar')
                elif (otcm == 162):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:2bar:760572097306689576> **|** <:bar:760572063139758090> **|** <:2bar:760572097306689576>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 2Bar, Bar, 2Bar')
        #2 Bar and 3 Bar
                elif (otcm == 163):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:bar:760572063139758090> **|** <:bar:760572063139758090> **|** <:3bar:760572136384364585>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Bar, Bar, 3Bar')
                elif (otcm == 164):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:bar:760572063139758090> **|** <:3bar:760572136384364585> **|** <:3bar:760572136384364585>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Bar, 3Bar, 3Bar')
                elif (otcm == 165):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:bar:760572063139758090> **|** <:3bar:760572136384364585> **|** <:bar:760572063139758090>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: Bar, 3Bar, Bar')
                elif (otcm == 166):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:3bar:760572136384364585> **|** <:3bar:760572136384364585> **|** <:bar:760572063139758090>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 3Bar, 3Bar, Bar')
                elif (otcm == 167):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:3bar:760572136384364585> **|** <:bar:760572063139758090> **|** <:bar:760572063139758090>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 3Bar, Bar, Bar')
                elif (otcm == 168):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:3bar:760572136384364585> **|** <:bar:760572063139758090> **|** <:3bar:760572136384364585>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 3Bar, Bar, 3Bar')
        #2 Bar and 3 Bar
                elif (otcm == 169):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:2bar:760572097306689576> **|** <:2bar:760572097306689576> **|** <:3bar:760572136384364585>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 2Bar, 2Bar, 3Bar')
                elif (otcm == 170):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:2bar:760572097306689576> **|** <:3bar:760572136384364585> **|** <:3bar:760572136384364585>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 2Bar, 3Bar, 3Bar')
                elif (otcm == 171):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:2bar:760572097306689576> **|** <:3bar:760572136384364585> **|** <:2bar:760572097306689576>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 2Bar, 3Bar, 2Bar')
                elif (otcm == 172):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:3bar:760572136384364585> **|** <:3bar:760572136384364585> **|** <:2bar:760572097306689576>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 3Bar, 3Bar, 2Bar')
                elif (otcm == 173):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:3bar:760572136384364585> **|** <:2bar:760572097306689576> **|** <:2bar:760572097306689576>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 3Bar, 2Bar, 2Bar')
                elif (otcm == 174):
                    embed = discord.Embed(
                    type='rich',
                    colour=discord.Color.dark_red(),
                    description="""RESULT:
        <:3bar:760572136384364585> **|** <:2bar:760572097306689576> **|** <:3bar:760572136384364585>
        \u200b""")
                    embed.add_field(name='**LOSE**', value=f'{money} <:kbucks:816469503365480498>K-Bucks!', inline=True)
                    await db.execute(f"UPDATE economy SET money = money - {money} WHERE user_id = {ctx.author.id}")
                    await asyncio.sleep(0.5)
                    print('RESULT: 3Bar, 2Bar, 3Bar')
                    pass
                await db.commit()
                embed.title = '**SLOT MACHINE**'
                embed.set_author(name=ctx.author, icon_url=str(ctx.author.avatar_url))
                embed.set_footer(text="Developed by LIPD Productions Inc.#1205", icon_url=str(ctx.guild.icon_url))
                embed.timestamp=datetime.datetime.utcnow()
                await ctx.send(embed=embed)
                pass
            pass
        pass
        
    pass
    
def setup(bot):
    bot.add_cog(SlotsCog(bot))