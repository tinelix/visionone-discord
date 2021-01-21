import random

async def photo_cmd(bot, discord, message, botconfig, os, platform, datetime, one_result, localization, unix_time_millis, unsplash, time_diff, bot_data_result, cursor, connection, embed_color, reddit, prefix):
  args = message.content.split();
  try:
    if " ".join(args[1:]) == "" or " ".join(args[1:]) == " " or " ".join(args[1:]) == None:
      no_args = discord.Embed(title=localization[1][8][0], description=str(localization[1][8][5]).format(prefix), color=embed_color)
      return await message.channel.send(embed=no_args)
    if args[1] == "-u":
      if time_diff >= 3600000:
        bot_data = [(0, 0)]
        cursor.executemany("INSERT OR REPLACE INTO bot_data VALUES(?, ?)", bot_data)
        connection.commit()
        if bot_data_result[1] >= 20:
          photo_changed = discord.Embed(title=localization[1][8][3], description=localization[1][8][4], color=embed_color)
          return await message.channel.send(embed=photo_changed)
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
            photo_changed = discord.Embed(title=localization[1][8][0], color=embed_color)
            photo_changed.add_field(name=str(localization[1][8][1]), value=u_photo2.user.name + " [(Unsplash)](" + u_photo2.user.links.html + ")", inline=True)
            photo_changed.add_field(name=str(localization[1][8][2]), value=str(u_photo2.likes), inline=True)
            photo_changed.set_image(url=u_photo2.urls.raw)
            await msg.edit(embed=photo_changed)
          else:
            photo_changed = discord.Embed(title=localization[1][8][3], description=localization[1][8][4], color=embed_color)
            await msg.edit(embed=photo_changed)
    elif args[1] == "-r":
          subreddits = ['analog', 'wallpaper', 'photo']
          random_sr = subreddits[random.randint(0,len(subreddits) - 1)]
          subreddit = reddit.subreddit(random_sr)
          print(subreddit)
          photo = subreddit.random()
          photo_content = discord.Embed(title=localization[1][8][0], color=embed_color)
          photo_content.add_field(name=str(localization[1][8][1]), value="r/" + str(subreddit.display_name) + " [(Reddit)](https://reddit.com/" + str(subreddit.display_name) + ")", inline=True)
          photo_content.set_image(url=photo.url)
          msg = await message.channel.send(embed=photo_content)
          await msg.add_reaction(emoji="🎲")
          @bot.event
          async def on_reaction_add(reaction, user):
            if reaction.emoji == "🎲" and user.id != bot.user.id:
              subreddits = ['analog', 'wallpaper', 'photo']
              random_sr = subreddits[random.randint(0,len(subreddits) - 1)]
              subreddit = reddit.subreddit(random_sr)
              photo = subreddit.random()
              photo_changed = discord.Embed(title=localization[1][8][0], color=embed_color)
              photo_changed.add_field(name=str(localization[1][8][1]), value="r/" + str(subreddit.display_name) + " [(Reddit)](https://reddit.com/r/" + str(subreddit.display_name) + ")", inline=True)
              photo_changed.set_image(url=photo.url)
              await msg.edit(embed=photo_changed)
  except:
    no_args = discord.Embed(title=localization[1][8][0], description=str(localization[1][8][5]).format(prefix), color=embed_color)
    pass
    return await message.channel.send(embed=no_args)
