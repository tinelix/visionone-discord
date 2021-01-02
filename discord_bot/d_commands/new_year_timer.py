async def new_year_timer_cmd(bot, discord, message, botconfig, os, platform, datetime, one_result, localization, unix_time_millis):
    new_year = datetime.datetime.strptime('2021-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
    try:
      timer = (-unix_time_millis(datetime.datetime.utcnow())) + unix_time_millis(new_year) - one_result[3]
    except:
      pass
    try:
      timer_moscow = (-unix_time_millis(datetime.datetime.utcnow())) + unix_time_millis(new_year) - 10800000
    except:
      pass
    try:
      timer_chelyabinsk = (-unix_time_millis(datetime.datetime.utcnow())) + unix_time_millis(new_year) - 18000000
    except:
      pass
    try:
      timer_barnaul = (-unix_time_millis(datetime.datetime.utcnow())) + unix_time_millis(new_year) - 25200000
    except:
      pass
    try:
      timer_ulan_ude = (-unix_time_millis(datetime.datetime.utcnow())) + unix_time_millis(new_year) - 28800000
    except:
      pass
    try:
      timer_d = str(datetime.datetime.fromtimestamp(timer / 1000).strftime("%d"))
    except:
      pass
    try:
      timer_mc_d = str(datetime.datetime.fromtimestamp(timer_moscow / 1000).strftime("%d"))
    except:
      pass
    try:
      timer_cb_d = str(datetime.datetime.fromtimestamp(timer_chelyabinsk / 1000).strftime("%d"))
    except:
      pass
    try:
      timer_bn_d = str(datetime.datetime.fromtimestamp(timer_barnaul / 1000).strftime("%d"))
    except:
      pass
    try:
      timer_uu_d = str(datetime.datetime.fromtimestamp(timer_ulan_ude / 1000).strftime("%d"))
    except:
      pass
    try:
      timer_h = str(datetime.datetime.fromtimestamp(timer / 1000).strftime("%H"))
    except:
      pass
    try:    
      timer_mc_h = str(datetime.datetime.fromtimestamp(timer_moscow / 1000).strftime("%H"))
    except:
      pass
    try:
      timer_cb_h = str(datetime.datetime.fromtimestamp(timer_chelyabinsk / 1000).strftime("%H"))
    except:
      pass
    try:    
      timer_bn_h = str(datetime.datetime.fromtimestamp(timer_barnaul / 1000).strftime("%H"))
    except:
      pass
    try:
      timer_uu_h = str(datetime.datetime.fromtimestamp(timer_ulan_ude / 1000).strftime("%H"))
    except:
      pass
    try:
      timer_m = str(datetime.datetime.fromtimestamp(timer / 1000).strftime("%M"))
    except:
      pass
    try:
      timer_mc_m = str(datetime.datetime.fromtimestamp(timer_moscow / 1000).strftime("%M"))
    except:
      pass
    try:
      timer_cb_m = str(datetime.datetime.fromtimestamp(timer_chelyabinsk / 1000).strftime("%M"))
    except:
      pass
    try:
      timer_bn_m = str(datetime.datetime.fromtimestamp(timer_barnaul / 1000).strftime("%M"))
    except:
      pass
    try:
      timer_uu_m = str(datetime.datetime.fromtimestamp(timer_ulan_ude / 1000).strftime("%M"))
    except:
      pass
    try:
      timer_s = str(datetime.datetime.fromtimestamp(timer / 1000).strftime("%S"))
    except:
      pass
    try:
      timer_mc_s = str(datetime.datetime.fromtimestamp(timer_moscow / 1000).strftime("%S"))
    except:
      pass
    try:
      timer_cb_s = str(datetime.datetime.fromtimestamp(timer_chelyabinsk / 1000).strftime("%S"))
    except:
      pass
    try:
      timer_bn_s = str(datetime.datetime.fromtimestamp(timer_barnaul / 1000).strftime("%S"))
    except:
      pass
    try:
      timer_uu_s = str(datetime.datetime.fromtimestamp(timer_ulan_ude / 1000).strftime("%S"))
    except:
      pass
    localization_days = localization[1][7][1]
    localization_hours = localization[1][7][2]
    localization_minutes = localization[1][7][3]
    localization_seconds = localization[1][7][4]
    localization_seconds_2 = localization[1][7][5]
    try:
      moscow = str(int(timer_mc_d) - 1) + localization_days + timer_mc_h + localization_hours  + timer_mc_m + localization_minutes + timer_mc_s + localization_seconds_2 + str(localization[1][7][6])
    except:
      moscow = localization[1][7][11]
    try:
      chelyabinsk = str(int(timer_cb_d) - 1) + localization_days + timer_cb_h + localization_hours + timer_cb_m + localization_minutes + timer_cb_s + localization_seconds_2 + str(localization[1][7][7])
    except:
      chelyabinsk = localization[1][7][12]
    try:
      barnaul = str(int(timer_bn_d) - 1) + localization_days + timer_bn_h + localization_hours + timer_bn_m + localization_minutes + timer_bn_s + localization_seconds_2 + str(localization[1][7][8])
    except:
      barnaul = localization[1][7][13]
    try:
      ulan_ude = str(int(timer_uu_d) - 1) + localization_days + timer_uu_h + localization_hours + timer_uu_m + localization_minutes + timer_uu_s + localization_seconds_2 + str(localization[1][7][9])
    except:
      ulan_ude = localization[1][7][14]
    new_year_timer_content = discord.Embed(title=localization[1][7][0], description="```" + str(int(timer_d) - 1) + localization_days + timer_h + localization_hours + timer_m + localization_minutes + timer_s + localization_seconds + "```\n", color=botconfig['accent1'])
    new_year_timer_content.add_field(name=str(localization[1][7][10]), value=moscow + "\n" + chelyabinsk + "\n" + barnaul + "\n" + ulan_ude, inline=False)
    await message.channel.send(embed=new_year_timer_content)
