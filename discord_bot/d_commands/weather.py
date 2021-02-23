async def weather_cmd(bot, discord, sqlite3, message, botconfig, os, platform, datetime, one_result, localization, embed_color, requests):
  args = message.content.split();
  city_id = 0
  no_args = discord.Embed(title=localization[1][13][0], description=localization[1][11][14], color=embed_color)
  if " ".join(args[1:]) == "" or " ".join(args[1:]) == " " or " ".join(args[1:]) == None:
    return await message.channel.send(embed=no_args)
  try:
    res = requests.get("http://api.openweathermap.org/data/2.5/find",
                 params={'q': " ".join(args[1:]), 'type': 'like', 'units': 'metric', 'APPID': os.environ['OPENWMAPT']})
    data = res.json()
    city_id = data['list'][0]['id']
  except Exception as e:
    weather_content = discord.Embed(title=localization[1][11][11], description=localization[1][11][12], color=embed_color)
    return await message.channel.send(embed=weather_content)
  try:
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                 params={'id': city_id, 'units': 'metric', 'lang': localization[1][11][10], 'APPID': os.environ['OPENWMAPT']})
    res2 = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                           params={'id': city_id, 'units': 'metric', 'lang': localization[1][11][10], 'cnt': '5', 'APPID': os.environ['OPENWMAPT']})
    data = res.json()
    forecast_five_days_json = res2.json()
    forecast_str = ""
    for i in forecast_five_days_json['list']:
      forecast_str += datetime.datetime.fromtimestamp(i['dt']).strftime("%m-%d %H:%M") + ' | ' + '{0:+3.0f}°C'.format(i['main']['temp']) + " | " + i['weather'][0]['description'] + "\n"
    weather_content = discord.Embed(title=localization[1][11][0] + data['name'] + ", " + data['sys'][
    'country'], description=data['weather'][0]['description'][0].upper() + "".join(data['weather'][0]['description'][1:]), color=embed_color)
    weather_content.add_field(name=str(localization[1][11][1]), value=str(localization[1][11][2]) + str(data['main']['temp_min']) + "°C" + str(localization[1][11][3])  + str(data['main']['temp']) + "°C" + str(localization[1][11][4]) + str(data['main']['temp_max']) + "°C", inline=True)
    weather_content.add_field(name=str(localization[1][11][5]), value=str(data['wind']['speed']) + localization[1][11][6], inline=True)
    weather_content.add_field(name=str(localization[1][11][7]), value=str(data['main']['humidity']) + "%", inline=True)
    weather_content.add_field(name=str(localization[1][11][8]), value="```" + forecast_str + "```", inline=False)
    weather_content.set_footer(text=localization[1][11][9])
    await message.channel.send(embed=weather_content)
  except Exception as e:
    weather_content = discord.Embed(title=localization[1][11][11], description=localization[1][11][12], color=embed_color)
    await message.channel.send(embed=weather_content)