async def rep_cmd(bot, discord, message, botconfig, platform, os, datetime, one_result, localization, embed_color, connection, cursor, prefix):
  args = message.content.split();
  rep_err_b = discord.Embed(title=str(localization[1][17][0]).format(prefix), description=str(localization[1][17][2]), color=embed_color)
  no_args = discord.Embed(title=str(localization[1][17][0]).format(prefix), color=embed_color)
  no_args.add_field(name=localization[1][17][5], value=str(localization[1][17][6]).format(prefix))
  try:
    if " ".join(args[1]) == "" or " ".join(args[1]) == " " or " ".join(args[1]) == None or args[1].isdigit() == False:
      return await message.channel.send(embed=no_args)
    if args[1] == str(one_result[0]):
      return await message.channel.send(embed=rep_err_b)
  except:
      return await message.channel.send(embed=no_args)
  try:
    rep_content = discord.Embed(title=str(localization[1][17][0]), description=str(localization[1][17][1]), color=embed_color)
    msg = await message.channel.send(embed=rep_content)
    await msg.add_reaction(emoji="👍")
    await msg.add_reaction(emoji="👎")
    @bot.event
    async def on_reaction_add(reaction, user):
        channel = reaction.message.channel
        if reaction.emoji == "👍" and user.id != bot.user.id:
          rep_content = discord.Embed(title=str(localization[1][17][0]), description=str(localization[1][17][4]), color=embed_color)
          rep_err_a = discord.Embed(title=str(localization[1][17][0]), description=str(localization[1][17][7]), color=embed_color)
          rep_err_c = discord.Embed(title=str(localization[1][17][0]), description=str(localization[1][17][8]), color=embed_color)
          userdb = one_result
          rep = cursor.execute("SELECT * FROM reputations WHERE userid = " +
	                        str(message.author.id) + " AND repid = "+ str(args[1]) + " ;").fetchone()
	           
          #print(str(userdb) + " | " + str(rep))
          if userdb == None:
            return await msg.edit(embed=rep_err_a)
          try:
            if rep[3] == "False":
              return await msg.edit(embed=rep_err_c)
          except:
            pass
          if rep == None or rep[3] == "False":
            if rep == None:
              reputation = [(message.id, message.author.id, args[1], 'True', 'False')]
            else:
              reputation = [(rep[0], rep[1], rep[2], 'True', 'False')]
            cursor.executemany("INSERT OR REPLACE INTO reputations VALUES(?, ?, ?, ?, ?);", reputation)
            connection.commit()
            user_rep = [(userdb[0], userdb[1], userdb[2], userdb[3], userdb[4], userdb[5], userdb[6], userdb[7] + 1, userdb[8], userdb[9])]
            cursor.executemany("INSERT OR REPLACE INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", user_rep)
            connection.commit()
            await msg.edit(embed=rep_content)
        if reaction.emoji == "👎" and user.id != bot.user.id:
          rep_content = discord.Embed(title=str(localization[1][17][0]), description=str(localization[1][17][3]), color=embed_color)
          rep_err_a = discord.Embed(title=str(localization[1][17][0]), description=str(localization[1][17][7]), color=embed_color)
          rep_err_c = discord.Embed(title=str(localization[1][17][0]), description=str(localization[1][17][9]), color=embed_color)
          rep = cursor.execute("SELECT * FROM reputations WHERE userid = " +
	                        str(message.author.id) + " AND repid = "+ str(args[1]) + " ;").fetchone()
          userdb = one_result
          if userdb == None:
            return await msg.edit(embed=rep_err_a)
          try:
            if rep[3] == "False":
              return await msg.edit(embed=rep_err_c)
          except:
            pass
          if rep == None or rep[3] == "True":
            if rep == None:
              reputation = [(message.id, message.author.id, args[1], 'False', 'True')]
            else:
              reputation = [(rep[0], rep[1], rep[2], 'False', 'True')]
            cursor.executemany("INSERT OR REPLACE INTO reputations VALUES(?, ?, ?, ?, ?);", reputation)
            connection.commit()
            user_rep = [(userdb[0], userdb[1], userdb[2], userdb[3], userdb[4], userdb[5], userdb[6], userdb[7] - 1, userdb[8], userdb[9])]
            cursor.executemany("INSERT OR REPLACE INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", user_rep)
            connection.commit()
            await msg.edit(embed=rep_content)
    #cursor.executemany("INSERT OR REPLACE INTO polls VALUES(?, ?, ?);", poll)
  except:
    pass