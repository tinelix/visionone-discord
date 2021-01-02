async def add_guild_to_blacklist(bot, discord, message, botconfig, platform, os, datetime, one_result, localization, args, unix_time_millis, connection, cursor):
    accessdenied_msg = discord.Embed(title="Доступ запрещен", description="Эта команда защищена владельцем бота, поэтому она недоступна.", color=botconfig['accent2'])
    if str(message.author.id) != botconfig['owner']:
        return await message.channel.send(embed=accessdenied_msg)
    try:
      subargs = args[2]
    except:  
        subargs = ""
    try:
        blacklist_guild = [(subargs,)]
        cursor.executemany("INSERT OR REPLACE INTO blacklist_guilds VALUES(?);", blacklist_guild)
        connection.commit()
        try:
            await bot.get_guild(int(subargs)).leave()
        except:
            pass
        await message.channel.send("Ok")
    except Exception as e:
        await message.channel.send(e)
        print(subargs.isdigit())
