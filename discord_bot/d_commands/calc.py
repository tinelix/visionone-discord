async def calc_cmd(bot, discord, message, botconfig, os, platform, datetime, one_result, localization, numexpr):
        args = message.content.split();
        no_args = discord.Embed(title=localization[1][9][0], description=localization[1][9][4], color=botconfig['accent1'])
        no_args.add_field(name=localization[1][9][6], value=localization[1][9][7], inline=False)
        if " ".join(args[1:]) == "" or " ".join(args[1:]) == " " or " ".join(args[1:]) == None:
            return await message.channel.send(embed=no_args)
        calc_content = discord.Embed(title=localization[1][9][0], color=botconfig['accent1'])
        calc_content.add_field(name=localization[1][9][1], value="```py\n" + " ".join(args[1:]) + "```", inline=False)
        try:
            result = str(numexpr.evaluate(" ".join(args[1:])))
        except Exception as e:
            result = localization[1][9][3] + str(e)
        finally:
            calc_content.add_field(name=localization[1][9][2], value="```" + result + "```", inline=False)
            calc_content.add_field(name=localization[1][9][6], value=localization[1][9][7], inline=False)
            await message.channel.send(embed=calc_content)  
