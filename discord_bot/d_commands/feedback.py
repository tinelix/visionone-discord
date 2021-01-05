async def feedback_cmd(bot, discord, message, botconfig, os, platform, datetime, one_result, localization, embed_color):
  args = message.content.split();
  no_args = discord.Embed(title=localization[1][10][0], description=localization[1][10][3], color=embed_color)
  if " ".join(args[1:]) == "" or " ".join(args[1:]) == " " or " ".join(args[1:]) == None:
    return await message.channel.send(embed=no_args)
  if message.author.id != int(botconfig['owner']):
    feedback_content = discord.Embed(title=localization[1][10][0], description=localization[1][10][2], color=embed_color)
    new_message_content = discord.Embed(title='Feedback', description=message.author.name + "#" + str(message.author.discriminator) + ": \"" + " ".join(args[1:]) + "\"", color=embed_color)
    new_message_content.add_field(name="Channel ID", value=str(message.channel.id), inline=True)
    new_message_content.add_field(name="User ID", value=str(message.author.id), inline=True)
    await bot.get_user(int(botconfig['owner'])).send(embed=new_message_content)
    await message.channel.send(embed=feedback_content)
  else:
    try:
      ch_id = args[1]
      user_id = args[2]
      text_id = args[3:]
      new_message_content = discord.Embed(title=localization[1][10][1], description=localization[1][10][4] + "\"`" + " ".join(args[3:]) + "`\"", color=embed_color)
      await bot.get_channel(int(ch_id)).send("<@" + user_id + ">")
      await bot.get_channel(int(ch_id)).send(embed=new_message_content)
    except:
      pass