import random


async def help_cmd(bot, discord, message, botconfig, platform, os, datetime, one_result, localization, embed_color, guild_result):
	if localization[0] == "Russian":
		tips = [
		    'С помощью VisionOne можно проводить голосования?',
		    'Все наши ссылки находятся в `info`?',
		    'Узнать погоду можно в `weather`?',
		    'Просмотреть рандомные фото можно в `photo`? Вдруг пригодится поставить обои на свой рабочий стол?',
		    'Поступили две новости в `=tnews`?',
        'Игра "Магический шар" генерирует случайные ответы трех типов (да/нет/хз) для заданного вопроса? Обратите внимание, что совпадения случайны, поэтому воспринимайте как игру, а не как реальность.',
        'Автор {0} (`{1}`) начал строить своего предшественника под названием Highflash в декабре 2018 г. на discord.js (JavaScript).'.format(botconfig['name'], bot.get_user(int(botconfig['owner'])).name + "#" + str(bot.get_user(int(botconfig['owner'])).discriminator)),
        'Можно послушать музыку в `=music`? В этой команде присутствует поддержка плейлиста, но такая своеобразная.'
		]
	else:
		tips = [
      'All our links on `info` command',
      'Starting with VisionOne 01R8 (January 21, 2021), has it become possible to change prefixes, get experiences for messages, etc?',
      'Author {0} (`{1}`) started building his predecessor called Dmitryev Bot (now Highflash) in December 2018 on discord.js (JavaScript).'.format(botconfig['name'], bot.get_user(int(botconfig['owner'])).name + "#" + str(bot.get_user(int(botconfig['owner'])).discriminator))
    ]
	try:
		if guild_result[6] == botconfig['prefix']:
			custom_prefix = ""
		else:
			custom_prefix = " `" + guild_result[6] + "`"
		if custom_prefix == None:
			custom_prefix = "="
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
