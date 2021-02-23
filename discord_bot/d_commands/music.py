from requests import get
import pafy
from youtube_search import YoutubeSearch as ytsearch
import sqlite3
import tempfile
import os
import asyncio

def sort_asc(item):
	return item[0]

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
    except Exception as e:
        print(f"SQLite Database | The error '{e}' occurred")

    return connection


async def yt_search(bot, discord, sqlite3, message, botconfig, os, platform, datetime, one_result, localization, embed_color, prefix, requests):
		dl_status = [0, 0, 0]
		def check_download_status(total, recvd, ratio, rate, eta):
			dl_status = [recvd, total, eta]

		args = message.content.split();
		if " ".join(args[1:]) == "" or " ".join(args[1:]) == " " or " ".join(args[1:]) == None:
			no_args = discord.Embed(title=localization[1][21][0], description=localization[1][21][14].format(prefix), color=embed_color)
			return await message.channel.send(embed=no_args)

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
		try:
			results = ytsearch(" ".join(args[1:]), max_results=9).to_dict()
		except Exception as e:
			if str(e) == "'sectionListRenderer'":
				err_yt_content = discord.Embed(title=localization[1][21][0], description=localization[1][21][17], color=embed_color)
			else:
				err_yt_content = discord.Embed(title=localization[1][21][0], description=localization[1][21][2], color=embed_color)
			return await message.channel.send(content=err_yt_content)
		results_text = ""
		video_url = []
		video_title = []
		yt_channel = []
		yt_duration = []
		file_url = {}
		for video in results:
			if str(video['duration']) != "0":
				results_text += emoji_number[str(results.index(video) + 1)] + " **{0}** ({1})\n".format(video['title'], video['duration'])
			else:
				results_text += emoji_number[str(results.index(video) + 1)] + " **{0}** (Stream)\n".format(video['title'])
			video_url.append("https://youtube.com{0}".format(video['url_suffix']))
			video_title.append(video['title'])
			yt_channel.append(video['channel'])
			yt_duration.append(video['duration'])
		yt_search_results = discord.Embed(title=localization[1][21][0], color=embed_color)
		yt_search_results.add_field(name=localization[1][21][3], value=results_text)
		msg = await message.channel.send(embed=yt_search_results)
		for video in results:
			await msg.add_reaction(emoji=emoji_number[str(results.index(video) + 1)])
		#print(video_infos['entries'])
		@bot.event
		async def on_reaction_add(reaction, user):
			channel = reaction.message.channel
			connection = create_connection(os.path.join(os.path.dirname(__file__), '../guilds_data.sqlite'))
			cursor = connection.cursor()
			queue_index = 0
			try:
				if reaction.emoji == str(emoji_number[str(emoji_number[reaction.emoji])]) and reaction.message.embeds != [] and reaction.message.embeds[0].fields != [] and reaction.message.embeds[0].fields[0].name == localization[1][21][3] and user.bot != True:
					if user.voice == None:
						no_args = discord.Embed(title=localization[1][21][0], description=localization[1][21][6].format(prefix), color=embed_color)
						return await message.channel.send(embed=no_args)
					if user.voice != None or user.voice.channel != None:

						cursor.execute("""CREATE TABLE IF NOT EXISTS music_queues_{0}(
        					position TEXT NOT NULL PRIMARY KEY,
        					userid INT NOT NULL,
        					url TEXT NOT NULL,
        					duration TEXT NOT NULL,
        					status TEXT NOT NULL);
    					""".format(str(message.guild.id)))

						cursor.execute("SELECT * FROM music_queues_{0}".format(message.guild.id) + " ORDER BY position;")
						music_queues = (cursor.fetchall())
						#print(music_queues)
						def state_change():
								connection = create_connection(os.path.join(os.path.dirname(__file__), '../guilds_data.sqlite'))
								cursor = connection.cursor()
								if (music_queues != None or music_queues != []) and len(music_queues) > 1:
									queue_mask = [(str(len(music_queues)), user.id, "{0}".format(video_url[emoji_number[reaction.emoji] - 1]), yt_duration[emoji_number[reaction.emoji] - 1], "Completed")]
									
								else:
									queue_mask = [(str(1), user.id, "{0}".format(video_url[emoji_number[reaction.emoji] - 1]), yt_duration[emoji_number[reaction.emoji] - 1], "Completed")]
									
								cursor.executemany("INSERT OR REPLACE INTO music_queues_{0} VALUES(?, ?, ?, ?, ?);".format(str(message.guild.id)), queue_mask)
								connection.commit()
						def after(error):
							try:
								fut = asyncio.run_coroutine_threadsafe(state_change(), bot.loop)
								fut.result()
							except Exception as e:
								print(e)
						try:
							os.remove(tempfile.gettempdir() + '/audio_dl_{0}.tmp'.format(reaction.message.guild.id))
						except:
							pass
						try:
							if reaction.message.guild.voice_client is not None and reaction.message.guild.voice_client.is_playing() == True:
								reaction.message.guild.voice_client.stop()
						except:
							pass
						video = pafy.new("{0}".format(video_url[emoji_number[reaction.emoji] - 1]))
						#print(video.length)
						if video.length == 0.0 or video.length == 0:
							music_length_exceed = discord.Embed(title=localization[1][21][0], description=localization[1][21][16], color=botconfig['accent2'])
							return await channel.send(embed=music_length_exceed)
						best = video.getbestaudio()
						if video.length != None and video.length > 1800:
							music_length_exceed = discord.Embed(title=localization[1][21][0], description=localization[1][21][13], color=botconfig['accent2'])
							return await channel.send(embed=music_length_exceed)
						if (music_queues != None or music_queues != []) and len(music_queues) > 1:
							queue_mask = [(str(len(music_queues)), user.id, "{0}".format(video_url[emoji_number[reaction.emoji] - 1]), yt_duration[emoji_number[reaction.emoji] - 1], "Playing")]						
						else:
							queue_mask = [(str(1), user.id, "{0}".format(video_url[emoji_number[reaction.emoji] - 1]), yt_duration[emoji_number[reaction.emoji] - 1], "Playing")]
						current_queue_mask = [("Current", user.id, "{0}".format(video_url[emoji_number[reaction.emoji] - 1]), yt_duration[emoji_number[reaction.emoji] - 1], "Playing")]
						cursor.executemany("INSERT OR REPLACE INTO music_queues_{0} VALUES(?, ?, ?, ?, ?);".format(str(message.guild.id)), queue_mask)
						cursor.executemany("INSERT OR REPLACE INTO music_queues_{0} VALUES(?, ?, ?, ?, ?);".format(str(message.guild.id)), current_queue_mask)
						connection.commit()
						cursor.execute("SELECT * FROM music_queues_{0}".format(message.guild.id) + ";")
						music_queues_currently = (cursor.fetchall())

						for queue in music_queues_currently:
							if music_queues_currently[music_queues_currently.index(queue)] == "{0}".format(video_url[emoji_number[reaction.emoji] - 1]):
								queue_index = music_queues_currently.index(queue)
						playing_now_embed = discord.Embed(title=localization[1][21][0], description=localization[1][21][12].format(str(round(dl_status[0] / 1024 / 1024, 2)), str(round(best.get_filesize() / 1024 / 1024, 2))), color=embed_color)
						msg = await channel.send(embed=playing_now_embed)
						if len(music_queues_currently) > 2:
							await msg.add_reaction(emoji="⏮")
						if len(music_queues_currently) > 2:
							await msg.add_reaction(emoji="⏭")
						await msg.add_reaction(emoji="⏯")
						await msg.add_reaction(emoji="⏹")
						best.download(quiet=False, filepath=tempfile.gettempdir() + '/audio_dl_{0}.tmp'.format(reaction.message.guild.id), callback=check_download_status)
						#with ytdl(ydl_opts) as ytdl_video:
							#song_info = ytdl_video.extract_info(, download=False)
						try:
							await user.voice.channel.connect()
						except Exception as e:
							print("Connection error: " + str(e))
						current_track = [()]
						current_track_index = 0
						for current_queue in music_queues_currently:
							if current_queue[0].startswith("Current"):
								current_track = current_queue
							try:
								if current_queue[2] == current_track[2] and current_queue[0] == "Current":
									current_track_index = music_queues_currently.index(current_queue)
							except:
								pass
						playing_now_embed = discord.Embed(title=localization[1][21][0], description=localization[1][21][4].format(video_title[emoji_number[reaction.emoji] - 1], "0:00", yt_duration[emoji_number[reaction.emoji] - 1], str(current_track_index), str(len(music_queues_currently) - 1)), color=embed_color)
						source = discord.FFmpegOpusAudio(tempfile.gettempdir() + '/audio_dl_{0}.tmp'.format(reaction.message.guild.id))
						if reaction.message.guild.voice_client is not None and reaction.message.guild.voice_client.is_playing() == True:
							reaction.message.guild.voice_client.stop()
							reaction.message.guild.voice_client.play(source, after=after)
						else:
							reaction.message.guild.voice_client.play(source, after=after)
						await msg.edit(embed=playing_now_embed)
						#reaction.message.guild.voice_client.source = discord.PCMVolumeTransformer(reaction.message.guild.voice_client.source)
						#reaction.message.guild.voice_client.source.volume = 1
			except Exception as e:
				if str(e).startswith == "<PartialEmoji":
					pass
				else:
					print(e)
			if reaction.emoji == "⏮" and reaction.message.embeds != [] and (reaction.message.embeds[0].description.startswith("".join(localization[1][21][4][:8])) or reaction.message.embeds[0].description.startswith("".join(localization[1][21][15][:4]))) and user.bot != True:
					if reaction.message.guild.voice_client is not None and reaction.message.guild.voice_client.is_playing() == True:
						reaction.message.guild.voice_client.stop()
					cursor.execute("SELECT * FROM music_queues_{0}".format(message.guild.id) + " ORDER BY position;")
					music_queues = (cursor.fetchall())
					music_queues.sort(key=sort_asc)
					current_track = [()]
					current_track_index = 0
					for current_queue in music_queues:
						if current_queue[0].startswith("Current"):
							current_track = current_queue
						try:
							if current_queue[2] == current_track[2] and current_queue[0] != "Current":
								current_track_index = music_queues.index(current_queue) - 1
						except:
							pass
					try:
						os.remove(tempfile.gettempdir() + '/audio_dl_{0}.tmp'.format(reaction.message.guild.id))
					except:
						pass
					cursor.execute("SELECT * FROM music_queues_{0}".format(message.guild.id) + " ORDER BY position;")
					music_queues_2 = (cursor.fetchall())
					music_queues_2.sort(key=sort_asc)
					for current_queue in music_queues_2:
						if current_queue[0] == "Current":
							current_track = current_queue
						try:
							if current_queue[2] == current_track[2] and current_queue[0] != "Current":
								current_track_index = music_queues.index(current_queue) - 1
								print(current_queue)
						except:
							pass
					#print(music_queues)
					current_queue_mask = [("Current", user.id, "{0}".format(music_queues_2[current_track_index][2]), music_queues_2[current_track_index][3], "Playing")]
					cursor.executemany("INSERT OR REPLACE INTO music_queues_{0} VALUES(?, ?, ?, ?, ?);".format(str(message.guild.id)), current_queue_mask)
					connection.commit()
					prev_video = pafy.new("{0}".format("{0}".format(music_queues_2[current_track_index][2])))
					best = prev_video.getbestaudio()
					if prev_video.length > 1800:
						music_length_exceed = discord.Embed(title=localization[1][21][0], description=localization[1][21][13], color=botconfig['accent2'])
						return await channel.send(embed=music_length_exceed)
					msg = reaction.message
					playing_now_embed = discord.Embed(title=localization[1][21][0], description=localization[1][21][12].format(str(round(dl_status[0] / 1024 / 1024, 2)), str(round(best.get_filesize() / 1024 / 1024, 2))), color=embed_color)
					await msg.edit(embed=playing_now_embed)
					def state_change():
						return

					def after(error):
						try:
							fut = asyncio.run_coroutine_threadsafe(state_change(), bot.loop)
							fut.result()
						except Exception as e:
							print("error" + str(e))
					best.download(quiet=False, filepath=tempfile.gettempdir() + '/audio_dl_{0}.tmp'.format(reaction.message.guild.id), callback=check_download_status)
					source = discord.FFmpegOpusAudio(tempfile.gettempdir() + '/audio_dl_{0}.tmp'.format(reaction.message.guild.id))
					
					playing_now_embed = discord.Embed(title=localization[1][21][0], description=localization[1][21][4].format(prev_video.title, "0:00", music_queues_2[current_track_index][3], str(current_track_index + 1), str(len(music_queues_2) - 1)), color=embed_color)
					await msg.edit(embed=playing_now_embed)
					if reaction.message.guild.voice_client.is_playing() == True:
						reaction.message.guild.voice_client.play(source, after=after)
					else:
						reaction.message.guild.voice_client.play(source, after=after)
			if reaction.emoji == "⏭" and reaction.message.embeds != [] and (reaction.message.embeds[0].description.startswith("".join(localization[1][21][4][:8])) or reaction.message.embeds[0].description.startswith("".join(localization[1][21][15][:4]))) and user.bot != True:
					if reaction.message.guild.voice_client.is_playing() == True:
						reaction.message.guild.voice_client.stop()
					cursor.execute("SELECT * FROM music_queues_{0}".format(message.guild.id) + " ORDER BY position;")
					music_queues = (cursor.fetchall())
					music_queues.sort(key=sort_asc)
					current_track = [()]
					current_track_index = 0
					for current_queue in music_queues:
						if current_queue[0].startswith("Current"):
							current_track = current_queue
						try:
							if current_queue[2] == current_track[2] and current_queue[0] != "Current":
								current_track_index = music_queues.index(current_queue) + 1
						except:
							pass
					try:
						os.remove(tempfile.gettempdir() + '/audio_dl_{0}.tmp'.format(reaction.message.guild.id))
					except:
						pass
					cursor.execute("SELECT * FROM music_queues_{0}".format(message.guild.id) + " ORDER BY position;")
					music_queues_2 = (cursor.fetchall())
					music_queues_2.sort(key=sort_asc)
					for current_queue in music_queues_2:
						if current_queue[0] == "Current":
							current_track = current_queue
						try:
							if current_queue[2] == current_track[2] and current_queue[0] != "Current":
								current_track_index = music_queues.index(current_queue) + 1
								print(current_queue)
						except:
							pass
					if(current_track_index) >= len(music_queues) - 1:
						return
					#print(music_queues)
					current_queue_mask = [("Current", user.id, "{0}".format(music_queues_2[current_track_index][2]), music_queues_2[current_track_index][3], "Playing")]
					cursor.executemany("INSERT OR REPLACE INTO music_queues_{0} VALUES(?, ?, ?, ?, ?);".format(str(message.guild.id)), current_queue_mask)
					connection.commit()
					prev_video = pafy.new("{0}".format("{0}".format(music_queues_2[current_track_index][2])))
					best = prev_video.getbestaudio()
					if prev_video.length > 1800:
						music_length_exceed = discord.Embed(title=localization[1][21][0], description=localization[1][21][13], color=botconfig['accent2'])
						return await channel.send(embed=music_length_exceed)
					msg = reaction.message
					playing_now_embed = discord.Embed(title=localization[1][21][0], description=localization[1][21][12].format(str(round(dl_status[0] / 1024 / 1024, 2)), str(round(best.get_filesize() / 1024 / 1024, 2))), color=embed_color)
					await msg.edit(embed=playing_now_embed)
					def state_change():
								return

					def after(error):
						try:
							fut = asyncio.run_coroutine_threadsafe(state_change(), bot.loop)
							fut.result()
						except Exception as e:
							print("error" + str(e))
					best.download(quiet=False, filepath=tempfile.gettempdir() + '/audio_dl_{0}.tmp'.format(reaction.message.guild.id), callback=check_download_status)
					source = discord.FFmpegOpusAudio(tempfile.gettempdir() + '/audio_dl_{0}.tmp'.format(reaction.message.guild.id))
					
					playing_now_embed = discord.Embed(title=localization[1][21][0], description=localization[1][21][4].format(prev_video.title, "0:00", music_queues_2[current_track_index][3], str(current_track_index + 1), str(len(music_queues_2) - 1)), color=embed_color)
					await msg.edit(embed=playing_now_embed)
					if reaction.message.guild.voice_client.is_playing() == True:
						reaction.message.guild.voice_client.play(source, after=after)
					else:
						reaction.message.guild.voice_client.play(source, after=after)
			if reaction.emoji == "⏯" and reaction.message.embeds != [] and (reaction.message.embeds[0].description.startswith("".join(localization[1][21][4][:8])) or reaction.message.embeds[0].description.startswith("".join(localization[1][21][15][:4]))) and user.bot != True:
					cursor.execute("SELECT * FROM music_queues_{0} WHERE position='Current'".format(message.guild.id) + ";")
					music_queues = (cursor.fetchall())[len(cursor.fetchall()) - 1]
					#print(music_queues)
					cursor.execute("SELECT * FROM music_queues_{0}".format(message.guild.id) + " ORDER BY position;")
					music_queues_2 = (cursor.fetchall())
					music_queues_2.sort(key=sort_asc)
					current_track = [()]
					current_track_index = 0
					for current_queue in music_queues_2:
						if current_queue[0] == "Current":
							current_track = current_queue
						try:
							if current_queue[2] == current_track[2] and current_queue[0] == "Current":
								current_track_index = music_queues.index(current_queue)
								print(current_queue)
						except:
							pass
					paused_video = pafy.new("{0}".format(music_queues[2]))
					best = paused_video.getbestaudio()
					msg = reaction.message
					if reaction.message.guild.voice_client.is_playing() == True:
						playing_now_embed = discord.Embed(title=localization[1][21][0], description=localization[1][21][15].format(paused_video.title, "0:00", music_queues_2[current_track_index][3], str(current_track_index + 1), str(len(music_queues_2) - 1)), color=embed_color)
						reaction.message.guild.voice_client.pause()
					else:
						playing_now_embed = discord.Embed(title=localization[1][21][0], description=localization[1][21][4].format(paused_video.title, "0:00", music_queues_2[current_track_index][3], str(current_track_index + 1), str(len(music_queues_2) - 1)), color=embed_color)
						reaction.message.guild.voice_client.resume()
					await msg.edit(embed=playing_now_embed)
			if reaction.emoji == "⏹" and reaction.message.embeds != [] and (reaction.message.embeds[0].description.startswith("".join(localization[1][21][4][:8])) or reaction.message.embeds[0].description.startswith("".join(localization[1][21][15][:4]))) and user.bot != True:
					msg = reaction.message
					try:
						reaction.message.guild.voice_client.stop()
						await msg.guild.voice_client.disconnect()
						os.remove(tempfile.gettempdir() + '/audio_dl_{0}.tmp'.format(reaction.message.guild.id))
					except:
						pass
					cursor.execute("DELETE FROM music_queues_{0};".format(message.guild.id))
					connection.commit()
					playing_now_embed = discord.Embed(title=localization[1][21][0], description=localization[1][21][7], color=embed_color)
					await msg.edit(embed=playing_now_embed)