async def messaging_logger(bot, discord, message, one_result, guild_result, connection, cursor, unix_time_millis, botconfig, bot_data_result):
  logging_content = discord.Embed(title=botconfig['name'] + " Logger", description=str(message.author.name) + "#" + str(message.author.discriminator) + " typing \"" + message.content + "\" on " + message.guild.name + ", " + message.channel.name, color=botconfig['accent1'])
  logging_content.add_field(name="IDs", value="```S: " + str(message.guild.id) + "\nC: " + str(message.channel.id) + "\nU: " + str(message.author.id) + "```", inline=False)
  logging_content.add_field(name="Database changes", value="```S: " + str(guild_result) + "\nU: " + str(one_result) + "\nB: " + str(bot_data_result) + "```", inline=False)
  #await bot.get_channel(botconfig['logs_channel']).send(embed=logging_content)

async def traceback_logger(bot, discord, message, one_result, guild_result, connection, cursor, unix_time_millis, botconfig, bot_data_result, ex, e):
  logging_content = discord.Embed(title=botconfig['name'] + " Logger", description="Found bug.", color=botconfig['accent1'])
  logging_content.add_field(name="Traceback", value="```" + ex[0] + "\n" + ex[1] + "\n" + ex[2] + "\nErrorcode: " + str(e) + "```", inline=False)
  logging_content.add_field(name="Message", value="```" + str(message.author.name) + "#" + str(message.author.discriminator) + ": " + message.content + "```")
  #await bot.get_channel(botconfig['logs_channel']).send(embed=logging_content)


async def registration_logger(bot, discord, message, one_result, guild_result, connection, cursor, unix_time_millis, botconfig, bot_data_result, e):
  logging_content = discord.Embed(title=botconfig['name'] + " Logger", description="`" + str(message.author.name) + "#" + str(message.author.discriminator) + "` passed registation in DB.", color=botconfig['accent1'])
  logging_content.add_field(name="IDs", value="```S: " + str(message.guild.id) + "\nU: "+ str(message.author.id) + "```")
  logging_content.add_field(name="Database", value="```S: " + str(guild_result) + "\nU: "+ str(one_result) + "```")
  #await bot.get_channel(botconfig['logs_channel']).send(embed=logging_content)

async def joining_logger(bot, discord, guild, connection, cursor, unix_time_millis, botconfig):
  logging_content = discord.Embed(title=botconfig['name'] + " Logger", description="Bot joined the **" + str(guild.name) + "** server! We have " + str(len(bot.guilds)) + " guilds.", color=botconfig['accent1'])
  logging_content.add_field(name="IDs", value="```S: " + str(guild.id) + "\nO: " + str(guild.owner_id) + "```", inline=False)
  logging_content.add_field(name="Statistics", value="```Owner: " + str(guild.owner.name) + "#" + str(guild.owner.discriminator) + "\nMembers: " + str(guild.member_count) + "\nBoosts: " + str(guild.premium_subscription_count) + "\nChannels: Text - " + str(len(guild.text_channels)) + " | Voice - " + str(len(guild.voice_channels)) + "\nRegion: " + str(guild.region) + "```", inline=False)
  logging_content.set_thumbnail(url=str(guild.icon_url_as(format=None, static_format="jpeg", size=4096)))
  #await bot.get_channel(botconfig['logs_channel']).send(embed=logging_content)


async def leaving_logger(bot, discord, guild, connection, cursor, unix_time_millis, botconfig):
  logging_content = discord.Embed(title=botconfig['name'] + " Logger", description="Bot left the **" + str(guild.name) + "** server. We have " + str(len(bot.guilds)) + " guilds.", color=botconfig['accent1'])
  logging_content.add_field(name="IDs", value="```S: " + str(guild.id) + "\nO: " + str(guild.owner_id) + "```", inline=False)
  logging_content.set_thumbnail(url=str(guild.icon_url_as(format=None, static_format="jpeg", size=4096)))
  #await bot.get_channel(botconfig['logs_channel']).send(embed=logging_content)

