async def post(bot, discord, message, botconfig, platform, os, datetime, one_result, localization, args, unix_time_millis, connection, cursor):

    try:
        subargs = args[2]
    except:
        # posterr_content = discord.Embed(title=bot_detector + str(localization[1][3][0]) + str(a_user), description="**ID: **" + str(a_user.id), color=botconfig['accent1']) 
        # *** UNDER CONSTRUCTION ***
