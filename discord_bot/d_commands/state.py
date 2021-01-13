async def state_cmd(bot, discord, sqlite3, message, botconfig, os, platform, datetime, one_result, localization, embed_color, connection, cursor):
        usersdb = cursor.execute('SELECT * FROM users').rowcount
        usersdb_count = cursor.fetchall()
        state_content = discord.Embed(title=str(localization[1][1][0]), color=embed_color, inline=True)
        state_content.add_field(name=str(localization[1][1][1]), value=str(round(bot.latency * 1000, 2)) + str(localization[1][1][2]), inline=True) 
        state_content.add_field(name=str(localization[1][1][3]), value=platform.uname()[0] + " " + platform.uname()[2] + " (" + platform.uname()[3] + ")", inline=True)
        state_content.add_field(name=str(localization[1][1][4]), value=platform.processor(), inline=True)
        state_content.add_field(name=str(localization[1][1][5]), value=platform.python_version(), inline=True)
        state_content.add_field(name=str(localization[1][1][6]), value=platform.python_build()[1], inline=True)
        state_content.add_field(name=str(localization[1][1][7]), value="**discord.py:** " + discord.__version__ + "\n**SQLite3 library:** " + sqlite3.sqlite_version + "\n**Vision bot:** " + botconfig['version'], inline=True)
        state_content.add_field(name=str(localization[1][1][8]), value="🏠 " + str(len(bot.guilds)) + " | 👥 " + str(len(bot.users)) + " | 🗃 " + str(len(usersdb_count)), inline=True)
        await message.channel.send(embed=state_content)