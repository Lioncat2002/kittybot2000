import discord
import youtube_dl
from discord.ext import commands
class music(commands.Cog):
  def __init__(self,bot):
    self.bot=bot
  
  

  def issupported(url):
    extractors = youtube_dl.extractor.gen_extractors()
    for e in extractors:
        if e.suitable(url) and e.IE_NAME != 'generic':
            return True
    return False

  @commands.command()
  async def play(self,ctx,url):
    YTDL_OPTS = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
  }
    
    
    voice_channel=ctx.author.voice.channel
    if voice_channel==None:
      embed=discord.Embed(title="Error!",description="Please join a voice channel to use this command!",color=discord.Colour.red())
      await ctx.send(embed=embed)
    
    else:
      print("Connecting")
      vc=await voice_channel.connect()
      print("Connected!")
      ytdl = youtube_dl.YoutubeDL(YTDL_OPTS)
      info = ytdl.extract_info(url, download=False)
      asrc = discord.FFmpegOpusAudio(info['formats'][0]['url'], before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5")
      vc.play(asrc)

  @commands.command()
  async def leave(self,ctx):
    print("leaving")
    if (ctx.author.voice):
      for vc in self.bot.voice_clients:
            if vc.guild == ctx.guild:
                await vc.disconnect()
                print(f"Someone stopped playing music at {ctx.guild.name}")
    else:
            await ctx.send("Please connect to a voice channel first!")

      
    

def setup(bot):
  bot.add_cog(music(bot))