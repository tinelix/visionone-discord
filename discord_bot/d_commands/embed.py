def remove_outer_symbols(s):
    left = s.index("[")
    right = s.rindex("]", left)
    return s[:left] + s[left+1:right] + s[right+1:]

async def embed_cmd(bot, discord, message, botconfig, platform, os, datetime, one_result, localization, unix_time_millis, embed_color, connection, cursor, prefix):
  args = message.content.split(" ");
  args2 = message.content.split("-[]");
  parameter_option = ""
  args_str = " ".join(args[1:])
  try:
    question_rindex = args_str.rindex('-t', 0)
    text = args_str[:question_rindex]
    options_str = ""
    options = []
    endtimeerr = ""
    endtime = 0
    for args_index in args: 
      if args_index == "-t":
        parameter_option += '-t' 
    for args_index in args2: 
      try: 
        if message.content.startswith(botconfig['prefix']):
          index = args_str.index('[') + 7
          rindex = args_str.rindex(']') + 8
        elif message.content.startswith(prefix):
          index = args_str.index('[') + 6 + len(prefix)
          rindex = args_str.rindex(']') + 7 + len(prefix)
        options_str += remove_outer_symbols(args_index[index:rindex])
        options = options_str.split("],[")
      except:
        pass
          
    embed_title = ""
    embed_footer = ""
    for opt in options:
      if options.index(opt) == 0:
       embed_title = opt
       print('Yes! ' + embed_title+ "\n" + str(options))
      if options.index(opt) == 1:
        embed_footer += opt
    if args[1] == "" or args[1] == None or args[2] == "" or parameter_option != '-t' or options == [] or args[2] == None:
      no_args = discord.Embed(title=localization[1][20][0], description=str(localization[1][20][1]).format(prefix), color=embed_color)
      return await message.channel.send(embed=no_args)
    embed = discord.Embed(title=embed_title, description=text, color=embed_color)
    embed.set_footer(text=embed_footer)
    msg = await message.channel.send(embed=embed)
  except Exception as e:
      print(e)
      no_args = discord.Embed(title=localization[1][16][0], description=str(localization[1][16][4]).format(prefix), color=embed_color)
      await message.channel.send(embed=no_args)
