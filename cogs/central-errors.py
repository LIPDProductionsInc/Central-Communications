import discord
import math
import traceback
import sqlite3
import sys

from discord.ext import commands


class CommandErrorHandler(commands.Cog, name="Command Error Handler"):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """The event triggered when an error is raised while invoking a command.
        Parameters
        ------------
        ctx: commands.Context
            The context used for command invocation.
        error: commands.CommandError
            The Exception raised.
        """
        if hasattr(ctx.command, 'on_error'):
            return

        cog = ctx.cog
        if cog:
            if cog._get_overridden_method(cog.cog_command_error) is not None:
                return

        ignored = (commands.CommandNotFound, )
        error = getattr(error, 'original', error)

        if isinstance(error, ignored):
            print('Unknown command sent')
            await ctx.send(':x: | I do not know that command. `cc!help` has a list of commands that can be used.')

        if isinstance(error, commands.DisabledCommand):
            await ctx.send(f'{ctx.command} has been disabled.')
            
        if isinstance(error, commands.NotOwner):
            await ctx.send(':x: | You are not my owner!')
            
        if isinstance(error, discord.ClientException):
            await ctx.send(':x: | <@!222766150767869952> parameter missing.')
            
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(':x: | Argument needed')
            
        if isinstance(error, commands.CheckFailure):
            await ctx.send(':x: | A critical error has occured. ||Code 54||')
            
        if isinstance(error, commands.ExtensionAlreadyLoaded):
            await ctx.send(':x: | <@!222766150767869952> That cog is already loaded')
            
        if isinstance(error, commands.ExtensionNotLoaded):
            await ctx.send(':x: | <@!222766150767869952> Could not load cog. Check the terminal for more details')
            
        if isinstance(error, commands.ExtensionFailed):
            await ctx.send(':x: | <@!222766150767869952> Cog failed. Check the terminal for more details')
            
        if isinstance(error, commands.ExtensionNotFound):
            await ctx.send(':x: | <@!222766150767869952> Could not find cog. Check the spelling and try again')
            
        if isinstance(error, commands.CommandRegistrationError):
            await ctx.send(':x: | <@!222766150767869952> Command is already in service. Check the spelling and try again')
            
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send(f':x: | My perms got disabled. Please tag someone who can help! (Missing {error.missing_perms})')
        
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f':x: | You need the {error.missing_perms} permission to run this command!')
            
        if isinstance(error, commands.CommandOnCooldown):
            if ctx.command.name == 'daily':
                totalseconds = error.retry_after
                rawminutes = totalseconds / 60
                totalhours = rawminutes / 60
                hours = math.floor(totalhours)
                minutessub = hours * 60
                totalminutes = rawminutes - minutessub
                minutes = math.floor(totalminutes)
                await ctx.send(f':x: | Please wait **{hours} hours and {minutes} minutes** before claiming the daily again')
            elif ctx.command.name == 'work':
                totalseconds = error.retry_after
                minutes = totalseconds / 60
                await ctx.send(f':x: | Please wait **{round(minutes)} minutes** before working again')
            else:
                print(ctx.command)
                await ctx.send(f':x: | Please wait **{round(error.retry_after)} seconds** before using another economy command')
                pass
        
        if isinstance(error, ZeroDivisionError):
            await ctx.send(':x: | Cannot divide by zero!')
            
        if isinstance(error, AttributeError):
            await ctx.send(f':x: | AttributeError: {error}')
            
        if isinstance(error, NameError):
            await ctx.send(f':x: | NameError: {error}')
        
        if isinstance(error, ValueError):
            await ctx.send(f':x: | Invalid amount of K-Bucks given')
        
        if isinstance(error, SyntaxError):
            await ctx.send(f':x: | SyntaxError: {error}')
            
        if isinstance(error, KeyError):
            await ctx.send(f':x: | KeyError: {error} is not found')
            
        if isinstance(error, TypeError):
            await ctx.send(f':x: | TypeError: {error}')
            
        if isinstance(error, discord.HTTPException):
            await ctx.send(f':x: | HTTPException: {error.status} (error code: {error.code}): {error.text}')
             
        if isinstance(error, sqlite3.IntegrityError):
            await ctx.send(f':x: | You are already registered. If this is in error, please open a ticket')
            
        if isinstance(error, sqlite3.OperationalError):
            await ctx.send(f':x: | OperationalError: {error}')

        elif isinstance(error, commands.NoPrivateMessage):
            try:
                await ctx.author.send(f'{ctx.command} can not be used in Private Messages.')
            except discord.HTTPException:
                pass

        elif isinstance(error, commands.BadArgument):
            if ctx.command.qualified_name == 'tag list':
                await ctx.send('I could not find that member. Please try again.')
            elif ctx.command.qualified_name == 'note':
                await ctx.send(f':x: | You need to mention someone!')

        else:
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

    @commands.command(name='repeat', aliases=['mimic', 'copy'])
    async def do_repeat(self, ctx, *, inp: str):
        """A simple command which repeats your input!
        Parameters
        ------------
        inp: str
            The input you wish to repeat.
        """
        await ctx.send(inp)

    @do_repeat.error
    async def do_repeat_handler(self, ctx, error):
        """A local Error Handler for our command do_repeat.
        This will only listen for errors in do_repeat.
        The global on_command_error will still be invoked after.
        """

        if isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == 'inp':
                await ctx.send("You forgot to give me input to repeat!")


def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))
