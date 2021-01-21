import discord
import platform
import os
import keep_alive
import requests

bot = discord.Client()

from .discord_botconfig import botconfig

@bot.event
async def on_ready():
    keep_alive.keep_alive()
    print('\nWelcome! Vision ver. ' + botconfig['version'] + '\n(©) 2020-2021 Tinelix. All rights reserved.')
    print('\nConnected - ' + bot.user.name + '#' + bot.user.discriminator + '\nLatency: ' + str(round(bot.latency * 1000, 2)) + ' ms | Guilds: ' + str(len(bot.guilds)))
    print('----------------------------------------------------------------------')
    boticord_token = os.environ['BOTICORDTOKEN']
    bots_ds_token = os.environ['BOTSDST']
    game = discord.Game(str("Something went wrong..."), type=discord.ActivityType.watching)
    await bot.change_presence(status=discord.Status.dnd, activity=game)
    res = requests.post("https://api.server-discord.com/v2/bots/785383439196487720/stats", headers={'Content-Type':'application/json',
               'Authorization': 'SDC {0}'.format(bots_ds_token)}, json={'shards': 0, 'servers': len(bot.guilds)}) 
    print(res.content.decode('utf-8'))
    res2 = requests.post("https://boticord.top/api/stats", headers={'Content-Type':'application/json',
               'Authorization': '{}'.format(boticord_token)}, json={'shards': 0, 'servers': len(bot.guilds), 'users': len(bot.users)})
    print(res2.content.decode('utf-8'))

@bot.event
async def on_message(message):
  if message.content.startswith(botconfig['prefix']):
    text = 'В работе бота произошли технические неполадки, мы разберемся с ними. А чтобы не скучать, заходите на наш [саппорт-сервер](https://discord.gg/HAt6K2QuJU) или воспользуйтесь [тестируемой версии бота](https://discord.com/oauth2/authorize?client_id=769515555765616690&permissions=8&scope=bot).\n\n**Приносим свои извинения за доставленные неудобства!**'
    information = discord.Embed(title="Важная информация!", description=text, color=botconfig['accent2'])
    await message.channel.send(embed=information)
    
bot.run(botconfig['token'])