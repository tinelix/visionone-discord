async def state_cmd(bot, discord, sqlite3, message, botconfig, os, platform, datetime, one_result, localization, embed_color, connection, cursor, cpuinfo, psutil):
        data_collecting_content = discord.Embed(title=str(localization[1][1][0]), description="**" + str(localization[1][1][1]) + ":** " + str(round(bot.latency * 1000, 2)) + str(localization[1][1][2]) + "\n\n" + str(localization[1][1][18]), color=embed_color)
        msg = await message.channel.send(embed=data_collecting_content)
        usersdb = cursor.execute('SELECT * FROM users').rowcount
        usersdb_count = cursor.fetchall()
        guildsdb = cursor.execute('SELECT * FROM guilds').rowcount
        guildsdb_count = cursor.fetchall()
        if cpuinfo.get_cpu_info()['count'] < 2:
          cores_amount = str(cpuinfo.get_cpu_info()['count']) + localization[1][1][9]
        elif cpuinfo.get_cpu_info()['count'] < 5:
          cores_amount = str(cpuinfo.get_cpu_info()['count']) + localization[1][1][10]
        else:
          cores_amount = str(cpuinfo.get_cpu_info()['count']) + localization[1][1][11]

        if psutil.virtual_memory().available < 1024:
          ram_available = str(round(psutil.virtual_memory().available / 1024, 2)) + localization[1][1][14] + localization[1][1][17]
        elif psutil.virtual_memory().available < 1048576 and psutil.virtual_memory().available >= 1024:
          ram_available = str(round(psutil.virtual_memory().available / 1024 / 1024, 2)) + localization[1][1][15] + localization[1][1][17]
        else:
          ram_available = str(round(psutil.virtual_memory().available / 1024 / 1024 / 1024, 2)) + localization[1][1][16] + localization[1][1][17]

        if psutil.virtual_memory().total < 1024:
          ram_total = str(round(psutil.virtual_memory().total / 1024, 2)) + localization[1][1][14]
        elif psutil.virtual_memory().total < 1048576  and psutil.virtual_memory().total >= 1024:
          ram_total = str(round(psutil.virtual_memory().total / 1024 / 1024, 2)) + localization[1][1][15]
        else:
          ram_total = str(round(psutil.virtual_memory().total / 1024 / 1024 / 1024, 2)) + localization[1][1][16]
        state_content = discord.Embed(title=str(localization[1][1][0]), description="**" + str(localization[1][1][1]) + ":** " + str(round(bot.latency * 1000, 2)) + str(localization[1][1][2]), color=embed_color)
        state_content.add_field(name=str(localization[1][1][3]), value=platform.uname()[0] + " " + platform.uname()[2] + " (" + platform.uname()[3] + ")", inline=False)
        state_content.add_field(name=str(localization[1][1][4]), value=str(cpuinfo.get_cpu_info()['brand_raw']) + " (" + cores_amount + ", " + str(round(cpuinfo.get_cpu_info()['hz_advertised'][0] / 1000000, 2)) + localization[1][1][12] + ")", inline=False)
        state_content.add_field(name=str(localization[1][1][13]), value=ram_available + " / " + ram_total, inline=True)
        state_content.add_field(name=str(localization[1][1][5]), value=platform.python_version(), inline=True)
        state_content.add_field(name=str(localization[1][1][6]), value=platform.python_build()[1], inline=True)
        state_content.add_field(name=str(localization[1][1][7]), value="**discord.py:** " + discord.__version__ + "\n**SQLite3 library:** " + sqlite3.sqlite_version + "\n**Vision bot:** " + botconfig['version'], inline=True)
        state_content.add_field(name=str(localization[1][1][8]), value="🏠 " + str(len(bot.guilds)) + " | 👥 " + str(len(bot.users)) + " | 🗃 " + str(len(usersdb_count) + len(guildsdb_count)), inline=True)
        await msg.edit(embed=state_content)