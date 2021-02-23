async def db_cmd(bot, discord, message, botconfig, os, platform, datetime, one_result, localization, connection, cursor):
        args = message.content.split();
        subargs = args[1:]
        accessdenied_msg = discord.Embed(description=localization[1][19][0], color=botconfig['accent2'])
        eval_content = discord.Embed(title="Просмотр базы данных", color=botconfig['accent1'])
        if str(message.author.id) != botconfig['owner']:
            return await message.channel.send(embed=accessdenied_msg)
        if args[1] == "-g":
          cursor.execute("SELECT * FROM guilds")
          database = cursor.fetchall()
          try:
              result = str(database)
          except Exception as e:
              result = "Обнаружено исключение!\n" + str(e)
          finally:
              eval_content.add_field(name="Результат", value="```" + result + "```", inline=False)
              await message.channel.send(embed=eval_content)
        elif args[1] == "-u":
          cursor.execute("SELECT * FROM users")
          database = cursor.fetchall()
          try:
              result = str(database)
          except Exception as e:
              result = "Обнаружено исключение!\n" + str(e)
          finally:
              eval_content.add_field(name="Результат", value="```" + result + "```", inline=False)
              await message.channel.send(embed=eval_content)
