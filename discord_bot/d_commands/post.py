async def post_cmd(bot, discord, message, botconfig, platform, os, datetime, one_result, localization, unix_time_millis, embed_color):
  args = message.content.split();
  guild_community = ""
  for guild_features in message.guild.features:
      if guild_features == "COMMUNITY":
        guild_community = "COMMUNITY"
  if guild_community != "COMMUNITY":
      notcommunity_msg = discord.Embed(title=localization[1][13][0], description=localization[1][13][1], color=botconfig['accent2'])
      return await message.channel.send(embed=notcommunity_msg)
  if str(message.channel.type) == "news":
    if message.author.guild_permissions.manage_messages == True:
      try:
        await message.delete(delay=5000)
        no_args = discord.Embed(title=localization[1][13][0], description=localization[1][13][2], color=embed_color)
        if " ".join(args[1:]) == "" or " ".join(args[1:]) == " " or " ".join(args[1:]) == None:
            return await message.channel.send(embed=no_args)
        publishing_msg = discord.Embed(description=" ".join(args[1:]), color=embed_color)
        publishing_msg.set_footer(text=message.guild.name + " | " + message.author.name)
        msg = await message.channel.send(embed=publishing_msg)
        await msg.publish()
      except:
        pass
    else:
      noperm_msg = discord.Embed(title=localization[1][13][0], description=localization[1][13][3], color=botconfig['accent2'])
      return await message.channel.send(embed=noperm_msg)
  else:
    notnewsch_msg = discord.Embed(title=localization[1][13][0], description=localization[1][13][4], color=botconfig['accent2'])
    return await message.channel.send(embed=notnewsch_msg)
