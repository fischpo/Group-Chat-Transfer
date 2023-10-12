import os
import discord
from discord.ext import commands
from discord.utils import get
from reader import mssgread
try:
    TOKEN = ""
    intents = discord.Intents().all()
    bot = commands.Bot(command_prefix=".",intents=intents)
    @bot.command(name='transferchat')
    async def transfere(ctx):
        await ctx.channel.purge(limit=1)

        msggp=mssgread()
        try:
          with open("reply.list","+r") as fil:
            idlist=eval(fil.read())
        except:
          with open("reply.list","w") as fil:
            fil.write("{}")
            idlist={}
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
                      elif msggp[ms]['attachment']:
                            await ctx.channel.send(msggp[ms]['attachment'])
          else:
                  sentmsg=await ctx.channel.send(embed=embes)
                  if msggp[ms]['embed']:
                              await ctx.channel.send(msggp[ms]['embed'])
                  elif msggp[ms]['attachment']:
                            await ctx.channel.send(msggp[ms]['attachment'])
              
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
  
