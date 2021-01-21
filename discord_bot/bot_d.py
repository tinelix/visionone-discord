import discord
import platform
import os
import sqlite3
import datetime
import requests
import time
import sys
import traceback
import json
import numexpr
import gc
import keep_alive
import cpuinfo
import psutil

keep_alive.keep_alive()

from requests.auth import HTTPBasicAuth
from threading import Timer
from sqlite3 import Error
from discord.ext import commands
from .discord_botconfig import botconfig

from unsplash.api import Api as unsplash_api
from unsplash.auth import Auth
from .d_commands.help import help_cmd
from .d_commands.state import state_cmd
from .d_commands.eval import eval_cmd
from .d_commands.db import db_cmd
from .d_commands.settings import settings_cmd
from .d_commands.photo import photo_cmd
from .d_commands.calc import calc_cmd
from .d_commands.feedback import feedback_cmd
from .d_commands.weather import weather_cmd
from .d_commands.crystball import crystball_cmd
from .d_commands.post import post_cmd
from .d_commands.guilds import guilds_cmd
from .d_commands.info import info_cmd
from .d_commands.poll import poll_cmd
from .d_commands.reputation import rep_cmd
from .d_events.new_level import message_to_xp
import discord_bot.d_commands.set as settings
import discord_bot.d_commands.profile as profile
import discord_bot.d_events.cooldown as cooldown
import discord_bot.d_events.logging as logging
import discord_bot.d_author_cmds.tnews as tnews
import discord_bot.d_commands.blacklist as blacklist
import discord_bot.d_events.new_member as autorole
import discord_bot.d_commands.codec as codec
import discord_bot.mem
import praw

reddit = praw.Reddit(client_id=os.environ['REDDITID'],
                     client_secret=os.environ['REDDITST'], 
                     user_agent='Vision Bot',
                     username='dmitcomputers')

import discord_bot.d_languages.binary as binary
import discord_bot.d_languages.en_US as en_US
import discord_bot.d_languages.ru_RU as ru_RU

intents = discord.Intents.all()

auth = Auth(botconfig['unsplash_ak'], botconfig['unsplash_sk'], botconfig['unsplash_ur'], code='')
unsplash = unsplash_api(auth)

bot = discord.Client(intents=intents)
epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

def removeduplicate(it):
       seen = set()
       for x in it:
           t = tuple(x.items())
           if t not in seen:
               yield x
               seen.add(t)

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
    except Error as e:
        print(f"SQLite Database | The error '{e}' occurred")

    return connection

connection = create_connection(os.path.join(os.path.dirname(__file__), 'vision_discord.sqlite'))
cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users(
        userid TEXT NOT NULL PRIMARY KEY,
        botlanguage TEXT NOT NULL,
        messages INT NOT NULL,
        timezone INT NOT NULL,
        dbregdate INT NOT NULL,
        messagecount TEXT NOT NULL,
        lastmsgtime INT NOT NULL,
        reputation INT NOT NULL,
        scores INT NOT NULL,
        level INT NOT NULL);
    """)
cursor.execute("""CREATE TABLE IF NOT EXISTS guilds(
        guildid TEXT NOT NULL PRIMARY KEY,
        region TEXT NOT NULL,
        messages INT NOT NULL,
        dbregdate INT NOT NULL,
        messagecount TEXT NOT NULL,
        embedmsgcolor TEXT NOT NULL,
        msgprefix TEXT NOT NULL,
        botlanguage TEXT NOT NULL,
        welcomech INT NOT NULL,
        welcometext TEXT,
        goodbyech INT NOT NULL,
        goodbyetext TEXT NOT NULL,
        levelsystem TEXT NOT NULL);
    """)
cursor.execute("""CREATE TABLE IF NOT EXISTS blacklist_guilds(
        guildid TEXT PRIMARY KEY);
    """)
cursor.execute("""CREATE TABLE IF NOT EXISTS bot_data(
        number INT NOT NULL PRIMARY KEY,
        unsplash_count INT NOT NULL);
    """)
cursor.execute("""CREATE TABLE IF NOT EXISTS polls(
        msgid INT NOT NULL PRIMARY KEY,
        userid INT NOT NULL,
        enddate INT NOT NULL);
    """)
cursor.execute("""CREATE TABLE IF NOT EXISTS reputations(
        msgid INT NOT NULL PRIMARY KEY,
        userid INT NOT NULL,
        repid INT NOT NULL,
        fan TEXT NOT NULL,
        hater TEXT NOT NULL);
    """)
connection.commit()


@bot.event
async def on_ready():
    print('\nWelcome! Vision ver. ' + botconfig['version'] + '\n(©) 2020-2021 Tinelix. All rights reserved.')
    print('\nConnected - ' + bot.user.name + '#' + bot.user.discriminator + '\nLatency: ' + str(round(bot.latency * 1000, 2)) + ' ms | Guilds: ' + str(len(bot.guilds)))
    print('----------------------------------------------------------------------')
    boticord_token = os.environ['BOTICORDTOKEN']
    bots_ds_token = os.environ['BOTSDST']
    game = discord.Game(str(len(bot.guilds)) + " guilds | " + botconfig['prefix'] + "help", type=discord.ActivityType.watching)
    await bot.change_presence(status=discord.Status.dnd, activity=game)
    res = requests.post("https://api.server-discord.com/v2/bots/785383439196487720/stats", headers={'Content-Type':'application/json',
               'Authorization': 'SDC {0}'.format(bots_ds_token)}, json={'shards': 0, 'servers': len(bot.guilds)}) 
    print(res.content.decode('utf-8'))
    res2 = requests.post("https://boticord.top/api/stats", headers={'Content-Type':'application/json',
               'Authorization': '{}'.format(boticord_token)}, json={'shards': 0, 'servers': len(bot.guilds), 'users': len(bot.users)})
    print(res2.content.decode('utf-8'))

@bot.event
async def on_guild_join(guild):
    boticord_token = os.environ['BOTICORDTOKEN']
    bots_ds_token = os.environ['BOTSDST']
    res = requests.post("https://api.server-discord.com/v2/bots/785383439196487720/stats", headers={'Content-Type':'application/json',
               'Authorization': 'SDC {0}'.format(bots_ds_token)}, json={'shards': 0, 'servers': len(bot.guilds)}) 
    print(res.content.decode('utf-8'))
    res2 = requests.post("https://boticord.top/api/stats", headers={'Content-Type':'application/json',
               'Authorization': '{}'.format(boticord_token)}, json={'shards': 0, 'servers': len(bot.guilds), 'users': len(bot.users)})
    game = discord.Game(str(len(bot.guilds)) + " guilds | " + botconfig['prefix'] + "help", type=discord.ActivityType.watching)
    await bot.change_presence(status=discord.Status.dnd, activity=game)
    guild_s = [(guild.id, str(guild.region), 0, unix_time_millis(datetime.datetime.now()), "Enabled", 'Standart', '=', 'English', 0, '', 0, '', "Disabled")]
    cursor.executemany("INSERT OR REPLACE INTO guilds VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", guild_s)
    # print(guild)
    connection.commit()
    await logging.joining_logger(bot, discord, guild, connection, cursor, unix_time_millis, botconfig)

@bot.event
async def on_guild_remove(guild):
    requests.post("https://api.server-discord.com/v2/bots/785383439196487720/stats", params={'id': 785383439196487720}, headers={'Authorization': os.environ['BOTSDST']}, data={'shards': 0, 'servers': len(bot.guilds)})
    game = discord.Game(str(len(bot.guilds)) + " guilds | " + botconfig['prefix'] + "help", type=discord.ActivityType.watching)
    await bot.change_presence(status=discord.Status.dnd, activity=game)
    await logging.leaving_logger(bot, discord, guild, connection, cursor, unix_time_millis, botconfig)
  
@bot.event
async def on_member_join(member):
  await autorole.autorole(bot, discord, member, botconfig, cursor, connection)
  await autorole.new_member(bot, discord, member, botconfig, cursor, connection)

@bot.event
async def on_member_remove(member):
  await autorole.member_left(bot, discord, member, botconfig, cursor, connection)

@bot.event
async def on_message(message):
    if message.author == bot.user or str(message.channel.type) == "private" or message.author.bot == True:
        return
    cursor.execute("SELECT * FROM users WHERE userid='" + str(message.author.id) + "';")
    one_result = (cursor.fetchone())
    # print("SQLite Database | " + str(one_result))
    cursor.execute("SELECT * FROM guilds WHERE guildid='" + str(message.guild.id) + "';")
    guild_result = (cursor.fetchone())
    # print("SQLite Database | " + str(guild_result))
    cursor.execute("SELECT * FROM users WHERE userid='" + str(message.author.id) + "';")
    cursor.execute("SELECT * FROM bot_data WHERE number='" + str(0) + "';")
    bot_data_result = (cursor.fetchone())
    try:
        lastmsgtime = one_result[6]
    except:
        lastmsgtime = 0
    bot_data = [(0, 0)]

    try:
      if guild_result[6] == None or guild_result[6] == "":
          prefix = botconfig['prefix']
      else:
          prefix = guild_result[6]
    except:
      prefix = botconfig['prefix']
    try:
        if message.content.startswith(botconfig['prefix']) or message.content.startswith(guild_result[6]):
            time_diff = ((datetime.datetime.utcnow() - epoch).total_seconds() * 1000) - one_result[6]
            if time_diff < 500:
                return await cooldown.cooldown(bot, message, one_result, guild_result, connection, cursor, unix_time_millis, ru_RU, en_US)
            await logging.messaging_logger(bot, discord, message, one_result, guild_result, connection, cursor, unix_time_millis, botconfig, bot_data_result)
        if one_result[1] == "Russian":
            localization = ru_RU.get()
        elif one_result[1] == "English":
            localization = en_US.get()
        if one_result[5] == "Enabled":
            user = [(message.author.id, one_result[1], one_result[2] + 1, one_result[3], one_result[4], "Enabled", unix_time_millis(message.created_at), one_result[7], one_result[8], one_result[9])]
            userdata_recovery = {
                "userid": message.author.id,
                "botlanguage": one_result[1],
                "messages": one_result[2] + 1,
                "timezone": one_result[3],
                "dbregdate": one_result[4],
                "messagecount": "Enabled",
                "lastmsgtime": unix_time_millis(message.created_at),
                "reputation": one_result[7]
            }
        elif one_result[5] == "Disabled": 
            user = [(message.author.id, one_result[1], one_result[2], one_result[3], one_result[4], "Disabled", unix_time_millis(message.created_at), one_result[7], one_result[8], one_result[9])]
            userdata_recovery = {
                "userid": message.author.id,
                "botlanguage": one_result[1],
                "messages": one_result[2] + 1,
                "timezone": one_result[3],
                "dbregdate": one_result[4],
                "messagecount": "Disabled",
                "lastmsgtime": unix_time_millis(message.created_at),
                "reputation": one_result[7]
            }
        else:
            user = [(message.author.id, one_result[1], one_result[2] + 1, one_result[3], one_result[4], one_result[5], unix_time_millis(message.created_at))]
            userdata_recovery = {
                "userid": message.author.id,
                "botlanguage": one_result[1],
                "messages": one_result[2] + 1,
                "timezone": one_result[3],
                "dbregdate": one_result[4],
                "messagecount": one_result[5],
                "lastmsgtime": unix_time_millis(message.created_at),
                "reputation": one_result[7]
            }
        if guild_result[4] == "Enabled":
            guild = [(message.guild.id, guild_result[1], guild_result[2] + 1, guild_result[3], "Enabled", guild_result[5], guild_result[6], guild_result[7], guild_result[8], guild_result[9], guild_result[10], guild_result[11], guild_result[12])]
            guilddata_recovery = {
                "guildid": message.guild.id,
                "region": guild_result[1],
                "messages": guild_result[2] + 1,
                "dbregdate": guild_result[3],
                "messagecount": "Enabled",
                "embedmsgcolor": guild_result[5],
                "msgprefix": guild_result[6],
                "botlanguage": guild_result[7],
                "welcomech": guild_result[8],
                "welcometext": guild_result[9],
                "goodbyech": guild_result[10],
                "goodbyetext": guild_result[11],
            },
        elif guild_result[4] == "Disabled": 
            guild = [(message.guild.id, guild_result[1], guild_result[2], guild_result[3], "Disabled", guild_result[5], guild_result[6], guild_result[7], guild_result[8], guild_result[9], guild_result[10], guild_result[11], guild_result[12])]
            guilddata_recovery = {
                "guildid": message.guild.id,
                "region": guild_result[1],
                "messages": guild_result[2] + 1,
                "dbregdate": guild_result[3],
                "messagecount": "Disabled",
                "embedmsgcolor": guild_result[5],
                "msgprefix": guild_result[6],
                "botlanguage": guild_result[7],
                "welcomech": guild_result[8],
                "welcometext": guild_result[9],
                "goodbyech": guild_result[10],
                "goodbyetext": guild_result[11],
            },
        else:
            guild = [(message.guild.id, guild_result[1], guild_result[2] + 1, guild_result[3], "Enabled", guild_result[5], guild_result[6], guild_result[7], guild_result[8], guild_result[9], guild_result[10], guild_result[11], guild_result[12])]
            guilddata_recovery = {
                "guildid": message.guild.id,
                "region": guild_result[1],
                "messages": guild_result[2] + 1,
                "dbregdate": guild_result[3],
                "messagecount": "Enabled",
                "embedmsgcolor": guild_result[5],
                "msgprefix": guild_result[6],
                "botlanguage": guild_result[7],
                "welcomech": guild_result[8],
                "welcometext": guild_result[9],
                "goodbyech": guild_result[10],
                "goodbyetext": guild_result[11],
            },
        blacklist_guilds = [(message.guild.id)]
        if bot_data_result[0] == 0:
            bot_data = [(0, bot_data_result[1])]
        else:
            bot_data = [(0, 0)]
        if guild_result[5] == "Red":
          embed_color = 0xff3333
        if guild_result[5] == "Standart":
          embed_color = botconfig['accent1']
        if guild_result[5] == "Yellow":
          embed_color = 0xffcc00
        if guild_result[5] == "Green":
          embed_color = 0x00dd1f
        if guild_result[5] == "Sky-blue":
          embed_color = 0x4f9dfe
        if guild_result[5] == "Blue":
          embed_color = 0x002277     
        if guild_result[5] == "Violet":
          embed_color = 0x7f66ef 
        if guild_result[5] == "Rose":
          embed_color = 0xff0066    
    except Exception as e:
        if one_result is None or guild_result is None or bot_data_result is None:
          print("Registration...")
          pass
        if str(message.guild.region) == "russia":
            user = [(message.author.id, "Russian", 0, 10800000, unix_time_millis(message.created_at), "Disabled", unix_time_millis(message.created_at), 0, 0, 0)]
            guild = [(message.guild.id, str(message.guild.region), 0, unix_time_millis(message.created_at), "Disabled", "Standart", "=", "Russian", 0, "", 0, "", "Disabled")]
        else:
              user = [(message.author.id, "English", 0, 10800000, unix_time_millis(message.created_at), "Disabled", unix_time_millis(message.created_at), 0, 0, 0)]
              guild = [(message.guild.id, str(message.guild.region), 0, unix_time_millis(message.created_at), "Disabled", "Standart", "=", "English", 0, "", 0, "", "Disabled")]
        print(e)
        bot_data = [(0, 0)]

    cursor.executemany("INSERT OR REPLACE INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", user)
    # print(user)
    connection.commit()
    cursor.executemany("INSERT OR REPLACE INTO guilds VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", guild)
    # print(guild)
    cursor.executemany("INSERT OR REPLACE INTO bot_data VALUES(?, ?)", bot_data)
    connection.commit()
    try:
      if guild_result[12] == "Enabled":
        await message_to_xp(bot, discord, message, botconfig, platform, os, datetime, one_result, guild_result, localization, unix_time_millis, embed_color, connection, cursor, prefix)
    except:
      pass

    timingcount = 0
    if message.content.startswith(botconfig['prefix']) or message.content.startswith(guild_result[6]):
      try:
            time_diff = (datetime.datetime.utcnow() - epoch).total_seconds() - 2
            print(time_diff)
            if time_diff >= 120:
                pass
            if message.content.startswith(botconfig['prefix'] + 'help') or message.content.startswith(guild_result[6] + 'help'):
              try:
                await help_cmd(bot, discord, message, botconfig, os, platform, datetime, one_result, localization, embed_color, guild_result)
              except:
                if str(message.guild.region) == "russia":
                  await help_cmd(bot, discord, message, botconfig, os, platform, datetime, one_result, ru_RU.get(), botconfig['accent1'], "=")
                else:
                  await help_cmd(bot, discord, message, botconfig, os, platform, datetime, one_result, en_US.get(), botconfig['accent1'], "=")
            if message.content.startswith(botconfig['prefix'] + 'state') or message.content.startswith(guild_result[6] + 'state'):
                await state_cmd(bot, discord, sqlite3, message, botconfig, os, platform, datetime, one_result, localization, embed_color, connection, cursor, cpuinfo, psutil)
            if message.content.startswith(botconfig['prefix'] + 'eval' or message.content.startswith(guild_result[6] + 'eval')):
                await eval_cmd(bot, discord, message, botconfig, os, platform, datetime, one_result, localization, en_US, guild_result, intents, embed_color)
            if message.content.startswith(botconfig['prefix'] + 'guilds' or message.content.startswith(guild_result[6] + 'guilds')):
                await guilds_cmd(bot, discord, message, botconfig, os, platform, datetime, one_result, localization, guild_result, intents, embed_color)
            if message.content.startswith(botconfig['prefix'] + 'db' or message.content.startswith(guild_result[6] + 'db')):
                await db_cmd(bot, discord, message, botconfig, os, platform, datetime, one_result, localization, connection, cursor)
            if message.content.startswith(botconfig['prefix'] + 'clock'):
                await eval_cmd(bot, discord, message, botconfig, os, platform, datetime, one_result, localization, en_US, guild_result, intents, embed_color)
            if message.content.startswith(botconfig['prefix'] + 'settings') or message.content.startswith(guild_result[6] + 'settings'):
                await settings_cmd(bot, discord, message, botconfig, os, platform, datetime, one_result, localization, unix_time_millis, embed_color, guild_result, prefix)
            if message.content.startswith(botconfig['prefix'] + 'set') or message.content.startswith(guild_result[6] + 'set'):
              args = message.content.split(" ");
              try:
                if args[1] == "-l":
                    await settings.set_bot_language(bot, discord, message, botconfig, os, platform, datetime, one_result, args, connection, cursor, unix_time_millis)
                if args[1] == "-tz":
                    await settings.set_timezone(bot, discord, message, botconfig, os, platform, datetime, one_result, args, connection, cursor, localization, unix_time_millis)
                if args[1] == "-mc":
                    await settings.switch_msgcounter(bot, discord, message, botconfig, os, platform, datetime, one_result, args, connection, cursor, localization, unix_time_millis, guild_result)
                if args[1] == "-ec":
                    await settings.set_embed_color(bot, discord, message, botconfig, os, platform, datetime, one_result, args, connection, cursor, localization, unix_time_millis, embed_color, guild_result)
                if args[1] == "-pfx":
                    await settings.set_prefix(bot, discord, message, botconfig, os, platform, datetime, one_result, args, connection, cursor, localization, unix_time_millis, embed_color, guild_result, prefix)
                if args[1] == "-lvs":
                    await settings.switch_lvlsystem(bot, discord, message, botconfig, os, platform, datetime, one_result, args, connection, cursor, localization, unix_time_millis, embed_color, guild_result, prefix)
                if args[1] == "-wl_msg":
                    await settings.set_welcome_message(bot, discord, message, botconfig, os, platform, datetime, one_result, args, connection, cursor, localization, unix_time_millis, embed_color, guild_result, prefix)
                if args[1] == "-gb_msg":
                    await settings.set_goodbye_message(bot, discord, message, botconfig, os, platform, datetime, one_result, args, connection, cursor, localization, unix_time_millis, embed_color, guild_result, prefix)
                else: return
              except Exception as e:
                print(e)
            if message.content.startswith(botconfig['prefix'] + 'profile') or message.content.startswith(guild_result[6] + 'profile'):
                args = message.content.split();
                try:
                  if args[1] == "-u":
                        await profile.get_user(bot, discord, message, botconfig, platform, os, datetime, one_result, localization, args, unix_time_millis, connection, cursor, intents, lastmsgtime, embed_color)
                  if args[1] == "-g":
                        await profile.get_guild(bot, discord, message, botconfig, platform, os, datetime, one_result, localization, args, unix_time_millis, connection, cursor, guild_result, intents, embed_color)
                  else:
                        pass
                except Exception as e: 
                    print(e)
                    await profile.get_help(bot, discord, message, botconfig, platform, os, datetime, one_result, localization, args, unix_time_millis, connection, cursor, embed_color, prefix)
            if message.content.startswith(botconfig['prefix'] + 'tnews') or message.content.startswith(guild_result[6] + 'tnews'):
                args = message.content.split();
                await tnews.get_tnews(bot, discord, message, botconfig, platform, os, datetime, one_result, localization, args, unix_time_millis, connection, cursor, embed_color)
            if message.content.startswith(botconfig['prefix'] + 'blacklist'):
                args = message.content.split(" ");
                try:
                    if args[1] == "-ag":
                        await blacklist.add_guild_to_blacklist(bot, discord, message, botconfig, platform, os, datetime, one_result, localization, args, unix_time_millis, connection, cursor)
                except Exception as e: 
                    print(e)
            if message.content.startswith(botconfig['prefix'] + 'photo') or message.content.startswith(guild_result[6] + 'photo'):
                await photo_cmd(bot, discord, message, botconfig, os, platform, datetime, one_result, localization, unix_time_millis, unsplash, time_diff, bot_data_result, cursor, connection, embed_color, reddit, prefix)
            if message.content.startswith(botconfig['prefix'] + 'calc') or message.content.startswith(guild_result[6] + 'calc'):
                await calc_cmd(bot, discord, message, botconfig, os, platform, datetime, one_result, localization, numexpr, prefix)
            if message.content.startswith(botconfig['prefix'] + 'feedback') or message.content.startswith(guild_result[6] + 'feedback'):
                await feedback_cmd(bot, discord, message, botconfig, os, platform, datetime, one_result, localization, embed_color, prefix)
            if message.content.startswith(botconfig['prefix'] + 'weather') or message.content.startswith(guild_result[6] + 'weather'):
                await weather_cmd(bot, discord, sqlite3, message, botconfig, os, platform, datetime, one_result, localization, embed_color, requests)
            if message.content.startswith(botconfig['prefix'] + '8ball') or message.content.startswith(botconfig['prefix'] + 'crystball') or message.content.startswith(guild_result[6] + '8ball') or message.content.startswith(guild_result[6] + 'crystball'):
              await crystball_cmd(bot, discord, sqlite3, message, botconfig, os, platform, datetime, one_result, localization, embed_color, requests)
            if message.content.startswith(botconfig['prefix'] + 'post') or message.content.startswith(guild_result[6] + 'post'):
                await post_cmd(bot, discord, message, botconfig, platform, os, datetime, one_result, localization, unix_time_millis, embed_color, prefix)
            if message.content.startswith(botconfig['prefix'] + 'info') or message.content.startswith(guild_result[6] + 'info'):
                await info_cmd(bot, discord, message, botconfig, platform, os, datetime, one_result, localization, embed_color)
            if message.content.startswith(botconfig['prefix'] + 'codec') or message.content.startswith(guild_result[6] + 'codec'):
              args = message.content.split();
              try:
                if args[1] == "-d": 
                  await codec.decoder(bot, discord, message, botconfig, os, platform, datetime, one_result, localization, embed_color, args, binary, prefix)
                if args[1] == "-e":
                  await codec.encoder(bot, discord, message, botconfig, os, platform, datetime, one_result, localization, embed_color, args, binary, prefix)
              except Exception as e:
                await codec.get_help(bot, discord, message, botconfig, os, platform, datetime, one_result, localization, embed_color, prefix)
                print(e)
            if message.content.startswith(botconfig['prefix'] + 'poll') or message.content.startswith(guild_result[6] + 'poll'):
                await poll_cmd(bot, discord, message, botconfig, platform, os, datetime, one_result, localization, unix_time_millis, embed_color, connection, cursor, prefix)
            if message.content.startswith(botconfig['prefix'] + 'rep') or message.content.startswith(guild_result[6] + 'rep'):
                await rep_cmd(bot, discord, message, botconfig, platform, os, datetime, one_result, localization, embed_color, connection, cursor, prefix)
      except Exception as e:
        if message.content.startswith(botconfig['prefix']) or message.content.startswith(guild_result[6]):
          exc_type, exc_value, exc_tb = sys.exc_info()
          ex = traceback.format_exception(exc_type, exc_value, exc_tb)
          await logging.traceback_logger(bot, discord, message, one_result, guild_result, connection, cursor, unix_time_millis, botconfig, bot_data_result, ex, e)
          if str(e) == "local variable 'localization' referenced before assignment":
            if str(message.guild.region) == "russia":
              dbregistred_content = discord.Embed(title="База данных пользователя", description="База данных пользователя зарегистрирована. Напишите команду еще раз.", color=botconfig['accent1'])
            else:
              dbregistred_content = discord.Embed(title="User Database", description="Database registered. Type the command again", color=botconfig['accent1'])
            return await message.channel.send(embed=dbregistred_content)
          if str(e) == "list index out of range" or str(e) == "'NoneType' object is not subscriptable":
            pass
          errorcode = discord.Embed(title="Something went wrong...", description="This bug was reported to the bot developer.\n\n```" + ex[0] + "\n" + ex[1] + "\n" + ex[2] + "\nErrorcode: " + str(e) + "```", color=botconfig['accent1'])
          await message.channel.send(embed=errorcode)
          gc.collect()
        else:
          pass

bot.run(botconfig['token'])
