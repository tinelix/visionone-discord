async def help_cmd(bot, discord, message, botconfig, platform, os, datetime, one_result, localization, embed_color):
        help_content = discord.Embed(title=botconfig['name'], description=str(botconfig['name'] + localization[1][0][0]), color=embed_color)
        help_content.set_footer(text='Ver. ' + botconfig['version'])
        help_content.set_image(url='https://media.discordapp.net/attachments/787270057952542720/789065309554343936/bandicam_2020-12-17_16-43-41-557.png')
        await message.channel.send(embed=help_content)
