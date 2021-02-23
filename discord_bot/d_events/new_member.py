import datetime

async def autorole(bot, discord, member, botconfig, cursor, connection, unix_time_millis):
  if member.guild.id == 795532426331422730:
    newbie_content = discord.Embed(title="Хитро!", description="К сожалению, Вы совсем недавно зарегистрировались в Discord, так как в целях безопасности вход для Вас упразднен. Советуем повторить верификацию через неделю.")
    if (unix_time_millis(datetime.datetime.utcnow()) - unix_time_millis(member.created_at)) < 604800000:
      await bot.get_channel(795621547946934292).send("<@" + str(member.id) + ">")
      return await bot.get_channel(795621547946934292).send(embed=newbie_content)
    new_member_content = discord.Embed(title=member.name + "#" + str(member.discriminator) + " пришел!", description="Привет! Для сохранения безопасной и комфортной атмосферы советуем прочитать правила в <#795532426331422733> и в окне приветствия. Для согласия нажмите на кнопку \"Выполнено\", затем после 10 минут на реакцию ✅.", color=botconfig['accent1'])
    await bot.get_channel(795621547946934292).send("<@" + str(member.id) + ">")
    msg = await bot.get_channel(795621547946934292).send(embed=new_member_content)
    await msg.add_reaction(emoji="✅")
    @bot.event
    async def on_reaction_add(reaction, user):
        channel = reaction.message.channel
        if reaction.emoji == "✅" and user.id != bot.user.id:
          try:
            await member.add_roles(member.guild.roles[2])
          except:
            new_member_content = discord.Embed(title="Хорошо...", description="А Вы пока подождите админов, чтобы они руками давали роль участника.\n\nЕсли заподозрим что-то неладное, администраторы могут в любой момент кикнуть или забанить Вас.", color=botconfig['accent1'])
            await msg.edit(embed=new_member_content)

async def new_member(bot, discord, member, botconfig, cursor, connection):
  try:
    cursor.execute("SELECT * FROM guilds WHERE guildid='" + str(member.guild.id) + "';")
    guild_result = (cursor.fetchone())
    search_results = 0
    for channel in member.guild.channels:
      if channel.id == guild_result[8]:
        search_results += 1
    msgtext = guild_result[9]
    try:
      msgtext_formatted = msgtext.format(user = member.name, user_with_discrim = str(member.name) + "#" + str(member.discriminator), mention = "<@" + str(member.id) + ">")
    except:
      msgtext_formatted = ""
    if search_results == 1 and guild_result[9] != None and guild_result[9] != "" and guild_result[9] != " " and msgtext_formatted != "":
      new_member_content = discord.Embed(description=msgtext_formatted, color=botconfig['accent1'])
      msg = await bot.get_channel(guild_result[8]).send(embed=new_member_content)
    if guild_result is None:
      return
  except:
    pass

async def member_left(bot, discord, member, botconfig, cursor, connection, guild_result):
  cursor.execute("SELECT * FROM guilds WHERE guildid='" + str(member.guild.id) + "';")
  guild_result = (cursor.fetchone())
  search_results = 0
  for channel in member.guild.channels:
    if channel.id == guild_result[10]:
      search_results += 1
  msgtext = guild_result[11]
  try:
    msgtext_formatted = msgtext.format(user = member.name, user_with_discrim = str(member.name) + "#" + str(member.discriminator), mention = "<@" + str(member.id) + ">")
  except:
    msgtext_formatted = ""
  if search_results == 1 and guild_result[11] != None and guild_result[11] != "" and guild_result[11] != " " and msgtext_formatted != "":
      new_member_content = discord.Embed(description=msgtext_formatted, color=botconfig['accent1'])
      msg = await bot.get_channel(guild_result[8]).send(embed=new_member_content)
  if guild_result is None:
      return