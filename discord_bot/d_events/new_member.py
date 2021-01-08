async def autorole(bot, discord, member, botconfig):
  if member.guild.id == 795532426331422730:
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
            new_member_content = discord.Embed(title="Хорошо...", description="А Вы пока подождите админов, чтобы они руками давали роль участника.", color=botconfig['accent1'])
            await msg.edit(embed=new_member_content)