async def db_cmd(bot, discord, message, botconfig, os, platform, datetime, one_result, localization, connection, cursor, unix_time_millis):
        args = message.content.split();
        subargs = args[1:]
        accessdenied_msg = discord.Embed(description=localization[1][19][0], color=botconfig['accent2'])
        eval_content = discord.Embed(title="Просмотр базы данных", color=botconfig['accent1'])
        if str(message.author.id) != botconfig['owner']:
            return await message.channel.send(embed=accessdenied_msg)
        if args[1] == "-g":
          cursor.execute("SELECT * FROM guilds WHERE guildid='" + args[2] + "';")
          database = cursor.fetchall()
          try:
              result = str(database)
          except Exception as e:
              result = "Обнаружено исключение!\n" + str(e)
          finally:
              eval_content.add_field(name="Результат", value="```" + result + "```", inline=False)
              await message.channel.send(embed=eval_content)
        elif args[1] == "-u":
          try:
            cursor.execute("SELECT * FROM users WHERE userid='" + args[2] + "';")
            database = cursor.fetchall()
            try:
              result = str(database)
            except Exception as e:
              result = "Обнаружено исключение!\n" + str(e)
            finally:
              eval_content.add_field(name="Результат", value="```" + result + "```", inline=False)
              await message.channel.send(embed=eval_content)
          except:
              cursor.execute("SELECT * FROM users WHERE userid='" + str(args[2]) + "';")
              database = cursor.fetchall()
              if database != None:
                print("\n\nEval content:\n" + database)
              else:
                print("\n\nEval content:\n" + "(none)")
        elif args[1] == "-reg-u":
          try:
            user = [(args[2], args[3], 0, 10800000, unix_time_millis(message.created_at), "Disabled", unix_time_millis(message.created_at), 0, 0, 0)]
            cursor.executemany("INSERT OR REPLACE INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", user)
            cursor.execute("SELECT * FROM users WHERE userid='" + args[2] + "';")
            database = cursor.fetchall()
            try:
              result = str(database)
            except Exception as e:
              result = "Обнаружено исключение!\n" + str(e)
            finally:
              eval_content.add_field(name="Результат", value="```" + result + "```", inline=False)
              await message.channel.send(embed=eval_content)
          except Exception as e:
            result = "Обнаружено исключение!\n" + str(e)
            eval_content.add_field(name="Результат", value="```" + result + "```", inline=False)
            await message.channel.send(embed=eval_content)
        elif args[1] == "-reg-g":
          try:
            guild_info = bot.get_guild(int(args[2]))
            guild = [(args[2], str(guild_info.region), 0, unix_time_millis(message.created_at), "Disabled", "Standart", "=", args[3], 0, "", 0, "", "Disabled")]
            cursor.executemany("INSERT OR REPLACE INTO guilds VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", guild)
            cursor.execute("SELECT * FROM guilds WHERE guildid='" + args[2] + "';")
            database = cursor.fetchall()
            try:
              result = str(database)
            except Exception as e:
              result = "Обнаружено исключение!\n" + str(e)
            finally:
              eval_content.add_field(name="Результат", value="```" + result + "```", inline=False)
              await message.channel.send(embed=eval_content)
          except Exception as e:
            result = "Обнаружено исключение!\n" + str(e)
            eval_content.add_field(name="Результат", value="```" + result + "```", inline=False)
            await message.channel.send(embed=eval_content)
            