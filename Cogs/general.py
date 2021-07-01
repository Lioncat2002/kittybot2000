import discord,random,os
from discord.ext import commands
import requests
class general(commands.Cog):
  def __init__(self,bot):
    self.bot=bot
  
  async def get(session: object, url: object) -> object:
    async with session.get(url) as response:
        return await response.text()

  @commands.command()
  async def cat(self,ctx):
    r = requests.get("https://api.thecatapi.com/v1/images/search").json()
    cat_embed = discord.Embed(title="Requested by: "+ctx.author.name)
    cat_embed.set_image(url=f"{r[0]['url']}")
    await ctx.send(embed=cat_embed)
  
  @commands.command()
  async def axolotl(self,ctx):
    f='''https://i.imgur.com/IPmxh6n.jpg
https://i.gyazo.com/b4245e8b5209f888451454a916c6f179.png
https://i.gyazo.com/ae815093c6bef3bbb5533c49a4575f8d.png
https://i.gyazo.com/09d06a5fd1dd11befaf8e5d8440c7b0c.png
https://i.gyazo.com/ab48442da9a5f4a039aba44204858f22.png
https://i.gyazo.com/83993e5c5c188c2cb19002978cbdcffc.png
https://i.gyazo.com/4308d952db3c7d6fc404edc3e0dda89d.png
https://i.redd.it/2840bjinjks61.jpg
https://i.redd.it/t34yap0hssr61.jpg
https://i.redd.it/zv47onr83gr61.jpg
https://media.discordapp.net/attachments/831162540910182410/831162901679046656/image0.jpg
https://media.discordapp.net/attachments/831162540910182410/831163074315681822/image0.jpg
https://media.discordapp.net/attachments/831162540910182410/831163074655289374/image1.jpg
https://i.redd.it/uxxg0wnirqs61.jpg
https://i.redd.it/de7ljawmrbr61.jpg
https://i.redd.it/2k86cvdn0os61.jpg
https://i.redd.it/qyrgumbgins61.jpg
https://i.redd.it/k9tn8yb4nis61.jpg
https://i.redd.it/p6q3i9v16ys61.png
https://i.redd.it/ituf7l0ruts61.jpg
https://i.redd.it/jku5co590zs61.jpg
https://i.redd.it/f5o9vho2v5t61.jpg
https://i.redd.it/8il7t0s99mp61.jpg
https://i.redd.it/t11640tym5t61.jpg
https://i.redd.it/bt721j9fh6t61.jpg
https://i.redd.it/sdxkus5gh6t61.jpg
https://i.redd.it/7cu073c5b0t61.jpg
https://i.redd.it/gh51nh2sybt61.jpg
https://i.redd.it/0yuly1l1zbt61.jpg
https://i.redd.it/htzxnvscuft61.jpg
https://i.redd.it/mlwzklv3rzr61.jpg
https://i.redd.it/jasffkzb1st61.jpg
https://i.redd.it/wtguf5dc0ft61.jpg
https://i.redd.it/dl7yvb2cpvt61.jpg
https://i.redd.it/uxonz051fdt61.jpg
https://media.discordapp.net/attachments/808700312881070120/834665883972272128/image0.jpg
https://media.discordapp.net/attachments/808700312881070120/834665996957777940/image0.jpg
https://i.redd.it/gdu8jqv3xnv61.jpg
https://i.redd.it/gfjqypdzbxu61.jpg
https://i.redd.it/upljcqdzbxu61.jpg
https://i.redd.it/crwawpdzbxu61.jpg
https://i.redd.it/ulyh1qdzbxu61.jpg
https://i.redd.it/biaquhx5m6v61.jpg
https://i.redd.it/ttrmh1hcdeu61.jpg
https://i.redd.it/hxtzr33gryu61.jpg
https://i.redd.it/arsq043gryu61.jpg
https://i.redd.it/uu9t8lnkg1v61.jpg
https://i.redd.it/gkmddm3k7jv61.jpg
https://i.redd.it/tlvmrvek7jv61.jpg
https://media.discordapp.net/attachments/830856529607000086/836880613545607188/eWMYp20SXOXHcnjFfxg_4LXA-Rcn54dXfG8tM4jp2p8.png
https://i.redd.it/gem2izs5i8v61.jpg
https://i.redd.it/ohzs77l3bju61.jpg
https://i.redd.it/pjxedpxl4rv61.jpg
https://i.redd.it/vta79pxl4rv61.jpg
https://i.redd.it/eagv9qxl4rv61.jpg
https://i.redd.it/67573puf1dv61.jpg
https://i.redd.it/uu9t8lnkg1v61.jpg
https://i.redd.it/wsb10qph0wu61.jpg
https://i.redd.it/81mz90m2sxu61.jpg
https://i.redd.it/1d43b1m2sxu61.jpg
https://i.redd.it/7boqoap7xcv61.jpg
https://i.redd.it/cjwtsis7xcv61.jpg
https://i.redd.it/3ur3hgjjyqv61.jpg
https://i.redd.it/qt7534167mv61.jpg
https://i.redd.it/ifcdx5d1zfu61.jpg'''
    r=f.split()
    rand=random.randint(0,len(r)-1)
    url=r[rand]
    embed=discord.Embed(title="Axolotls",description=f"Requested by {ctx.author.name}")
    embed.set_image(url=url)
    await ctx.send(embed=embed)
  
  @commands.command()
  async def meme(self,ctx):
    r = requests.get("https://meme-api.herokuapp.com/gimme").json()
    embed = discord.Embed(title="Requested by: "+ctx.author.name)
    while( r['nsfw']):
        r = requests.get("https://meme-api.herokuapp.com/gimme").json()

    embed.set_image(url=f"{r['url']}")
    await ctx.send(embed=embed)
  
  
  @commands.command()
  @commands.is_nsfw()
  async def urban(self,ctx,args):
    url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
    my_secret = os.environ['urbanapi']
    try:
      querystring = {"term":args}

      headers = {
    'x-rapidapi-key': my_secret,
    'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com"
    }
    
      response = requests.request("GET", url, headers=headers, params=querystring)
      d=response.json()
    
      embed=discord.Embed(title='Urban Dictonary ',description='Search the urban dictonary')
    
      if len(d['list'][0]['definition'])<1024:
      
        embed.add_field(name="Definition",value=d['list'][0]['definition'],inline=False)
    
      else:
        embed.add_field(name="Definition",value=d['list'][0]['permalink'],inline=False)
   
      if d['list'][0]['example']:
        embed.add_field(name="Example",value=d['list'][0]['example'],inline=False)
   
      await ctx.send(embed=embed)
    except:
      print("Error")
  @urban.error
  async def urbanerror(self,ctx,error):
    embed=discord.Embed(title="Error!",description="You can use this command in a nsfw channel only!",colour=discord.Colour.red())
    await ctx.send(embed=embed)



def setup(bot):
  bot.add_cog(general(bot))