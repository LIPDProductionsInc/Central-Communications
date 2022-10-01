import discord
import asyncio
import datetime
import logging
import os
import sys, traceback

from discord.ext import commands
from discord.ext.commands import Bot
from dotenv import load_dotenv
load_dotenv()

def get_prefix(bot, message):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""

    # Notice how you can use spaces in prefixes. Try to keep them simple though.
    prefixes = ['cc!', 'Cc!', 'CC!']

    # If we are in a guild, we allow for the user to mention us or use any of the prefixes in our list.
    return commands.when_mentioned_or(*prefixes)(bot, message)

bot = commands.Bot(command_prefix=get_prefix, help_command=None, case_insensitive=True, intents=discord.Intents.all(), fetch_offline_users=True)

activity = discord.Activity(name='Kallam get older and older | cc!help', type=discord.ActivityType.watching)
status = discord.Status.online

initial_extensions = ['cogs.central-economy',
                      'cogs.central-errors',
                      'cogs.central-eject',
                      'cogs.central-custom',
                      'cogs.central-owner',
                      'cogs.central-slots'
                      ]


admin_help = """
**cc!kick**: Kicks a user

**cc!ban**: Bans a user

**cc!adminhelp**: Sends this page

**cc!open <department>**: Sets the application status for the department on the bot to open

**cc!close <department>**: Sets the application status for the department on the bot to closed

**cc!note**: Makes a note about a member in the logs
"""

help_message = """
**cc!discordhelp**: Help related to Discord stuff, syncing, etc.

**cc!generalhelp**: List of commands that can be used
"""

help_discord = """
**cc!sync**: How to sync your Discord and Twitch

**cc!avtarsubmission**: Submit your design for the avatar of Central Communications. ||Serious submissions only!!!||

**cc!specs**: Kallam's PC specs

**cc!po-box**: Kallam's PO box

**cc!time**: Kallam's current time

**cc!secretlab**: Kallam's chair
"""

help_general = """
**cc!prime**: Learn how to get a FREE subscription with your Amazon/Twitch Prime account

**cc!service**: Kallam's LEO service

**cc!ping**: Gets the bot's ping

**cc!merch**: Get your Trooper Kallam merch

**cc!version**:  Current version of the bot
"""

@bot.event
async def on_invite_create(invite):
    if invite.guild.id == 731391566945714226:
        channel = bot.get_channel(os.getenv('GuildLogChannel'))
        embed = discord.Embed(
            title='**Invite created for Trooper K Station**',
            type='rich',
            colour=discord.Colour.blue(),
            description=f'{invite.url}')
        embed.set_author(name=invite.inviter, icon_url=str(invite.inviter.avatar_url))
        embed.set_footer(text=f'ID: {invite.inviter.id}')
        embed.timestamp=datetime.datetime.utcnow()
        embed.add_field(name='Inviter', value=f'{invite.inviter.mention}', inline=True).add_field(name='Channel', value=f'{invite.channel.mention}', inline=True)
        await channel.send(embed=embed)
        pass
    pass

@bot.event
async def on_ready():
    print(f'Successfully logged in as {bot.user}, Running Verison 0.0.8.0'.format(bot))
    await bot.change_presence(activity=activity, status=status)
    #bot.load_extension('cogs.central-music')
    print('Cogs loaded:')
    print(bot.cogs)

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

async def on_message(message):
    if message.author == bot.user:
        return

@bot.command()
async def test(ctx):
    if ctx.author.id == 222766150767869952:
        print('Test')
        await ctx.send("Success!")
    pass

@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, reason):
    print('Kicking a user...')
    await user.kick(reason=reason)
    print('Kicked!')
    await ctx.send(f"{user} have been kicked!")
    pass

@bot.command(name='ping')
async def _ping(ctx):
    print('Ping!')
    await ctx.send(f'Pong! Took **{round(bot.latency * 1000)}**ms')
    pass

@bot.command(name='ban')
@commands.has_permissions(ban_members=True)
async def _ban(ctx, user: discord.Member, reason):
    print('Banning a user...')
    await user.ban(reason=reason)
    print('Banned!')
    await ctx.send(f"{user} have been banned!")
    pass

@bot.command(name='unban')
@commands.has_permissions(ban_members=True)
async def _unban(ctx, user: discord.Member, reason):
    print('Unbanning a user...')
    await user.unban()
    print('Unbanned!')
    await ctx.send(f"{user} have been unbanned!")
    pass

@bot.command(name='adminhelp')
@commands.has_permissions(administrator=True)
async def _adminhelp(ctx):
    print('Admin help command ran...')
    embed=discord.Embed(
        title='ADMIN COMMANDS',
        typle='rich',
        colour=discord.Color(0x0000FF),
        description=admin_help
        )
    embed.set_footer(text="Developed by LIPD Producctions Inc.#1205")
    await ctx.send(embed=embed)
    pass

@bot.command()
async def help(ctx):
    print('Basic Help command ran...')
    embed=discord.Embed(
        title='HELP COMMANDS',
        type='rich',
        colour=discord.Color(0xFF0000),
        description=help_message
       )
    embed.set_footer(text="Developed by LIPD Producctions Inc.#1205")
    await ctx.send(embed=embed)
    pass

@bot.command(name='discordhelp')
async def _discordhelp(ctx):
    print('Discord Help command ran...')
    embed=discord.Embed(
        title='DISCORD HELP COMMANDS',
        type='rich',
        colour=discord.Color(0xFF0000),
        description=help_discord
       )
    embed.set_footer(text="Developed by LIPD Producctions Inc.#1205")
    await ctx.send(embed=embed)
    pass

@bot.command(name='generalhelp')
async def _revivalhelp(ctx):
    print('General Help command ran...')
    embed=discord.Embed(
        title='GENERAL/FUN COMMANDS',
        type='rich',
        colour=discord.Color(0x0000FF),
        description=help_general
       )
    embed.set_footer(text="Developed by LIPD Producctions Inc.#1205")
    await ctx.send(embed=embed)
    pass

@bot.command(name='note')
@commands.has_permissions(manage_guild=True)
async def _note(ctx, member: discord.Member, *, note = None):
    channel = ctx.bot.get_channel(os.getenv('GuildLogChannel'))
    logembed = discord.Embed(
        title=f'Note Created in {ctx.channel.mention} for {member.mention}',
        type='rich',
        colour=discord.Color.blue(),
        description=f'''
Note:
{note}
'''
        )
    logembed.set_author(name=ctx.author, icon_url=str(ctx.author.avatar_url))
    logembed.set_footer(text=f'User ID: {ctx.author.id}')
    logembed.timestamp=datetime.datetime.utcnow()
    embed = discord.Embed(
        type='rich',
        colour=discord.Color.dark_green(),
        description=f':white_check_mark: **Note created about {member}** | {note}'
        )
    if note == None:
        await ctx.send(f':x: | {ctx.author.mention}: Please specify what you want noted about {member.mention}')
    else:
        await ctx.send(embed=embed)
        await channel.send(embed=logembed)
        pass
    pass

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

bot.run(os.getenv('BotToken'))