async def guilds_cmd(bot, discord, message, botconfig, os, platform, datetime, one_result, localization, guild_result, intents, embed_color):
        accessdenied_msg = discord.Embed(title="Доступ запрещен", description="Эта команда защищена владельцем бота, поэтому она недоступна.", color=botconfig['accent2'])
        if str(message.author.id) != botconfig['owner']:
            return await message.channel.send(embed=accessdenied_msg)
        try:
          guild_list = ""
          for bot_guild in bot.guilds:
            guild_list += str(bot.guilds.index(bot_guild) + 1) + ". " + str(bot_guild.name) + " | Members: " + str(bot_guild.member_count) + "\n"
        except Exception as e:
            guild_list = "Обнаружено исключение!\n" + str(e)
        finally:
          await message.channel.send("```" + guild_list + "```")