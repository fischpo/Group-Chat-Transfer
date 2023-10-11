import os
import discord
from discord.ext import commands
from discord.utils import get
from reader import mssgread
try:
    TOKEN = ""
    GUILD = ""
    intents = discord.Intents().all()
    bot = commands.Bot(command_prefix=".",intents=intents)
    @bot.command(name='transferchat')
    async def transfere(ctx):
        await ctx.channel.purge(limit=1)

        msggp=mssgread()
        with open("reply.list","+r") as fil:
            idlist=eval(fil.read())
        pfpuser={"defaultimage":"https://i.imgur.com/LYN3cJD.png"}
        pltmp=1
        if list(idlist):
            lastentry=list(idlist)[-1]
        else:
            lastentry=""
            pltmp=0
        for ms in msggp:
          if ms==lastentry:
              pltmp=0
              continue
          if pltmp==1:
              continue
          embes= discord.Embed(title=msggp[ms]['sender'], description=msggp[ms]['mssgcontent'])
          try:
               embes.set_thumbnail(url=pfpuser[msggp[ms]['sender']])
          except:
               embes.set_thumbnail(url=pfpuser["defaultimage"])
          if msggp[ms]['attachment']:
              trigge=1
              locattach=os.path.basename(msggp[ms]['attachment'])
              lilocatch=os.path.splitext(locattach)
              file = discord.File(msggp[ms]['attachment'],filename=locattach)
              if lilocatch[1] in ['.jpg','.jpeg','.png','.gif','.webp']:
                  trigge=0
                  embes.set_image(url=f'attachment://{lilocatch[0]}{lilocatch[1]}')
              if msggp[ms]['replyto']:
                  try:
                      replid=idlist[msggp[ms]['replyto']]
                  except KeyError:
                      replid=""
                  if replid:
                      replymssg = await ctx.channel.fetch_message(replid)
                      if trigge:
                          await replymssg.reply(embed=embes)
                          sentmsg=await ctx.channel.send(file=file)
                          if msggp[ms]['embed']:
                              await ctx.channel.send(msggp[ms]['embed'])
                      else:
                          sentmsg=await replymssg.reply(embed=embes,file=file)
                          if msggp[ms]['embed']:
                              await ctx.channel.send(msggp[ms]['embed'])
                  else:
                    if trigge:
                          await ctx.channel.send(embed=embes)
                          sentmsg=await ctx.channel.send(file=file)
                          if msggp[ms]['embed']:
                              await ctx.channel.send(msggp[ms]['embed'])
                    else:
                        sentmsg=await ctx.channel.send(embed=embes,file=file)
                        if msggp[ms]['embed']:
                              await ctx.channel.send(msggp[ms]['embed'])
              else:
                  if trigge:
                          await ctx.channel.send(embed=embes)
                          sentmsg=await ctx.channel.send(file=file)
                          if msggp[ms]['embed']:
                              await ctx.channel.send(msggp[ms]['embed'])
                  else:
                      sentmsg=await ctx.channel.send(embed=embes,file=file)
                      if msggp[ms]['embed']:
                              await ctx.channel.send(msggp[ms]['embed'])
          else:
              if msggp[ms]['replyto']:
                  try:
                      replid=idlist[msggp[ms]['replyto']]
                  except KeyError:
                      replid=""
                  if replid:
                      replymssg = await ctx.channel.fetch_message(replid)
                      sentmsg=await replymssg.reply(embed=embes)
                      if msggp[ms]['embed']:
                              await ctx.channel.send(msggp[ms]['embed'])
                  else:
                      sentmsg=await ctx.channel.send(embed=embes)
                      if msggp[ms]['embed']:
                              await ctx.channel.send(msggp[ms]['embed'])
              else:
                  sentmsg=await ctx.channel.send(embed=embes)
                  if msggp[ms]['embed']:
                              await ctx.channel.send(msggp[ms]['embed'])
              
          idlist[ms]=sentmsg.id
          with open("reply.list","w") as fil:
              fil.write(str(idlist))
          
          if msggp[ms]['reacts']:
              reactn=msggp[ms]['reacts']
              if len(reactn)==3:
                    reac=f"<{reactn[2]}:{reactn[1]}>"
                  
              else:
                  reac=reactn[1]
              try:
                  await sentmsg.add_reaction(reac)
              except Exception as wies:
                      if 'Command raised an exception: HTTPException: 400 Bad Request (error code: 10014): Unknown Emoji'==str(wies):
                          emoj="👍"
                          await sentmsg.add_reaction(emoj)
    bot.run(TOKEN)
except Exception as excep:
     print("Error",excep)
  
