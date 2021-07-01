import discord
from discord.ext import commands

class moderation(commands.Cog):
  def __init__(self,bot):
    self.bot=bot
  
  
  @commands.command()
  @commands.has_permissions(kick_members=True)
  async def kick(self,ctx,member:discord.Member,reason=None):
    await member.kick(reason=reason)
  @kick.error
  async def kick_error(self,ctx,error):
    if isinstance(error,commands.MissingPermissions):
      await ctx.send("Error! kick member permission needed")

  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def ban(self,ctx,member:discord.Member,reason=None):
    await member.kick(reason=reason)
  @ban.error
  async def ban_error(self,ctx,error):
    if isinstance(error,commands.MissingPermissions):
      await ctx.send("Error! ban member permission needed")

def setup(bot):
  bot.add_cog(moderation(bot))