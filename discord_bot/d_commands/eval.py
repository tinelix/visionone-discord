async def eval_cmd(bot, discord, message, botconfig, os, platform, datetime, one_result, localization, en_US, guild_result, intents, embed_color):
        args = message.content.split();
        accessdenied_msg = discord.Embed(title="Доступ запрещен", description="Эта команда защищена владельцем бота, поэтому она недоступна.", color=botconfig['accent2'])
        eval_content = discord.Embed(title="Определение качества кода", color=botconfig['accent1'])
        eval_content.add_field(name="Листинг", value="```py\n" + " ".join(args[1:]) + "```", inline=False)
        if str(message.author.id) != botconfig['owner']:
            return await message.channel.send(embed=accessdenied_msg)
        try:
            result = str(eval(" ".join(args[1:])))
        except Exception as e:
            result = "Обнаружено исключение!\n" + str(e)
        finally:
          try:
            eval_content.add_field(name="Результат", value="```" + result + "```", inline=False)
            await message.channel.send(embed=eval_content) 
          except:
            await message.channel.send("```" + result + "```")
