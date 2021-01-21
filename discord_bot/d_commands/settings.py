async def settings_cmd(bot, discord, message, botconfig, os, platform, datetime, one_result, localization, unix_time_millis, embed_color, guild_result, prefix):
        if one_result[3] < 0:
            your_timezone = "-" + str(-round(one_result[3] / 60 / 60 / 1000, 1))
        if one_result[3] > 0:
            your_timezone = "+" + str(round(one_result[3] / 60 / 60 / 1000, 1))
        if one_result[3] == 0:
            your_timezone = ""
        dbregdate_ms = one_result[4]
        prefix = guild_result[6]
        today_ms = int(unix_time_millis(datetime.datetime.utcnow()) + one_result[3])
        today = datetime.datetime.fromtimestamp((today_ms) / 1000) # 25200000 for UTC+7
        dbregdate = datetime.datetime.fromtimestamp(dbregdate_ms / 1000)
        settings_content = discord.Embed(title=str(localization[1][2][0]), description=str(localization[1][2][1]), color=embed_color)
        botlanguage_content = discord.Embed(title=str(localization[1][2][2][0]), description=str(localization[1][2][2][1]).format(prefix), color=embed_color)
        timezone_content = discord.Embed(title=str(localization[1][2][3][0]), description=str(localization[1][2][3][1]) + ": " + today.strftime("%Y-%m-%d **%H:%M:%S**") + " (UTC" + your_timezone + ")", color=embed_color)
        timezone_content.add_field(name=str(localization[1][2][3][2]), value=str(localization[1][2][3][3]), inline=True)
        timezone_content.add_field(name=str(localization[1][2][3][4]), value=str(localization[1][2][3][5]).format(prefix), inline=True)
        timezone_content.set_footer(text=str(localization[1][2][3][6]))
        msgcount_content = discord.Embed(title=str(localization[1][2][6][0]), description=str(localization[1][2][6][1]) + dbregdate.strftime("%Y-%m-%d") + ": **" + str(one_result[2]) + "**" + str(localization[1][2][6][2]), color=embed_color)
        msgcount_content.add_field(name=str(localization[1][2][6][3]), value=str(localization[1][2][6][4]), inline=True)
        msgcount_content.add_field(name=str(localization[1][2][6][5]), value=str(localization[1][2][6][6]).format(prefix), inline=True)
        customecolor_content = discord.Embed(title=str(localization[1][2][7][0]), color=embed_color)
        customecolor_content.add_field(name=str(localization[1][2][7][1]), value=str(localization[1][2][7][2]), inline=True)
        customecolor_content.add_field(name=str(localization[1][2][7][3]), value=str(localization[1][2][7][4]).format(prefix), inline=True)
        customprefix_content = discord.Embed(title=str(localization[1][2][8][0]), color=embed_color)
        customprefix_content.add_field(name=str(localization[1][2][8][1]), value="`" + botconfig['prefix'] + "`", inline=True)
        customprefix_content.add_field(name=str(localization[1][2][8][2]), value=str(localization[1][2][8][3]).format(prefix), inline=True)
        levelsystem_content = discord.Embed(title=str(localization[1][2][9][0]), color=embed_color)
        levelsystem_content.add_field(name=str(localization[1][2][9][1]), value=str(localization[1][2][9][2]), inline=True)
        levelsystem_content.add_field(name=str(localization[1][2][9][3]), value=str(localization[1][2][9][4]).format(prefix), inline=True)
        welcomemsg_content = discord.Embed(title=str(localization[1][2][10][0]), color=embed_color)
        welcomemsg_content.add_field(name=str(localization[1][2][10][1]), value=str(localization[1][2][10][2]), inline=False)
        welcomemsg_content.add_field(name=str(localization[1][2][10][3]), value=str(localization[1][2][10][4]).format(prefix).replace('╭', '{').replace('╮', '}'), inline=False)
        welcomemsg_content.add_field(name=str(localization[1][2][10][5]), value=str(localization[1][2][10][6]), inline=False)
        msg = await message.channel.send(embed=settings_content)
        await msg.add_reaction(emoji="🗣️")
        await msg.add_reaction(emoji="🕓")
        await msg.add_reaction(emoji="🗨️")
        await msg.add_reaction(emoji="🌈")
        await msg.add_reaction(emoji="🚩")
        await msg.add_reaction(emoji="🏆")
        await msg.add_reaction(emoji="👋")
        @bot.event
        async def on_reaction_add(reaction, user):
            channel = reaction.message.channel
            if reaction.emoji == "🗣️" and user.id != bot.user.id:
               await msg.edit(embed=botlanguage_content)
            if reaction.emoji == "🕓" and user.id != bot.user.id:
               await msg.edit(embed=timezone_content)
            if reaction.emoji == "🗨️" and user.id != bot.user.id:
               await msg.edit(embed=msgcount_content)
            if reaction.emoji == "🌈" and user.id != bot.user.id:
               await msg.edit(embed=customecolor_content)
            if reaction.emoji == "🚩" and user.id != bot.user.id:
               await msg.edit(embed=customprefix_content)
            if reaction.emoji == "🏆" and user.id != bot.user.id:
               await msg.edit(embed=levelsystem_content)
            if reaction.emoji == "👋" and user.id != bot.user.id:
               await msg.edit(embed=welcomemsg_content)
