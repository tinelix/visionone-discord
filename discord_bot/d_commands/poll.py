def remove_outer_symbols(s):
    left = s.index("[")
    right = s.rindex("]", left)
    return s[:left] + s[left+1:right] + s[right+1:]

async def poll_cmd(bot, discord, message, botconfig, platform, os, datetime, one_result, localization, unix_time_millis, embed_color, connection, cursor, prefix):
  args = message.content.split(" ");
  args2 = message.content.split("-[]");
  parameter_option = ""
  args_str = " ".join(args[1:])
  emoji_number = {
      '0': '0️⃣',
      '1': '1️⃣',
      '2': '2️⃣',
      '3': '3️⃣',
      '4': '4️⃣',
      '5': '5️⃣',
      '6': '6️⃣',
      '7': '7️⃣',
      '8': '8️⃣',
      '9': '9️⃣'
    }
  try:
    question_rindex = args_str.rindex('-o', 0)
    question = args_str[:question_rindex]
    options_str = ""
    options = []
    endtimeerr = ""
    endtime = 0
    for args_index in args:
      try:
        endtime = int(unix_time_millis(datetime.datetime.strptime(args_index, '%Y-%m-%d=%H:%M')))
        endtimeerr = "" 
      except Exception as e:
        print(e)
        endtimeerr = "Error" 
    for args_index in args: 
      if args_index == "-o":
        parameter_option += '-o' 
    for args_index in args2: 
      try: 
        if message.content.startswith(botconfig['prefix']):
          index = args_str.index('[') + 6
          rindex = args_str.rindex(']') + 7
        elif message.content.startswith(prefix):
          index = args_str.index('[') + 5 + len(prefix)
          rindex = args_str.rindex(']') + 6 + len(prefix)
        options_str += remove_outer_symbols(args_index[index:rindex])
        options = options_str.split("],[")
      except:
        pass
    if endtime < (unix_time_millis(datetime.datetime.utcnow()) + one_result[3]):
          endtime = 0
          
    option_str = ""
    for opt in options:
      option_str += emoji_number[str(options.index(opt))] + " " + options[options.index(opt)] + "\n"
    if args[1] == "" or args[1] == None or args[2] == "" or parameter_option != '-o' or options == [] or args[2] == None or endtimeerr == "Error":
      no_args = discord.Embed(title=localization[1][16][0], description=str(localization[1][16][4]).format(prefix), color=embed_color)
      return await message.channel.send(embed=no_args)
    if endtime == 0:
      no_args = discord.Embed(title=localization[1][16][0], description=localization[1][16][5], color=embed_color)
      return await message.channel.send(embed=no_args)
    poll = [(message.id, message.author.id, endtime - one_result[3])]
    cursor.executemany("INSERT OR REPLACE INTO polls VALUES(?, ?, ?);", poll)
    connection.commit()
    cursor.execute("SELECT * FROM polls WHERE msgid='" + str(message.id) + "';")
    poll_result = cursor.fetchone()
    poll_content = discord.Embed(title=question, description=localization[1][16][2].format(str(datetime.datetime.fromtimestamp((poll_result[2] + one_result[3]) / 1000))) + "\n\n" + option_str, color=embed_color)
    msg = await message.channel.send(embed=poll_content)
    for opt in options:
        emoji = emoji_number[str(options.index(opt))]
        await msg.add_reaction(emoji=emoji)
  except Exception as e:
      print(e)
      no_args = discord.Embed(title=localization[1][16][0], description=str(localization[1][16][4]).format(prefix), color=embed_color)
      await message.channel.send(embed=no_args)
