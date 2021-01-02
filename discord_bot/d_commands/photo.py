async def photo_cmd(bot, discord, message, botconfig, os, platform, datetime, one_result, localization, unix_time_millis, unsplash, time_diff, bot_data_result, cursor, connection, embed_color):
    try:
        bot_data = [(0, bot_data_result[1] + 1)]
        cursor.executemany("INSERT OR REPLACE INTO bot_data VALUES(?, ?)", bot_data)
        connection.commit()
        cursor.execute("SELECT * FROM bot_data WHERE number='" + str(0) + "';")
        bot_data_result2 = cursor.fetchone()
    except:
        pass
    u_random = unsplash.photo.random()
    u_photo = unsplash.photo.get(u_random[0].id)
    photo_content = discord.Embed(title=localization[1][8][0], color=embed_color)
    photo_content.add_field(name=str(localization[1][8][1]), value=u_photo.user.name + " [(Unsplash)](" + u_photo.user.links.html + ")", inline=True)
    photo_content.add_field(name=str(localization[1][8][2]), value=str(u_photo.likes), inline=True)
    photo_content.set_image(url=u_random[0].urls.raw)
    msg = await message.channel.send(embed=photo_content)
    await msg.add_reaction(emoji="🎲")
    @bot.event
    async def on_reaction_add(reaction, user):
        channel = reaction.message.channel
        try:
            cursor.execute("SELECT * FROM bot_data WHERE number='" + str(0) + "';")
            bot_data_result3 = cursor.fetchone()
            bot_data2 = [(0, bot_data_result3[1] + 1)]
            cursor.executemany("INSERT OR REPLACE INTO bot_data VALUES(?, ?)", bot_data2)
            connection.commit()
        except:
            pass
        if reaction.emoji == "🎲" and user.id != bot.user.id:
          if bot_data_result3[1] < 20:
            u_random2 = unsplash.photo.random()
            u_photo2 = unsplash.photo.get(u_random2[0].id)
            photo_changed = discord.Embed(title=localization[1][8][0], color=botconfig['accent1'])
            photo_changed.add_field(name=str(localization[1][8][1]), value=u_photo2.user.name + " [(Unsplash)](" + u_photo2.user.links.html + ")", inline=True)
            photo_changed.add_field(name=str(localization[1][8][2]), value=str(u_photo2.likes), inline=True)
            photo_changed.set_image(url=u_photo2.urls.raw)
            await msg.edit(embed=photo_changed)
          else:
            photo_changed = discord.Embed(title=localization[1][8][3], description=localization[1][8][4], color=botconfig['accent1'])
            await msg.edit(embed=photo_changed)
