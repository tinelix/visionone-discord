async def help_cmd(bot, discord, message, botconfig, platform, os, datetime, one_result, localization, embed_color):
        help_content = discord.Embed(title=botconfig['name'], description=str(botconfig['name'] + localization[1][0][0]), color=embed_color)
        help_content.add_field(name=str(localization[1][0][1][0]), value=str(localization[1][0][1][1]), inline=True)
        help_content.add_field(name=str(localization[1][0][2][0]), value=str(localization[1][0][2][1]), inline=True)
        help_content.add_field(name=str(localization[1][0][3][0]), value=str(localization[1][0][3][1]), inline=True)
        help_content.add_field(name=str(localization[1][0][4][0]), value=str(localization[1][0][4][1]), inline=True)
        help_content.set_footer(text='Ver. ' + botconfig['version'])
        await message.channel.send(embed=help_content)
