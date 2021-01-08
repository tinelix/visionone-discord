# Source: https://github.com/justinbaur/m8b (MIT / X11 License)
import random

async def crystball_cmd(bot, discord, sqlite3, message, botconfig, os, platform, datetime, one_result, localization, embed_color, requests):
  args = message.content.split();
  no_args = discord.Embed(title=localization[1][12][0], description=localization[1][12][5], color=embed_color)
  if " ".join(args[1:]) == "" or " ".join(args[1:]) == " " or " ".join(args[1:]) == None:
    return await message.channel.send(embed=no_args)
  if localization[0] == "English":
    response_list = ["As I see it, yes", "Yes", "No", "Very likely", "Not even close", "Maybe", "Very unlikely", "Gino's mom told me yes", "Gino's mom told me no", "Ask again later", "Better not tell you now", "Concentrate and ask again", "Don't count on it", " It is certain", "My sources say no", "Outlook good", "You may rely on it", "Very Doubtful", "Without a doubt", 'I don\'t know.', 'Idk']
  elif localization[0] == "Russian":
    response_list = ["Логично.", "Да.", "Нет.", "Вероятно.", "Мне что-то слабо верится.", "Может быть.", "Маловерятно.", "Мне сказали \"да\".", "Мне сказали \"нет\".", "Повтори-ка...", "Я лучше промолчу.", "Сконцетрируйтесь и спросите еще раз.", "Не рассчитывайте на это.", "Это точно.", "Ничего подобного.", "Я не знаю.", "Конечно.", "Хз.", "Но это не точно", 'Откуда я знаю?']
  
  lucky_num = random.randint(0,len(response_list) - 1)  

  crystball_content = discord.Embed(title=localization[1][12][0], color=embed_color)
  crystball_content.add_field(name=localization[1][12][1], value=" ".join(args[1:]), inline=False)
  crystball_content.add_field(name=localization[1][12][2], value=response_list[lucky_num], inline=False)
  crystball_content.set_footer(text=localization[1][12][3])
  await message.channel.send(embed=crystball_content)


