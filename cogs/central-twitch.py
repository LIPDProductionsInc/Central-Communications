import discord
import twitch
import datetime

from discord.ext import commands

helix=twitch.Helix(client_id='ugzkblbct4drwknb5zq6dmoiizawyt', client_secret='f5vknnwcpon55k7kbd5sua8cad13cx')

class TwitchCog(commands.Cog, name="Twitch Cog"):
    
    def __init__(self, bot):
        self.bot = bot
        
    async def twitch_embed(self):
        channel = ctx.bot.get_channel(731404916647657493)
        embed = discord.Embed(
            title='Twtich Embed Test',
            type='rich',
            description=f'''
This was triggered by a Twitch command!
''')
        embed.set_footer(text="Developed by LIPD Productions Inc.#1205", icon_url=str(ctx.guild.icon_url))
        embed.timestamp=datetime.datetime.utcnow()
        await channel.send(embed=embed)
    pass

def setup(bot):
    bot.add_cog(TwitchCog(bot))

def handle_message(message: twitch.chat.Message) -> None:
    if message.text.startswith('!views'):
        message.chat.send(f'@{message.user().display_name}, TrooperKallam has {message.user().view_count} views.')
    elif message.text.startswith('!test'):
        message.chat.send('Testing log embed')
        self.twitch_embed()
    elif message.text.startswith('!youtube'):
        message.chat.send('Check out Kallam\'s YouTube! https://www.youtube.com/channel/UC91A_2kuRT-zpA_kbioZgsA')
    elif message.text.startswith('!time'):
        time = datetime.datetime.utcnow() - datetime.timedelta(hours=7)
        message.chat.send(f"Kallam's current time: {time.strftime('%I:%M %p')}")


def main():
    chat = twitch.Chat(channel='#trooperkallam',
                       nickname='bot',
                       oauth='oauth:ywpx281z40urmuu8oynetvdcw3fasq',
                       helix=twitch.Helix(client_id='ugzkblbct4drwknb5zq6dmoiizawyt', client_secret='f5vknnwcpon55k7kbd5sua8cad13cx', use_cache=True))

    chat.subscribe(handle_message)


if __name__ == '__main__':
    main()