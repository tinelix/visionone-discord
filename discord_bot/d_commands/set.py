from .settings import settings_cmd

async def set_bot_language(bot, discord, message, botconfig, os, platform, datetime, one_result, args, connection, cursor, unix_time_millis):
    subargs = args[2]
    if subargs == "en-US":
        try:
            user = [(message.author.id, 'English', one_result[2] + 1, one_result[3], one_result[4], one_result[5], unix_time_millis(message.created_at))]
        except:
            user = [(message.author.id, 'English', 1, 10800000, unix_time_millis(message.created_at), 'Enabled', unix_time_millis(message.created_at))]
        cursor.executemany("INSERT OR REPLACE INTO users VALUES(?, ?, ?, ?, ?, ?, ?);", user)
        connection.commit()
        current_language = "English"
        botlanguage_content = discord.Embed(title="Bot language", description="Your language choosed to " + current_language, color=botconfig['accent1'])
        await message.channel.send(embed=botlanguage_content)
    if subargs == "ru-RU":
        try:
            user = [(message.author.id, 'Russian', one_result[2] + 1, one_result[3], one_result[4], "Enabled", unix_time_millis(message.created_at))]
        except:
            user = [(message.author.id, 'Russian', 1, 10800000, unix_time_millis(message.created_at), "Enabled", unix_time_millis(message.created_at))]
        cursor.executemany("INSERT OR REPLACE INTO users VALUES(?, ?, ?, ?, ?, ?, ?);", user)
        connection.commit()     
        current_language = "Russian"
        botlanguage_content = discord.Embed(title="Язык бота", description="Ваш язык выбран на " + current_language, color=botconfig['accent1'])
        await message.channel.send(embed=botlanguage_content)
    if subargs != "en-US" and subargs != "ru-RU":
        await settings_cmd(bot, discord, message, botconfig, os, platform, datetime, one_result)
        
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
                    user = [(message.author.id, one_result[1], one_result[2] + 1, int((-int(subargs2) / 10) * 60 * 60 * 1000), one_result[4], one_result[5], unix_time_millis(message.created_at))]
                except:
                    user = [(message.author.id, "Russian", 0, 10800000, unix_time_millis(message.created_at), "Enabled", unix_time_millis(message.created_at))]
            cursor.executemany("INSERT OR REPLACE INTO users VALUES(?, ?, ?, ?, ?, ?, ?);", user)
            connection.commit()
            timezone_content = discord.Embed(title=str(localization[1][2][3][0]), description=localization[1][2][4][2] + your_timezone, color=botconfig['accent1'])
            await message.channel.send(embed=timezone_content)
        else:
            return await message.channel.send(embed=stringnotisdigit_content)
    if int(subargs) >= -120 and int(subargs) <= 140:
        try:
            user = [(message.author.id, one_result[1], one_result[2] + 1, int((int(subargs) / 10) * 60 * 60 * 1000), one_result[4], one_result[5], unix_time_millis(message.created_at))]
        except:
            user = [(message.author.id, 'Russian', 1, int((subargs / 10) * 60 * 60 * 1000), unix_time_millis(message.created_at), 'Enabled', unix_time_millis(message.created_at))]
        cursor.executemany("INSERT OR REPLACE INTO users VALUES(?, ?, ?, ?, ?, ?, ?);", user)
        connection.commit()
        timezone_content = discord.Embed(title=str(localization[1][2][3][0]), description=localization[1][2][4][2] + your_timezone, color=botconfig['accent1'])
        await message.channel.send(embed=timezone_content)

async def switch_msgcounter(bot, discord, message, botconfig, os, platform, datetime, one_result, args, connection, cursor, localization, unix_time_millis):
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
                        guild = [(message.guild.id, one_result[1], one_result[2], one_result[3], 'Disabled', one_result[5], one_result[6], one_result[7], one_result[8], one_result[9], one_result[10], one_result[11])]
                    except:
                        guild = [(message.guild.id, str(message.guild.region), 1, unix_time_millis(message.created_at), 'Enabled', 'Standart', '=', 'English', 0, '', 0, '')]
                    cursor.executemany("INSERT OR REPLACE INTO guilds VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", guild)
                    connection.commit()
                    await msg.edit(embed=msgcounter_content)
                else:
                    await msg.edit(embed=nopermerr_content)
            if reaction.emoji == "👤" and user.id != bot.user.id:
                try:
                    user = [(message.author.id, one_result[1], one_result[2], one_result[3], one_result[4], 'Enabled', unix_time_millis(message.created_at))]
                except:
                    user = [(message.author.id, 'Russian', 1, 10800000, unix_time_millis(message.created_at), 'Enabled', unix_time_millis(message.created_at))]
                cursor.executemany("INSERT OR REPLACE INTO users VALUES(?, ?, ?, ?, ?, ?, ?);", user)
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
                        guild = [(message.guild.id, one_result[1], one_result[2], one_result[3], 'Disabled', one_result[5], one_result[6], one_result[7], one_result[8], one_result[9], one_result[10], one_result[11])]
                    except:
                        guild = [(message.guild.id, str(message.guild.region), 1, unix_time_millis(message.created_at), 'Disabled', "Standart", "=", 'English', 0, '', 0, '')]
                    cursor.executemany("INSERT OR REPLACE INTO guilds VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", guild)
                    connection.commit()
                    await msg.edit(embed=msgcounter_content)
                else:
                    await msg.edit(embed=nopermerr_content)
            if reaction.emoji == "👤" and user.id != bot.user.id:
                try:
                    user = [(message.author.id, one_result[1], one_result[2], one_result[3], one_result[4], 'Disabled', unix_time_millis(message.created_at))]
                except:
                    user = [(message.author.id, 'Russian', 1, 10800000, unix_time_millis(message.created_at), 'Disabled', unix_time_millis(message.created_at))]
                cursor.executemany("INSERT OR REPLACE INTO users VALUES(?, ?, ?, ?, ?, ?, ?);", user)
                connection.commit()
                await msg.edit(embed=msgcounter_content)
    if subargs != "off" and subargs != "on":
        await settings_cmd(bot, discord, message, botconfig, os, platform, datetime, one_result)
        
async def set_embed_color(bot, discord, message, botconfig, os, platform, datetime, one_result, args, connection, cursor, localization, unix_time_millis, embed_color):
    subargs = args[2]
 
    nopermerr_content = discord.Embed(title=str(localization[1][2][5][5]), description=str(localization[1][2][5][4]), color=botconfig['accent2'])
    if message.author.guild_permissions.manage_guild == True: 
      if subargs == "red":
        try:
          print('test')
          guild = [(message.guild.id, one_result[1], one_result[2], one_result[3], one_result[4], "Red", one_result[6], one_result[7], one_result[8], one_result[9], one_result[10], one_result[11])]
        except:
          guild = [(message.guild.id, str(message.guild.region), 1, unix_time_millis(message.created_at), 'Enabled', "Red", "=", 'English', 0, '', 0, '')]
      if subargs == "orange":
        try:
          guild = [(message.guild.id, one_result[1], one_result[2], one_result[3], one_result[4], "Standart", one_result[6], one_result[7], one_result[8], one_result[9], one_result[10], one_result[11])]
        except:
          guild = [(message.guild.id, str(message.guild.region), 1, unix_time_millis(message.created_at), 'Enabled', "Standart", "=", 'English', 0, '', 0, '')]
      if subargs == "yellow":
        try:
          guild = [(message.guild.id, one_result[1], one_result[2], one_result[3], one_result[4], "Yellow", one_result[6], one_result[7], one_result[8], one_result[9], one_result[10], one_result[11])]
        except:
          guild = [(message.guild.id, str(message.guild.region), 1, unix_time_millis(message.created_at), 'Enabled', "Yellow", "=", 'English', 0, '', 0, '')]
      if subargs == "green":
        try:
          guild = [(message.guild.id, one_result[1], one_result[2], one_result[3], one_result[4], "Green", one_result[6], one_result[7], one_result[8], one_result[9], one_result[10], one_result[11])]
        except:
          guild = [(message.guild.id, str(message.guild.region), 1, unix_time_millis(message.created_at), 'Enabled', "Green", "=", 'English', 0, '', 0, '')]
      if subargs == "skyblue":
        try:
          guild = [(message.guild.id, one_result[1], one_result[2], one_result[3], one_result[4], "Sky-blue", one_result[6], one_result[7], one_result[8], one_result[9], one_result[10], one_result[11])]
        except:
          guild = [(message.guild.id, str(message.guild.region), 1, unix_time_millis(message.created_at), 'Enabled', "Sky-blue", "=", 'English', 0, '', 0, '')]
      if subargs == "blue":
        try:
          guild = [(message.guild.id, one_result[1], one_result[2], one_result[3], one_result[4], "Blue", one_result[6], one_result[7], one_result[8], one_result[9], one_result[10], one_result[11])]
        except:
          guild = [(message.guild.id, str(message.guild.region), 1, unix_time_millis(message.created_at), 'Enabled', "Blue", "=", 'English', 0, '', 0, '')]
      if subargs == "violet":
        try:
          guild = [(message.guild.id, one_result[1], one_result[2], one_result[3], one_result[4], "Violet", one_result[6], one_result[7], one_result[8], one_result[9], one_result[10], one_result[11])]
        except:
          guild = [(message.guild.id, str(message.guild.region), 1, unix_time_millis(message.created_at), 'Enabled', "Violet", "=", 'English', 0, '', 0, '')]
      if subargs == "rose":
        try:
          guild = [(message.guild.id, one_result[1], one_result[2], one_result[3], one_result[4], "Rose", one_result[6], one_result[7], one_result[8], one_result[9], one_result[10], one_result[11])]
        except:
          guild = [(message.guild.id, str(message.guild.region), 1, unix_time_millis(message.created_at), 'Enabled', "Rose", "=", 'English', 0, '', 0, '')]
      try:    
        cursor.executemany("INSERT OR REPLACE INTO guilds VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", guild)
        connection.commit()
        customecolor_content = discord.Embed(title=str(localization[1][2][7][0]), description=str(localization[1][2][7][6]), color=embed_color)
        await message.channel.send(embed=customecolor_content)
      except:
        pass
    else:
      return await message.channel.send(embed=nopermerr_content)
