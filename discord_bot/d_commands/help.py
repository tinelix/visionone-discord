import random


async def help_cmd(bot, discord, message, botconfig, platform, os, datetime, one_result, localization, embed_color, guild_result):
	if localization[0] == "Russian":
		tips = [
		    'Для просмотра авторской информационной программы "Новости Тинеликса" достаточно написать команду `tnews`?',
		    'Все наши ссылки находятся в `info`?',
		    'Узнать погоду можно в `weather`?',
		    'Просмотреть рандомные фото можно в `photo`? Вдруг пригодится поставить обои на свой рабочий стол?',
		    'Что в версии 01R5 (9 января 2020 г.) появилась команда `codec` для зашифровки и расшифровки текста?'
		]
	else:
		tips = ['All our links on `info` command']
	try:
		if guild_result[6] == botconfig['prefix']:
			custom_prefix = ""
		else:
			custom_prefix = " `" + guild_result[6] + "`"
	except Exception as e:
		print(e)
	lucky_num = random.randint(0, len(tips) - 1)
	help_content = discord.Embed(description=str(botconfig['name'] + localization[1][0][0]).format(botconfig['prefix'], custom_prefix, tips[lucky_num]),color=embed_color)
	help_content.add_field(name=str(localization[1][0][1][0]),value=str(localization[1][0][1][1]),inline=True)
	help_content.add_field(name=str(localization[1][0][2][0]),value=str(localization[1][0][2][1]),inline=True)
	help_content.add_field(name=str(localization[1][0][3][0]),value=str(localization[1][0][3][1]),inline=True)
	help_content.add_field(name=str(localization[1][0][4][0]),value=str(localization[1][0][4][1]),inline=True)
	help_content.set_footer(text='Ver. ' + botconfig['version'])
	await message.channel.send(embed=help_content)
