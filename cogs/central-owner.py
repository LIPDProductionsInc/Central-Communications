import discord
import asyncio
import datetime

from discord.ext import commands

class OwnerCog(commands.Cog, name="Owner Commands"):

    def __init__(self, bot):
        self.bot = bot
    
    # Hidden means it won't show up on the default help.
    @commands.command(name='load', hidden=True)
    @commands.is_owner()
    async def _load(self, ctx, *, cog: str):
        await ctx.send('**`Loading cog...`**')
        """Command which Loads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.load_extension(f'cogs.central-{cog}')
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.command(name='unload', hidden=True)
    @commands.is_owner()
    async def _unload(self, ctx, *, cog: str):
        await ctx.send('**`Unloading cog...`**')
        """Command which Unloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(f'cogs.central-{cog}')
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.command(name='reload', hidden=True)
    @commands.is_owner()
    async def _reload(self, ctx, *, cog: str):
        """Command which Reloads a Module.
        Remember to use dot path. e.g: cogs.owner"""
        print('Reloading a cog...')
        try:
            await ctx.send('**`Unloading cog...`**')
            self.bot.unload_extension(f'cogs.central-{cog}')
            await asyncio.sleep(2)
            self.bot.load_extension(f'cogs.central-{cog}')
            await ctx.send('**`Loading cog...`**')
            await asyncio.sleep(1)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')
            print('Sucess!')
            
    @commands.command(name='embed', hidden=True)
    @commands.is_owner()
    async def _embed(self, ctx):
        embed = discord.Embed(
            title='**REACT WITH**',
            type='rich',
            colour = discord.Color.dark_blue(),
            description = '''
:video_camera: to get the <@&731397963259052133> role
:microphone: to get the <@&732118149285150800> role
:tada: to get the <@&732868630710190140> role
:video_game: to get the <@&786174523405107200> role
:movie_camera: to get the <@&802013687333781534> role
:grey_question: to get the <@&809068173868400720> role
:question: to get the <@&948495979940823070> role
            ''')
        await ctx.send(embed=embed)
        pass
        
    @commands.command(name='revival')
    @commands.has_any_role(731391948102959104, 731392197437685772, 731395356419424297)
    async def _revival(self, ctx, member: discord.Member = None):
        if ctx.channel.category_id == 958548040724123710:
            embed = discord.Embed(
                type='rich',
                colour=discord.Color.dark_blue(),
                description='''
**Hey!** We think you have our server mistaken. We do not provide support, help, or advice for the Revival FiveM server. You need to open a <#774375679130992700> in the [Revival Discord](https://discord.gg/revivalrp). If you are unable to access the Discord server, you must try the [fourms](http://revivalrp.com). We can't help you otherwise. Sorry :(
                ''')
            embed.set_footer(text="Developed by LIPD Productions Inc.#1205", icon_url=str(ctx.guild.icon_url))
            embed.timestamp=datetime.datetime.utcnow()
            if member == None:
                await ctx.send(embed=embed)
            else:
                await ctx.send(member.mention,embed=embed)
            pass
        pass
    pass
    
    @commands.command(name='howto', aliases=['how-to'])
    @commands.has_any_role(731391948102959104, 731392197437685772, 731395356419424297)
    async def _howto(self, ctx, type = None, page: int = None, member: discord.Member = None):
        if ctx.channel.category_id == 958548040724123710:
            await ctx.message.delete()
            if type == None:
                await ctx.send(':x: | No guide type given')
            elif type == 'graphics':
                if page == None:
                    await ctx.send(':x: | Please give me a page number')
                elif page == 1:
                    embed = discord.Embed(
                        title='GRAPHICS GUIDE PAGE 1',
                        type='rich',
                        colour=discord.Color.dark_blue(),
                        description=f"To get started with getting Kallam's graphics, please provide proof of purchase for [QuantV](https://www.patreon.com/QuantV) and [NVE](https://www.patreon.com/razedmods)")
                    embed.set_footer(text="Developed by LIPD Productions Inc.#1205", icon_url=str(ctx.guild.icon_url))
                    embed.timestamp=datetime.datetime.utcnow()
                elif page == 2:
                    embed = discord.Embed(
                        title='GRAPHICS GUIDE PAGE 2',
                        type='rich',
                        colour=discord.Color.dark_blue(),
                        description=f"Next, you will need to get the [custom reshade](https://www.patreon.com/Tiessen) made by <@413601769512501250>. To have it exactly like Kallam's, use the Revival preset.")
                    embed.set_footer(text="Developed by LIPD Productions Inc.#1205", icon_url=str(ctx.guild.icon_url))
                    embed.timestamp=datetime.datetime.utcnow()
                elif page == 3:
                    embed = discord.Embed(
                        title='GRAPHICS GUIDE PAGE 3',
                        type='rich',
                        colour=discord.Color.dark_blue(),
                        description=f"Finally, you put the reshade preset in your main GTA folder. Once you have installed reshade and all the asset packs it prompts you to, you just open reshade with the home button and select the reshade preset in the top bar where it says `reshadepreset.ini`")
                    embed.set_footer(text="Developed by LIPD Productions Inc.#1205", icon_url=str(ctx.guild.icon_url))
                    embed.timestamp=datetime.datetime.utcnow()
                else:
                    await ctx.send(':x: | Invalid page number. Select from pages 1-x')
                if member == None:
                    await ctx.send(embed=embed)
                else:
                    await ctx.send(member.mention,embed=embed)
            else:
                await ctx.send(':x: | Invalid guide type')

def setup(bot):
    bot.add_cog(OwnerCog(bot))