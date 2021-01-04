import discord
import platform
import os
import sqlite3
import datetime
import requests
import time
import sys
import traceback
from threading import Timer
from sqlite3 import Error
from discord.ext import commands
from .discord_botconfig import botconfig
import keep_alive
import numexpr

from unsplash.api import Api as unsplash_api
from unsplash.auth import Auth
from .d_commands.help import help_cmd
from .d_commands.state import state_cmd
from .d_commands.eval import eval_cmd
from .d_commands.settings import settings_cmd
from .d_commands.photo import photo_cmd
from .d_commands.calc import calc_cmd
import discord_bot.d_commands.set as settings
import discord_bot.d_commands.profile as profile
import discord_bot.d_events.cooldown as cooldown
import discord_bot.d_events.logging as logging
import discord_bot.d_author_cmds.tnews as tnews
import discord_bot.d_commands.blacklist as blacklist

import discord_bot.d_languages.en_US as en_US
import discord_bot.d_languages.ru_RU as ru_RU

intents = discord.Intents.all()

auth = Auth(botconfig['unsplash_ak'], botconfig['unsplash_sk'], botconfig['unsplash_ur'], code='')
unsplash = unsplash_api(auth)

bot = discord.Client(intents=intents)
epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

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
        userid TEXT PRIMARY KEY,
        botlanguage TEXT,
        messages INT,
        timezone INT,
        dbregdate INT,
        messagecount TEXT,
        lastmsgtime INT);
    """)
cursor.execute("""CREATE TABLE IF NOT EXISTS guilds(
        guildid TEXT PRIMARY KEY,
        region TEXT,
        messages INT,
        dbregdate INT,
        messagecount TEXT,
        embedmsgcolor TEXT,
        msgprefix TEXT);
    """)
cursor.execute("""CREATE TABLE IF NOT EXISTS blacklist_guilds(
        guildid TEXT PRIMARY KEY);
    """)
cursor.execute("""CREATE TABLE IF NOT EXISTS bot_data(
        number INT PRIMARY KEY,
        unsplash_count INT);
    """)
connection.commit()

@bot.event
async def on_ready():
    keep_alive.keep_alive()
    print('\nWelcome! Vision ver. ' + botconfig['version'] + '\n(©) 2020-2021 Tinelix. All rights reserved.')
    print('\nConnected - ' + bot.user.name + '#' + bot.user.discriminator + '\nLatency: ' + str(round(bot.latency * 1000, 2)) + ' ms | Guilds: ' + str(len(bot.guilds)))
    print('----------------------------------------------------------------------')
    game = discord.Game(str(len(bot.guilds)) + " guilds | =help", type=discord.ActivityType.watching)
    await bot.change_presence(status=discord.Status.dnd, activity=game)

@bot.event
async def on_guild_join(guild):
    game = discord.Game(str(len(bot.guilds)) + " guilds | =help", type=discord.ActivityType.watching)
    await bot.change_presence(status=discord.Status.dnd, activity=game)
    try:
      cursor.execute("SELECT * FROM blacklist_guilds WHERE guildid='" + str(guild.id) + "';")
      blacklist_guild_result = cursor.fetchone()
      print("SQLite Database | " + str(blacklist_guild_result))
      await bot.get_guild(int(blacklist_guild_result[0])).leave()
    except Exception as e:
      print(e)
    guild_s = [(guild.id, str(guild.region), 0, unix_time_millis(datetime.datetime.now()), "Enabled")]
    cursor.executemany("INSERT OR REPLACE INTO guilds VALUES(?, ?, ?, ?, ?);", guild_s)
    # print(guild)
    connection.commit()
    await logging.joining_logger(bot, discord, guild, connection, cursor, unix_time_millis, botconfig)
    
@bot.event
async def on_message(message):
    if message.author == bot.user or str(message.channel.type) == "private" or message.author.bot == True:
        return
    cursor.execute("SELECT * FROM users WHERE userid='" + str(message.author.id) + "';")
    one_result = cursor.fetchone()
    # print("SQLite Database | " + str(one_result))
    cursor.execute("SELECT * FROM guilds WHERE guildid='" + str(message.guild.id) + "';")
    guild_result = cursor.fetchone()
    # print("SQLite Database | " + str(guild_result))
    cursor.execute("SELECT * FROM users WHERE userid='" + str(message.author.id) + "';")
    cursor.execute("SELECT * FROM bot_data WHERE number='" + str(0) + "';")
    bot_data_result = cursor.fetchone()
    try:
        lastmsgtime = one_result[6]
    except:
        lastmsgtime = 0
    bot_data = [(0, 0)]
    try:
        if message.content.startswith(botconfig['prefix']):
            time_diff = ((datetime.datetime.utcnow() - epoch).total_seconds() * 1000) - one_result[6]
            if time_diff < 2000:
                return await cooldown.cooldown(bot, message, one_result, guild_result, connection, cursor, unix_time_millis, ru_RU, en_US)
            await logging.messaging_logger(bot, discord, message, one_result, guild_result, connection, cursor, unix_time_millis, botconfig, bot_data_result)
        if message.content.startswith(botconfig['prefix'] + "photo"):
            time_diff = ((datetime.datetime.utcnow() - epoch).total_seconds() * 1000) - one_result[6]
            if time_diff >= 3600000:
                bot_data = [(0, 0)]
                cursor.executemany("INSERT OR REPLACE INTO bot_data VALUES(?, ?)", bot_data)
                connection.commit()
            if bot_data_result[1] >= 20:
                return await cooldown.cooldown(bot, message, one_result, guild_result, connection, cursor, unix_time_millis, ru_RU, en_US)
        if one_result[1] == "Russian":
            localization = ru_RU.get()
        if one_result[1] == "English":
            localization = en_US.get()
        if one_result[5] == "Enabled":
            user = [(message.author.id, one_result[1], one_result[2] + 1, one_result[3], one_result[4], "Enabled", unix_time_millis(message.created_at))]
        if one_result[5] == "Disabled": 
            user = [(message.author.id, one_result[1], one_result[2], one_result[3], one_result[4], "Disabled", unix_time_millis(message.created_at))]
        else:
            user = [(message.author.id, one_result[1], one_result[2] + 1, one_result[3], one_result[4], one_result[5], unix_time_millis(message.created_at))]
        if guild_result[4] == "Enabled":
            guild = [(message.guild.id, guild_result[1], guild_result[2] + 1, guild_result[3], "Enabled", guild_result[5], guild_result[6])]
        if guild_result[4] == "Disabled": 
            guild = [(message.guild.id, guild_result[1], guild_result[2], guild_result[3], "Disabled", guild_result[5], guild_result[6])]
        else:
            guild = [(message.guild.id, guild_result[1], guild_result[2] + 1, guild_result[3], guild_result[4], guild_result[5], guild_result[6])] 
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
        if message.guild.region == "russia":
            user = [(message.author.id, "Russian", 0, 10800000, unix_time_millis(message.created_at), "Enabled", unix_time_millis(message.created_at))]
        else:
            user = [(message.author.id, "English", 0, 10800000, unix_time_millis(message.created_at), "Enabled", unix_time_millis(message.created_at))]
        print(e)
        guild = [(message.guild.id, str(message.guild.region), 0, unix_time_millis(message.created_at), "Enabled", "Standart", "=")]
        bot_data = [(0, 0)]
        exc_type, exc_value, exc_tb = sys.exc_info()
        ex = traceback.format_exception(exc_type, exc_value, exc_tb)
        await logging.traceback_logger(bot, discord, message, one_result, guild_result, connection, cursor, unix_time_millis, botconfig, bot_data_result, ex, e)
    
    cursor.executemany("INSERT OR REPLACE INTO users VALUES(?, ?, ?, ?, ?, ?, ?);", user)
    # print(user)
    connection.commit()
    cursor.executemany("INSERT OR REPLACE INTO guilds VALUES(?, ?, ?, ?, ?, ?, ?);", guild)
    # print(guild)
    cursor.executemany("INSERT OR REPLACE INTO bot_data VALUES(?, ?)", bot_data)
    connection.commit()
    timingcount = 0
    if message.content.startswith(botconfig['prefix']):
      try:
            time_diff = (datetime.datetime.utcnow() - epoch).total_seconds() - 2
            print(time_diff)
            if time_diff >= 120:
                pass
            if message.content.startswith(botconfig['prefix'] + 'help'):
              try:
                await help_cmd(bot, discord, message, botconfig, os, platform, datetime, one_result, localization, embed_color)
              except:
                if str(message.guild.region) == "russia":
                  await help_cmd(bot, discord, message, botconfig, os, platform, datetime, one_result, ru_RU.get(), botconfig['accent1'])
                else:
                  await help_cmd(bot, discord, message, botconfig, os, platform, datetime, one_result, en_US.get(), botconfig['accent1'])
            if message.content.startswith(botconfig['prefix'] + 'state'):
                await state_cmd(bot, discord, sqlite3, message, botconfig, os, platform, datetime, one_result, localization, embed_color, connection, cursor)
            if message.content.startswith(botconfig['prefix'] + 'eval'):
                await eval_cmd(bot, discord, message, botconfig, os, platform, datetime, one_result, localization, en_US, guild_result, intents, embed_color)
            if message.content.startswith(botconfig['prefix'] + 'clock'):
                await eval_cmd(bot, discord, message, botconfig, os, platform, datetime, one_result, localization, en_US, guild_result, intents, embed_color)
            if message.content.startswith(botconfig['prefix'] + 'settings'):
                await settings_cmd(bot, discord, message, botconfig, os, platform, datetime, one_result, localization, unix_time_millis, embed_color)
            if message.content.startswith(botconfig['prefix'] + 'set'):
              try:
                args = message.content.split();
                if args[1] == "-l":
                    await settings.set_bot_language(bot, discord, message, botconfig, os, platform, datetime, one_result, args, connection, cursor, unix_time_millis)
                if args[1] == "-tz":
                    await settings.set_timezone(bot, discord, message, botconfig, os, platform, datetime, one_result, args, connection, cursor, localization, unix_time_millis)
                if args[1] == "-mc":
                    await settings.switch_msgcounter(bot, discord, message, botconfig, os, platform, datetime, one_result, args, connection, cursor, localization, unix_time_millis)
                if args[1] == "-ec":
                    await settings.set_embed_color(bot, discord, message, botconfig, os, platform, datetime, one_result, args, connection, cursor, localization, unix_time_millis, embed_color)
                else: return
              except:
                pass
            if message.content.startswith(botconfig['prefix'] + 'profile'):
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
                    await profile.get_help(bot, discord, message, botconfig, platform, os, datetime, one_result, localization, args, unix_time_millis, connection, cursor, embed_color)
            if message.content.startswith(botconfig['prefix'] + 'tnews'):
                args = message.content.split();
                await tnews.get_tnews(bot, discord, message, botconfig, platform, os, datetime, one_result, localization, args, unix_time_millis, connection, cursor, embed_color)
            if message.content.startswith(botconfig['prefix'] + 'blacklist'):
                args = message.content.split();
                try:
                    if args[1] == "-ag":
                        await blacklist.add_guild_to_blacklist(bot, discord, message, botconfig, platform, os, datetime, one_result, localization, args, unix_time_millis, connection, cursor)
                except Exception as e: 
                    print(e)
            if message.content.startswith(botconfig['prefix'] + 'photo'):
                await photo_cmd(bot, discord, message, botconfig, os, platform, datetime, one_result, localization, unix_time_millis, unsplash, time_diff, bot_data_result, cursor, connection, embed_color)
            if message.content.startswith(botconfig['prefix'] + 'calc'):
                await calc_cmd(bot, discord, message, botconfig, os, platform, datetime, one_result, localization, numexpr)
      except Exception as e:
        if message.content.startswith(botconfig['prefix']):
          exc_type, exc_value, exc_tb = sys.exc_info()
          ex = traceback.format_exception(exc_type, exc_value, exc_tb)
          await logging.traceback_logger(bot, discord, message, one_result, guild_result, connection, cursor, unix_time_millis, botconfig, bot_data_result, ex, e)
          if str(e) == "local variable 'localization' referenced before assignment" or str(e) == "'NoneType' object is not subscriptable":
            dbregistred_content = discord.Embed(title="База данных пользователя", description="База данных пользователя зарегистрирована, пишите команду еще раз.", color=botconfig['accent1'])
            return await message.channel.send(embed=dbregistred_content)
          if str(e) == "list index out of range":
            pass
          errorcode = discord.Embed(title="Something went wrong...", description="This bug was reported to the bot developer.\n\n```" + ex[0] + "\n" + ex[1] + "\n" + ex[2] + "\nErrorcode: " + str(e) + "```", color=botconfig['accent1'])
          await message.channel.send(embed=errorcode)
bot.run(botconfig['token'])
