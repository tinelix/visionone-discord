from .settings import settings_cmd

async def set_bot_language(bot, discord, message, botconfig, os, platform, datetime, one_result, args, connection, cursor, unix_time_millis, en_US, ru_RU, guild_result, prefix, embed_color, localization):
    subargs = args[2]
    if subargs == "en-US":
        localization = en_US.get()
        botlanguage_choice = discord.Embed(title=str(localization[1][2][2][0]), description=str(localization[1][2][5][1]), color=botconfig['accent1'])
        nopermerr_content = discord.Embed(title=str(localization[1][2][2][0]), description=str(localization[1][2][5][4]), color=botconfig['accent1'])
        msg = await message.channel.send(embed=botlanguage_choice)
        await msg.add_reaction(emoji="🏠")
        await msg.add_reaction(emoji="👤")
        @bot.event
        async def on_reaction_add(reaction, user):
            channel = reaction.message.channel
            if reaction.emoji == "🏠" and user.id != bot.user.id:
              if message.author.guild_permissions.manage_guild == True:
                try:
                  guild = [(message.guild.id, guild_result[1], guild_result[2], guild_result[3], guild_result[4], guild_result[5], guild_result[6], 'English', guild_result[8], guild_result[9], guild_result[10], guild_result[11], guild_result[12])]
                except:
                  guild = [(message.guild.id, str(message.guild.region), 1, unix_time_millis(message.created_at), 'Enabled', 'Standart', '=', 'English', 0, '', 0, '', "Enabled")]
                cursor.executemany("INSERT OR REPLACE INTO guilds VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", guild)
                connection.commit()
                current_language = "English"
                botlanguage_content = discord.Embed(title="Bot language", description="Your language choosed to " + current_language, color=botconfig['accent1'])
                await msg.edit(embed=botlanguage_content) 
              else:
                msg.edit(embed=nopermerr_content)
            if reaction.emoji == "👤" and user.id != bot.user.id:
              try:
                user = [(message.author.id, 'English', one_result[2] + 1, one_result[3], one_result[4], one_result[5], unix_time_millis(message.created_at), one_result[7], one_result[8], one_result[9])]
              except:
                user = [(message.author.id, 'English', 1, 10800000, unix_time_millis(message.created_at), 'Enabled', unix_time_millis(message.created_at), 0, 0 ,0)]
              cursor.executemany("INSERT OR REPLACE INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", user)
              connection.commit()
              current_language = "English"
              botlanguage_content = discord.Embed(title="Bot language", description="Your language choosed to " + current_language, color=botconfig['accent1'])
              await msg.edit(embed=botlanguage_content)
    if subargs == "ru-RU":
        localization = ru_RU.get()
        botlanguage_choice = discord.Embed(title=str(localization[1][2][2][0]), description=str(localization[1][2][5][1]), color=botconfig['accent1'])
        nopermerr_content = discord.Embed(title=str(localization[1][2][2][0]), description=str(localization[1][2][5][4]), color=botconfig['accent1'])
        msg = await message.channel.send(embed=botlanguage_choice)
        await msg.add_reaction(emoji="🏠")
        await msg.add_reaction(emoji="👤")
        @bot.event
        async def on_reaction_add(reaction, user):
            channel = reaction.message.channel
            if reaction.emoji == "🏠" and user.id != bot.user.id:
              if message.author.guild_permissions.manage_guild == True:
                try:
                  guild = [(message.guild.id, guild_result[1], guild_result[2], guild_result[3], guild_result[4], guild_result[5], guild_result[6], 'Russian', guild_result[8], guild_result[9], guild_result[10], guild_result[11], guild_result[12])]
                except:
                  guild = [(message.guild.id, str(message.guild.region), 1, unix_time_millis(message.created_at), 'Enabled', 'Standart', '=', 'Russian', 0, '', 0, '', "Enabled")]
                cursor.executemany("INSERT OR REPLACE INTO guilds VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", guild)
                connection.commit()
                current_language = "Russian"
                botlanguage_content = discord.Embed(title="Язык бота", description="Ваш язык изменен на " + current_language + "\n\nОбратите внимание, что настройки вступят в силу только после регистрации пользователя в нашу БД. В таком случае нужно поменять язык в личных настройках.", color=botconfig['accent1'])
                await msg.edit(embed=botlanguage_content) 
              else:
                msg.edit(embed=nopermerr_content)
            if reaction.emoji == "👤" and user.id != bot.user.id:
              try:
                user = [(message.author.id, 'Russian', one_result[2] + 1, one_result[3], one_result[4], one_result[5], unix_time_millis(message.created_at), one_result[7], one_result[8], one_result[9])]
              except:
                user = [(message.author.id, 'Russian', 1, 10800000, unix_time_millis(message.created_at), 'Enabled', unix_time_millis(message.created_at), 0, 0 ,0)]
              cursor.executemany("INSERT OR REPLACE INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", user)
              connection.commit()
              current_language = "Russian"
              botlanguage_content = discord.Embed(title="Язык бота", description="Ваш язык изменен на " + current_language, color=botconfig['accent1'])
              await msg.edit(embed=botlanguage_content)
    if subargs != "en-US" and subargs != "ru-RU":
        await settings_cmd(bot, discord, message, botconfig, os, platform, datetime, one_result, localization, unix_time_millis, embed_color, guild_result, prefix)
        
async def set_timezone(bot, discord, message, botconfig, os, platform, datetime, one_result, args, connection, cursor, localization, unix_time_millis):
    if one_result[3] < 0:
        your_timezone = "-" + str(-round(one_result[3] / 60 / 60 / 1000, 1))
    if one_result[3] > 0:
        your_timezone = "+" + str(round(one_result[3] / 60 / 60 / 1000, 1))
    if one_result[3] == 0:
        your_timezone = ""
    today_ms = int(unix_time_millis(datetime.datetime.utcnow()) + one_result[3])
    today = datetime.datetime.fromtimestamp((today_ms - 25200000) / 1000) # 25200000 for UTC+7
    subargs = args[2]
    subargs2 = subargs.lstrip("-")
    stringnotisdigit_content = discord.Embed(title=str(localization[1][2][4][0]), description=localization[1][2][4][1], color=botconfig['accent2'])
    if subargs.isdigit() == False:
        if subargs2.isdigit() == True:
            if -int(subargs) >= -120 and -int(subargs) <= 140:
                try:
                    user = [(message.author.id, one_result[1], one_result[2] + 1, int((-int(subargs2) / 10) * 60 * 60 * 1000), one_result[4], one_result[5], unix_time_millis(message.created_at), one_result[7], one_result[8], one_result[9])]
                except:
                    user = [(message.author.id, "Russian", 0, 10800000, unix_time_millis(message.created_at), "Enabled", unix_time_millis(message.created_at), 0, 0, 0)]
            cursor.executemany("INSERT OR REPLACE INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", user)
            connection.commit()
            timezone_content = discord.Embed(title=str(localization[1][2][3][0]), description=localization[1][2][4][2] + your_timezone, color=botconfig['accent1'])
            await message.channel.send(embed=timezone_content)
        else:
            return await message.channel.send(embed=stringnotisdigit_content)
    if int(subargs) >= 0:
        try:
            user = [(message.author.id, one_result[1], one_result[2] + 1, int((int(subargs) / 10) * 60 * 60 * 1000), one_result[4], one_result[5], unix_time_millis(message.created_at), one_result[7], one_result[8], one_result[9])]
        except:
            user = [(message.author.id, 'Russian', 1, int((subargs / 10) * 60 * 60 * 1000), unix_time_millis(message.created_at), 'Enabled', unix_time_millis(message.created_at), 0, 0, 0)]
        cursor.executemany("INSERT OR REPLACE INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", user)
        connection.commit()
        timezone_content = discord.Embed(title=str(localization[1][2][3][0]), description=localization[1][2][4][2] + your_timezone, color=botconfig['accent1'])
        await message.channel.send(embed=timezone_content)

async def switch_msgcounter(bot, discord, message, botconfig, os, platform, datetime, one_result, args, connection, cursor, localization, unix_time_millis, guild_result):
    subargs = args[2]
    if subargs == "on":
        msgcounter_choice = discord.Embed(title=str(localization[1][2][5][0]), description=str(localization[1][2][5][1]), color=botconfig['accent1'])
        msgcounter_content = discord.Embed(title=str(localization[1][2][5][0]), description=str(localization[1][2][5][2]), color=botconfig['accent1'])
        nopermerr_content = discord.Embed(title=str(localization[1][2][5][5]), description=str(localization[1][2][5][4]), color=botconfig['accent2'])
        msg = await message.channel.send(embed=msgcounter_choice)
        await msg.add_reaction(emoji="🏠")
        await msg.add_reaction(emoji="👤")
        @bot.event
        async def on_reaction_add(reaction, user):
            channel = reaction.message.channel
            if reaction.emoji == "🏠" and user.id != bot.user.id:
                if message.author.guild_permissions.manage_guild == True:
                    try:
                        guild = [(message.guild.id, guild_result[1], guild_result[2], guild_result[3], 'Disabled', guild_result[5], guild_result[6], guild_result[7], guild_result[8], guild_result[9], guild_result[10], guild_result[11], guild_result[12])]
                    except:
                        guild = [(message.guild.id, str(message.guild.region), 1, unix_time_millis(message.created_at), 'Enabled', 'Standart', '=', 'English', 0, '', 0, '', "Enabled")]
                    cursor.executemany("INSERT OR REPLACE INTO guilds VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", guild)
                    connection.commit()
                    await msg.edit(embed=msgcounter_content)
                else:
                    await msg.edit(embed=nopermerr_content)
            if reaction.emoji == "👤" and user.id != bot.user.id:
                try:
                    user = [(message.author.id, one_result[1], one_result[2], one_result[3], one_result[4], 'Enabled', unix_time_millis(message.created_at), one_result[7], one_result[8], one_result[9])]
                except:
                    user = [(message.author.id, 'Russian', 1, 10800000, unix_time_millis(message.created_at), 'Enabled', unix_time_millis(message.created_at), 0, 0, 0)]
                cursor.executemany("INSERT OR REPLACE INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", user)
                connection.commit()
                await msg.edit(embed=msgcounter_content)
    if subargs == "off":
        msgcounter_choice = discord.Embed(title=str(localization[1][2][5][0]), description=str(localization[1][2][5][1]), color=botconfig['accent1'])
        msgcounter_content = discord.Embed(title=str(localization[1][2][5][0]), description=str(localization[1][2][5][3]), color=botconfig['accent1'])
        nopermerr_content = discord.Embed(title=str(localization[1][2][5][5]), description=str(localization[1][2][5][4]), color=botconfig['accent2'])
        msg = await message.channel.send(embed=msgcounter_choice)
        await msg.add_reaction(emoji="🏠")
        await msg.add_reaction(emoji="👤")
        @bot.event
        async def on_reaction_add(reaction, user):
            channel = reaction.message.channel
            if reaction.emoji == "🏠" and user.id != bot.user.id:
                if message.author.guild_permissions.manage_guild == True:
                    try:
                        guild = [(message.guild.id, guild_result[1], guild_result[2], guild_result[3], 'Disabled', guild_result[5], guild_result[6], guild_result[7], guild_result[8], guild_result[9], guild_result[10], guild_result[11], guild_result[12])]
                    except:
                        guild = [(message.guild.id, str(message.guild.region), 1, unix_time_millis(message.created_at), 'Disabled', "Standart", "=", 'English', 0, '', 0, '', "Disabled")]
                    cursor.executemany("INSERT OR REPLACE INTO guilds VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", guild)
                    connection.commit()
                    await msg.edit(embed=msgcounter_content)
                else:
                    await msg.edit(embed=nopermerr_content)
            if reaction.emoji == "👤" and user.id != bot.user.id:
                try:
                    user = [(message.author.id, one_result[1], one_result[2], one_result[3], one_result[4], 'Disabled', unix_time_millis(message.created_at), one_result[7], one_result[8], one_result[9])]
                except:
                    user = [(message.author.id, 'Russian', 1, 10800000, unix_time_millis(message.created_at), 'Disabled', unix_time_millis(message.created_at), 0, 0, 0)]
                cursor.executemany("INSERT OR REPLACE INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);", user)
                connection.commit()
                await msg.edit(embed=msgcounter_content)
    if subargs != "off" and subargs != "on":
        await settings_cmd(bot, discord, message, botconfig, os, platform, datetime, one_result)
        
async def set_embed_color(bot, discord, message, botconfig, os, platform, datetime, one_result, args, connection, cursor, localization, unix_time_millis, embed_color, guild_result):
    subargs = args[2]
 
    nopermerr_content = discord.Embed(title=str(localization[1][2][5][5]), description=str(localization[1][2][5][4]), color=botconfig['accent2'])
    if message.author.guild_permissions.manage_guild == True: 
      if subargs == "red":
        try:
          print('test')
          guild = [(message.guild.id, one_result[1], guild_result[2], guild_result[3], guild_result[4], "Red", guild_result[6], guild_result[7], guild_result[8], guild_result[9], guild_result[10], guild_result[11], guild_result[12])]
        except:
          guild = [(message.guild.id, str(message.guild.region), 1, unix_time_millis(message.created_at), 'Enabled', "Red", "=", 'English', 0, '', 0, '', "Disabled")]
      if subargs == "orange":
        try:
          guild = [(message.guild.id, one_result[1], guild_result[2], guild_result[3], guild_result[4], "Standart", guild_result[6], guild_result[7], guild_result[8], guild_result[9], guild_result[10], guild_result[11], guild_result[12])]
        except:
          guild = [(message.guild.id, str(message.guild.region), 1, unix_time_millis(message.created_at), 'Enabled', "Standart", "=", 'English', 0, '', 0, '', "Disabled")]
      if subargs == "yellow":
        try:
          guild = [(message.guild.id, one_result[1], guild_result[2], guild_result[3], guild_result[4], "Yellow", guild_result[6], guild_result[7], guild_result[8], guild_result[9], guild_result[10], guild_result[11], guild_result[12])]
        except:
          guild = [(message.guild.id, str(message.guild.region), 1, unix_time_millis(message.created_at), 'Enabled', "Yellow", "=", 'English', 0, '', 0, '', "Disabled")]
      if subargs == "green":
        try:
          guild = [(message.guild.id, one_result[1], guild_result[2], guild_result[3], guild_result[4], "Green", guild_result[6], guild_result[7], guild_result[8], guild_result[9], guild_result[10], guild_result[11], guild_result[12])]
        except:
          guild = [(message.guild.id, str(message.guild.region), 1, unix_time_millis(message.created_at), 'Enabled', "Green", "=", 'English', 0, '', 0, '', "Disabled")]
      if subargs == "skyblue":
        try:
          guild = [(message.guild.id, one_result[1], guild_result[2], guild_result[3], guild_result[4], "Sky-blue", guild_result[6], guild_result[7], guild_result[8], guild_result[9], guild_result[10], guild_result[11], guild_result[12])]
        except:
          guild = [(message.guild.id, str(message.guild.region), 1, unix_time_millis(message.created_at), 'Enabled', "Sky-blue", "=", 'English', 0, '', 0, '', "Disabled")]
      if subargs == "blue":
        try:
          guild = [(message.guild.id, one_result[1], guild_result[2], guild_result[3], guild_result[4], "Blue", guild_result[6], guild_result[7], guild_result[8], guild_result[9], guild_result[10], guild_result[11], guild_result[12])]
        except:
          guild = [(message.guild.id, str(message.guild.region), 1, unix_time_millis(message.created_at), 'Enabled', "Blue", "=", 'English', 0, '', 0, '', "Disabled")]
      if subargs == "violet":
        try:
          guild = [(message.guild.id, one_result[1], guild_result[2], guild_result[3], guild_result[4], "Violet", guild_result[6], guild_result[7], guild_result[8], guild_result[9], guild_result[10], guild_result[11], guild_result[12])]
        except:
          guild = [(message.guild.id, str(message.guild.region), 1, unix_time_millis(message.created_at), 'Enabled', "Violet", "=", 'English', 0, '', 0, '', "Disabled")]
      if subargs == "rose":
        try:
          guild = [(message.guild.id, one_result[1], guild_result[2], guild_result[3], guild_result[4], "Rose", guild_result[6], guild_result[7], guild_result[8], guild_result[9], guild_result[10], guild_result[11], guild_result[12])]
        except:
          guild = [(message.guild.id, str(message.guild.region), 1, unix_time_millis(message.created_at), 'Enabled', "Rose", "=", 'English', 0, '', 0, '', "Disabled")]
      try:    
        cursor.executemany("INSERT OR REPLACE INTO guilds VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", guild)
        connection.commit()
        customecolor_content = discord.Embed(title=str(localization[1][2][7][0]), description=str(localization[1][2][7][6]), color=embed_color)
        await message.channel.send(embed=customecolor_content)
      except:
        pass
    else:
      return await message.channel.send(embed=nopermerr_content)

async def set_prefix(bot, discord, message, botconfig, os, platform, datetime, one_result, args, connection, cursor, localization, unix_time_millis, embed_color, guild_result, prefix):
    subargs = args[2]
    nopermerr_content = discord.Embed(title=str(localization[1][2][5][5]), description=str(localization[1][2][5][4]), color=botconfig['accent2'])
    if message.author.guild_permissions.manage_guild == True:    
      try:
        guild = [(message.guild.id, guild_result[1], guild_result[2], guild_result[3], guild_result[4], guild_result[5], subargs, guild_result[7], guild_result[8], guild_result[9], guild_result[10], guild_result[11], guild_result[12])]
      except:
        guild = [(message.guild.id, str(message.guild.region), 1, unix_time_millis(message.created_at), 'Enabled', "Standart", subargs, 'English', 0, '', 0, '', "Disabled")]
      try:    
        cursor.executemany("INSERT OR REPLACE INTO guilds VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", guild)
        connection.commit()
        customprefix_content = discord.Embed(title=str(localization[1][2][8][0]), description=str(localization[1][2][7][6]), color=embed_color)
        await message.channel.send(embed=customprefix_content)
      except Exception as e:
        print(e)
    else:
      return await message.channel.send(embed=nopermerr_content)

async def switch_lvlsystem(bot, discord, message, botconfig, os, platform, datetime, one_result, args, connection, cursor, localization, unix_time_millis, embed_color, guild_result, prefix):
    subargs = args[2]
    nopermerr_content = discord.Embed(title=str(localization[1][2][5][5]), description=str(localization[1][2][5][4]), color=botconfig['accent2'])
    if message.author.guild_permissions.manage_guild == True:
        if subargs == "on":
            try:
                guild = [(message.guild.id, guild_result[1], guild_result[2], guild_result[3], guild_result[4], guild_result[5], guild_result[6], guild_result[7], guild_result[8], guild_result[9], guild_result[10], guild_result[11], "Enabled")]
            except:
                guild = [(message.guild.id, str(message.guild.region), 1, unix_time_millis(message.created_at), 'Enabled', "Standart", botconfig['prefix'], 'English', 0, '', 0, '', "Enabled")]   
            try:    
                cursor.executemany("INSERT OR REPLACE INTO guilds VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", guild)
                connection.commit() 
                levelsys_content = discord.Embed(title=str(localization[1][2][9][0]), description=str(localization[1][2][7][6]), color=embed_color)
                await message.channel.send(embed=levelsys_content)
            except Exception as e:
                print(e)
        if subargs == "off":
            try:
                guild = [(message.guild.id, guild_result[1], guild_result[2], guild_result[3], guild_result[4], guild_result[5], guild_result[6], guild_result[7], guild_result[8], guild_result[9], guild_result[10], guild_result[11], "Disabled")]
            except:
                guild = [(message.guild.id, str(message.guild.region), 1, unix_time_millis(message.created_at), 'Enabled', "Standart", botconfig['prefix'], 'English', 0, '', 0, '', "Disabled")]   
            
            try:    
                cursor.executemany("INSERT OR REPLACE INTO guilds VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", guild)
                connection.commit() 
                levelsys_content = discord.Embed(title=str(localization[1][2][9][0]), description=str(localization[1][2][7][6]), color=embed_color)
                await message.channel.send(embed=levelsys_content)
            except Exception as e:
                print(e)
    else:
        return await message.channel.send(embed=nopermerr_content)


async def set_welcome_message(bot, discord, message, botconfig, os, platform, datetime, one_result, args, connection, cursor, localization, unix_time_millis, embed_color, guild_result, prefix):
    subargs = args[2]
    msgtext = " ".join(args[3:])
    nopermerr_content = discord.Embed(title=str(localization[1][2][5][5]), description=str(localization[1][2][5][4]), color=botconfig['accent2'])
    channel_not_found = discord.Embed(title=str(localization[1][2][10][7]), description=str(localization[1][2][10][8]), color=botconfig['accent2'])
    if message.author.guild_permissions.manage_guild == True:
        if subargs.isdigit() == True and (msgtext != None or msgtext != "" or msgtext != " "):
            search_result = 0
            for channel in message.guild.channels:
                if channel.id == int(subargs):
                    search_result += 1
            if search_result >= 1:
                try:
                    guild = [(message.guild.id, guild_result[1], guild_result[2], guild_result[3], guild_result[4], guild_result[5], guild_result[6], guild_result[7], int(subargs), msgtext, guild_result[10], guild_result[11], guild_result[12])]
                except:
                    guild = [(message.guild.id, str(message.guild.region), 1, unix_time_millis(message.created_at), 'Enabled', "Standart", botconfig['prefix'], 'English', int(subargs), msgtext, 0, '', "Disabled")]   
                try:    
                    cursor.executemany("INSERT OR REPLACE INTO guilds VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", guild)
                    connection.commit() 
                    welcomemsg_content = discord.Embed(title=str(localization[1][2][10][0]), description=str(localization[1][2][7][6]), color=embed_color)
                    await message.channel.send(embed=welcomemsg_content)
                except Exception as e:
                    print(e)
            else:
                await message.channel.send(embed=channel_not_found)

        elif subargs == "off":
            try:
                guild = [(message.guild.id, guild_result[1], guild_result[2], guild_result[3], guild_result[4], guild_result[5], guild_result[6], guild_result[7], 0, '', guild_result[10], guild_result[11], guild_result[12])]
            except:
                guild = [(message.guild.id, str(message.guild.region), 1, unix_time_millis(message.created_at), 'Enabled', "Standart", botconfig['prefix'], 'English', 0, '', 0, '', "Disabled")]   
            
            try:    
                cursor.executemany("INSERT OR REPLACE INTO guilds VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", guild)
                connection.commit() 
                welcomemsg_content = discord.Embed(title=str(localization[1][2][10][0]), description=str(localization[1][2][7][6]), color=embed_color)
                await message.channel.send(embed=welcomemsg_content)
            except Exception as e:
                print(e)
        else:
            welcomemsg_content = discord.Embed(title=str(localization[1][2][10][0]), color=embed_color)
            welcomemsg_content.add_field(name=str(localization[1][2][10][1]), value=str(localization[1][2][10][2]), inline=True)
            welcomemsg_content.add_field(name=str(localization[1][2][10][3]), value=str(localization[1][2][10][4]).format(prefix).replace('╭', '{').replace('╮', '}'), inline=False)
            welcomemsg_content.add_field(name=str(localization[1][2][10][5]), value=str(localization[1][2][10][6]), inline=True)
            return await message.channel.send(embed=welcomemsg_content)
    else:
        return await message.channel.send(embed=nopermerr_content)

async def set_goodbye_message(bot, discord, message, botconfig, os, platform, datetime, one_result, args, connection, cursor, localization, unix_time_millis, embed_color, guild_result, prefix):
    subargs = args[2]
    msgtext = " ".join(args[3:])
    nopermerr_content = discord.Embed(title=str(localization[1][2][5][5]), description=str(localization[1][2][5][4]), color=botconfig['accent2'])
    channel_not_found = discord.Embed(title=str(localization[1][2][10][7]), description=str(localization[1][2][10][8]), color=botconfig['accent2'])
    if message.author.guild_permissions.manage_guild == True:
        if subargs.isdigit() == True and (msgtext != None or msgtext != "" or msgtext != " "):
            search_result = 0
            for channel in message.guild.channels:
                if channel.id == int(subargs):
                    search_result += 1
            if search_result >= 1:
                #msgtext.format(user = member.name, user_with_discrim = str(member.name) + "#" + str(member.discriminator), mention = "<@" + member.id + ">")
                try:
                    guild = [(message.guild.id, guild_result[1], guild_result[2], guild_result[3], guild_result[4], guild_result[5], guild_result[6], guild_result[7], guild_result[8], guild_result[9], int(subargs), msgtext, guild_result[12])]
                except:
                    guild = [(message.guild.id, str(message.guild.region), 1, unix_time_millis(message.created_at), 'Enabled', "Standart", botconfig['prefix'], 'English', 0, '', int(subargs), msgtext, "Disabled")]   
                try:    
                    cursor.executemany("INSERT OR REPLACE INTO guilds VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", guild)
                    connection.commit() 
                    welcomemsg_content = discord.Embed(title=str(localization[1][2][10][0]), description=str(localization[1][2][7][6]), color=embed_color)
                    await message.channel.send(embed=welcomemsg_content)
                except Exception as e:
                    print(e)
            else:
                await message.channel.send(embed=channel_not_found)

        elif subargs == "off":
            try:
                guild = [(message.guild.id, guild_result[1], guild_result[2], guild_result[3], guild_result[4], guild_result[5], guild_result[6], guild_result[7], 0, '', guild_result[10], guild_result[11], guild_result[12])]
            except:
                guild = [(message.guild.id, str(message.guild.region), 1, unix_time_millis(message.created_at), 'Enabled', "Standart", botconfig['prefix'], 'English', 0, '', 0, '', "Disabled")]   
            
            try:    
                cursor.executemany("INSERT OR REPLACE INTO guilds VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", guild)
                connection.commit() 
                welcomemsg_content = discord.Embed(title=str(localization[1][2][10][0]), description=str(localization[1][2][7][6]), color=embed_color)
                await message.channel.send(embed=welcomemsg_content)
            except Exception as e:
                print(e)
        else:
            welcomemsg_content = discord.Embed(title=str(localization[1][2][10][0]), color=embed_color)
            welcomemsg_content.add_field(name=str(localization[1][2][10][1]), value=str(localization[1][2][10][2]), inline=False)
            welcomemsg_content.add_field(name=str(localization[1][2][10][3]), value=str(localization[1][2][10][4]).format(prefix).replace('╭', '{').replace('╮', '}'), inline=False)
            welcomemsg_content.add_field(name=str(localization[1][2][10][5]), value=str(localization[1][2][10][6]), inline=False)
            return await message.channel.send(embed=welcomemsg_content)
    else:
        return await message.channel.send(embed=nopermerr_content)