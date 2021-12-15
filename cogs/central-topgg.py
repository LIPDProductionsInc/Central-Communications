import discord
import pymongo

from discord.ext import commands
from pymongo import MongoClient


class TopGGCog(commands.Cog, name='Top.GG Server Vote Count'):
    
    def __init__(self, bot):
        self.bot = bot
        pass
    
    
    
    pass

def setup(bot):
    bot.add_cog(TopGGCog(bot))