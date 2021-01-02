async def cooldown(bot, message, one_result, guild_result, connection, cursor, unix_time_millis, ru_RU, en_US):
    await message.add_reaction(emoji="⌛")
    
