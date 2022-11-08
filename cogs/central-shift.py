# written by Alexa Hunts (Alexm#3020)
# This is a small little game that randomly assigns weapons, vehicles, and a location.
import discord
import asyncio
import datetime
import random

from discord.ext import commands

bot = commands.Bot

class shiftCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='startshift')
    async def _startshift(self, ctx,):
        print('someone is getting ready to go out on shift')
        
        pistol_list = ['Glock 19', 'Glock 22','Smith & Wesson M&P 9', 'Beretta Model 92', 'Sig Sauer P226', 'Heckler and Koch HK45', 'Ruger LC9', 'Colt M1911', 'Desert Eagle', 'Hi-Point Model C9', 'Luger']
        longgun_list =['AR-15', 'AK-47', 'Mossberg 500', 'Barrett M107', 'M1 Garand', 'Mosin Nagant', 'Musket', 'M32 Rotary Grenade Launcher' ]
        vehicle_list = ['Crown Victoria Police Intercepter', 'Chevy Caprice', 'Ford Taurus', 'Chevy Impala', 'Ford Mustang', 'Dodge Charger', 'F-150', 'FPIU']
        location_list = ['Legion Square', 'Vinewood', 'Mirror Park', 'Davis', 'Vespucci Beach', 'Rockford Hills', 'Little Seoul', 'La Puerta', 'Los Santos International Airport', 'Port of Los Santos', 'Grape Seed', 'Sandy Shores', 'Paleto Bay', 'Harmony', 'Stab City', 'Mount Chiliad', 'Dignaty Village', 'Grand Senora Desert']

        pistol = (random.choice(pistol_list))
        longgun = (random.choice(longgun_list))
        vehicle = (random.choice(vehicle_list))
        location = (random.choice(location_list))

        await ctx.send(f'You go to the armory and pull out your {pistol} and your {longgun}. You go to the motor pool and are assigned a {vehicle} and start patrolling near {location}.')
        pass

   

def setup(bot):
    bot.add_cog(shiftCog(bot))