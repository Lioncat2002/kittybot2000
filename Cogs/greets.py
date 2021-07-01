import discord
from discord.ext import commands

class greets(commands.Cog):
  def __init__(self,bot):
    self.bot=bot
  
  @commands.Cog.listener()
  async def on_ready(self):
    print(f"Bot online")
  
  #when bot joins a new server
  @commands.Cog.listener()
  async def on_guild_join(self,guild):
    embed=discord.Embed(title="Hello there!",description="I am your new all in one music bot :)")
    embed.add_field(name="prefix:",value="ktb>",inline=False)
    embed.add_field(name="Help Command:",value="ktb>help",inline=False)
    embed.add_field(name="Made by:",value="KittyCat",inline=False)
    embed.add_field(name="Special Thanks to:",value="You can get a chance to get your name written here if you buy kittybot premium (currently unavailable  :p)",inline=False)
    await guild.system_channel.send(embed=embed)
  
  #when a new member joins
  @commands.Cog.listener()
  async def on_member_join(self,member):  #If a member joins
    
    guild = member.guild
    print(f"member joined at {guild.name}")
    try:
      if guild.system_channel is not None:
        embed = discord.Embed(title="New member!",
                              description=f"👋 Everyone welcome **{member.name}** to **{guild.name} discord server**",
                              color=discord.Colour.green())
        embed.set_thumbnail(url=member.avatar_url)

        await guild.system_channel.send(embed=embed)
    except:
      print("Error!")
    
  
  @commands.Cog.listener()
  async def on_member_remove(self,member):  #If a member leaves
    
    guild = member.guild
    print(f"member left from {guild.name}")
    try:
      if guild.system_channel is not None:
        embed = discord.Embed(title="Oh no!",
                              description=f"**{member.name}** left **{guild.name}**😢 we will miss you..",
                              color=discord.Colour.green())
        embed.set_thumbnail(url=member.avatar_url)

        await guild.system_channel.send(embed=embed)
    except:
      print("Error!")
  
  @commands.Cog.listener()
  async def on_message_delete(self,message):
    if message.author.bot:
      return
  
    print(f"Someone deleted a message at {message.guild.name}")
    try:
      if message.mentions:
        embed=discord.Embed(title="Ghost ping detected!!",
                        description=message.author.mention,
                        color=discord.Colour.red())
        val=[i.mention for i in message.mentions]              
        embed.add_field(name="Pinged User:",value='\n'.join(x for x in val))
        await message.channel.send(embed=embed)
    except:
      print("Error")

  @commands.command()
  async def info(self,ctx):
    embed=discord.Embed(title="Hello",description="I am Kittybot",color=discord.Colour.green())
    
    embed.add_field(name="Server count",value=f" {len(list(self.bot.guilds))}",inline=True)
    embed.add_field(name="Made by",value="`Kittycat#2002`")
    embed.add_field(name="Nexus",value="[invite me](https://dsc.gg/kittybot) . [Vote me](https://top.gg/bot/839838901274935306/vote/)",inline=False)
    await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(greets(bot))

