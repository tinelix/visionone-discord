async def feedback_cmd(bot, discord, message, botconfig, os, platform, datetime, one_result, localization, embed_color, prefix):
  args = message.content.split();
  no_args = discord.Embed(title=localization[1][10][0], description=str(localization[1][10][3]).format(prefix), color=embed_color)
  if " ".join(args[1:]) == "" or " ".join(args[1:]) == " " or " ".join(args[1:]) == None:
    return await message.channel.send(embed=no_args)
  if message.author.id != int(botconfig['owner']):
    feedback_content = discord.Embed(title=localization[1][10][0], description=str(localization[1][10][2]), color=embed_color)
    new_message_content = discord.Embed(title='Feedback', description=message.author.name + "#" + str(message.author.discriminator) + ": \"" + " ".join(args[1:]) + "\"", color=embed_color)
    new_message_content.add_field(name="Channel ID", value=str(message.channel.id), inline=True)
    new_message_content.add_field(name="User ID", value=str(message.author.id), inline=True)
    if message.attachments is not None:
      attachments_str = "\n"
      try:
        for attachment in message.attachments:
          attachments_str += str("[Attachment " + str(message.attachments.index(attachment) + 1) + "](" + attachment.url + ")\n")
        if message.attachments != []:
          new_message_content.add_field(name="Attachments", value=attachments_str, inline=True)
      except:
        pass
    await bot.get_channel(botconfig['feedback_channel']).send(embed=new_message_content)
    await message.channel.send(embed=feedback_content)
  else:
    try:
      if args[1] != "-wt":
        ch_id = args[1]
        user_id = args[2]
        text_id = args[3:]
        new_message_content = discord.Embed(title=localization[1][10][1], description=localization[1][10][4] + "\"`" + " ".join(args[3:]) + "`\"", color=embed_color)
        await bot.get_channel(int(ch_id)).send("<@" + user_id + ">")
        await bot.get_channel(int(ch_id)).send(embed=new_message_content)
      if args[1] == "-wt":
        waiting_time = args[2]
    except:
      pass
