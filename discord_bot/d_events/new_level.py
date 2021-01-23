import random
import math

async def message_to_xp(bot, discord, message, botconfig, platform, os, datetime, one_result, guild_result, localization, unix_time_millis, embed_color, connection, cursor, prefix):
    if len(message.content) > 10: #за каждое сообщение длиной > 10 символов...
        expi=one_result[8]+random.randint(5, 40) #к опыту добавляется случайное число
        cursor.executemany('UPDATE users SET scores=? where userid=?', [(expi, message.author.id)])
        try:
            lvch=expi/(one_result[9] * (50 + (one_result[9] * 10)))
        except ZeroDivisionError as zerodivide_err:
            lvch=1
        connection.commit()
        lv=math.floor(lvch)
        print(((one_result[9]) * (50 + ((one_result[9]) * 10))) * (one_result[9] + 1))
        if one_result[9] < lv:
            if message.content.startswith(botconfig['prefix']) is False and message.content.startswith(guild_result[6]) is False and one_result[9] > 0:
            	new_level_msg = discord.Embed(title=localization[1][18][0], description=str(localization[1][18][1]).format('<@' + str(message.author.id) + '>', lv), color=embed_color)
            	await message.channel.send(embed=new_level_msg)
            cursor.executemany('UPDATE users SET level=? where userid=?', [(lv, message.author.id)])
            connection.commit()
