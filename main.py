import discord
from discord.ext import commands
from keep_alive import keep_alive
import os

intents = discord.Intents.default()
intents.members=True
if __name__ == "__main__":
    
    bot=commands.Bot(command_prefix=commands.when_mentioned_or('ktb>','Ktb>'),case_insensitive=True,intents=intents)
    bot.remove_command('help')

my_secret = 'ODQ0NTczMjY3MzQ4MjkxNTk2.YKUYJg.zgsIzqgx1mLj5l3dpP2b9TiFD_4'
bot.load_extension('Cogs.greets')
bot.load_extension('Cogs.general')
bot.load_extension('Cogs.moderation')
bot.load_extension('Cogs.music')
keep_alive()
bot.run(my_secret)