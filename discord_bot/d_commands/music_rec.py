from requests import get
from youtube_search import YoutubeSearch as ytsearch
import sqlite3

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
    except Error as e:
        print(f"SQLite Database | The error '{e}' occurred")

    return connection

YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}


async def yt_search(bot, discord, sqlite3, message, botconfig, os, platform, datetime, one_result, localization, embed_color, requests):
		args = message.content.split();
		results_list = ""
		emoji_number = {
      		'0': '0️⃣',
      		'1': '1️⃣',
      		'2': '2️⃣',
      		'3': '3️⃣',
      		'4': '4️⃣',
      		'5': '5️⃣',
      		'6': '6️⃣',
      		'7': '7️⃣',
      		'8': '8️⃣',
      		'9': '9️⃣',
      		'0️⃣': 0,
      		'1️⃣': 1,
      		'2️⃣': 2,
      		'3️⃣': 3,
      		'4️⃣': 4,
      		'5️⃣': 5,
      		'6️⃣': 6,
      		'7️⃣': 7,
      		'8️⃣': 8,
      		'9️⃣': 9
    	}
		results = ytsearch(" ".join(args[1:]), max_results=9).to_dict()
		print(results)
		results_text = ""
		for video in results:
			results_text += emoji_number[str(results.index(video) + 1)] + " **{0}**\n".format(video['title'])
		yt_search_results = discord.Embed(title=localization[1][21][0], color=embed_color)
		yt_search_results.add_field(name=localization[1][21][3], value=results_text)
		msg = await message.channel.send(embed=yt_search_results)
		for video in results:
			await msg.add_reaction(emoji=emoji_number[str(results.index(video) + 1)])
		#print(video_infos['entries'])
		@bot.event
		async def on_reaction_add(reaction, user):
			channel = reaction.message.channel
			if reaction.emoji == emoji_number[] and user.bot != True:
