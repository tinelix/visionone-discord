from .tnews_list import tnews_list
async def get_tnews(bot, discord, message, botconfig, platform, os, datetime, one_result, localization, args, unix_time_millis, connection, cursor, embed_color):
    news_title = ""
    news_text = ""
    tnews_content = discord.Embed(title=localization[1][6][0], description=localization[1][6][1] + tnews_list['title']['one'] + "\n" + tnews_list['title']['two'], color=embed_color)
    tnews_content.set_footer(text=tnews_list['footer'])
    msg = await message.channel.send(embed=tnews_content)
    await msg.add_reaction(emoji="1⃣")
    await msg.add_reaction(emoji="2⃣")
    @bot.event
    async def on_reaction_add(reaction, user):
        channel = reaction.message.channel
        if reaction.emoji == "1⃣" and user.id != bot.user.id:
            news_title = tnews_list['title']['non-unicode']['one']
            news_text = tnews_list['news']['one']
            tnews_text_content = discord.Embed(title=news_title, description=news_text, color=embed_color)
            tnews_text_content.set_image(url=tnews_list['images']['one'])
            await msg.edit(embed=tnews_text_content)
        if reaction.emoji == "2⃣" and user.id != bot.user.id:
            news_title = tnews_list['title']['non-unicode']['two']
            news_text = tnews_list['news']['two']
            tnews_text_content = discord.Embed(title=news_title, description=news_text, color=embed_color)
            tnews_text_content.set_image(url=tnews_list['images']['two'])
            await msg.edit(embed=tnews_text_content)
        if reaction.emoji == "3⃣" and user.id != bot.user.id:
            news_title = tnews_list['title']['non-unicode']['three']
            news_text = tnews_list['news']['three']
            tnews_text_content = discord.Embed(title=news_title, description=news_text, color=embed_color)
            tnews_text_content.set_image(url=tnews_list['images']['three'])
            await msg.edit(embed=tnews_text_content)
        if reaction.emoji == "4️⃣" and user.id != bot.user.id:
            news_title = tnews_list['title']['non-unicode']['four']
            news_text = tnews_list['news']['four']
            tnews_text_content = discord.Embed(title=news_title, description=news_text, color=embed_color)
            tnews_text_content.set_image(url=tnews_list['images']['four'])
            await msg.edit(embed=tnews_text_content)        
