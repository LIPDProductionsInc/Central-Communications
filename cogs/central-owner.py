from turtle import color
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

    @commands.command(name='edit')
    @commands.is_owner()
    async def _edit(self, ctx, id):
        message = await ctx.channel.fetch_message(id)
        embed = message.embeds[0].description = '''
:video_camera: to get the <@&731397963259052133> role
:microphone: to get the <@&732118149285150800> role
:tada: to get the <@&732868630710190140> role
:video_game: to get the <@&786174523405107200> role
:movie_camera: to get the <@&802013687333781534> role
:grey_question: to get the <@&809068173868400720> role
:question: to get the <@&948495979940823070> role
:robot: to get the <@&1015680899511242832> role
            '''
        await message.edit(embed=embed)
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

    @commands.command(name='rules')
    @commands.is_owner()
    async def _rules(self, ctx, github = False):
        if github == False:
            embed = discord.Embed(
                title="**Welcome to Kallam's Troop**",
                type='rich',
                colour = discord.Colour.dark_blue(),
                description='''
**RULES:**
`1.`Discord Terms of Service https://discord.com/terms and the Discord Community Guidelines https://discord.com/guidelines MUST be followed at all times.
`2.` Please be respectful to everyone here. **No hateful messages to members**
`3.` Leaking personal information of anyone is **not** allowed
`4.` Spamming and/or mic-spamming is **not** allowed
`5.` NSFW or inappropriate content is **not** allowed. This can be pornographic, gore, highly sensitive material, etc.
`6.` Advertising your material (Discord server/Twitch Channel/RP Community) is **not** allowed.  
`7.` Do **not** post malicious links, files, or anything of that sort
`8.` Sharing discord direct messages (DMS) in order to provoke them and make them look bad is **not** tolerated
`9.` Racism/Homophobia is **not** tolerated in this discord
`10.` This is an English speaking discord
`11.` Targeting someone in order to provoke by any means is forbidden
`12.` Impersonation of another person or bot is forbidden

**Common Sense is required in this Discord server. If you are questioning whether or not you should post something, it's better to not to or open a <#944466196663775262>**

**At the end of the day mods have final say on decisions made in the discord**
            **Rules are subject to change at any point**
**By remaining in the discord, you are acknowledging and agreeing to these rules** 
            ''')
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title="**Central Communications GitHub Repository**",
                type='rich',
                url='http://github.com/LIPDProductionsInc/Central-Communications',
                colour = discord.Colour.dark_blue(),
                description='''
**GITHUB RULES:**
`1.` The [Discord Developer Terms of Service](https://discord.com/developers/docs/policies-and-agreements/terms-of-service), [Discord Developer Policy](https://discord.com/developers/docs/policies-and-agreements/developer-policy), and the [GitHub Site Policies](https://docs.github.com/en/site-policy/github-terms) **MUST** be followed at **ALL** times
`2.` API Keys submitted in pull requests will **NOT** be used. If you have a premium key and would like to offer it, open a [support ticket in the Troop Discord](https://ptb.discord.com/channels/731391566945714226/944466196663775262).
`3.` [LIPD Productions Inc.](http://github.com/LIPDProductionsInc) has the final say on what gets integrated into the bot.
`4.` Attempting to get around the Discord API is not allowed.
`5.` Any edits made to files under the DB folder in a pull request will **NOT** be pushed to the bot itself.
`6.` Pull requests that are not related to the bot will be closed.
            ''')
            await ctx.send(embed=embed)
            pass
        pass

def setup(bot):
    bot.add_cog(OwnerCog(bot))