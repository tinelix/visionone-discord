async def get_user(bot, discord, message, botconfig, platform, os, datetime,
                   one_result, localization, args, unix_time_millis,
                   connection, cursor, intents, lastmsgtime, embed_color):
	try:
		subargs = args[2]
	except:
		subargs = ""
	if one_result[3] < 0:
		your_timezone = "-" + str(-round(one_result[3] / 60 / 60 / 1000, 1))
	if one_result[3] > 0:
		your_timezone = "+" + str(round(one_result[3] / 60 / 60 / 1000, 1))
	if one_result[3] == 0:
		your_timezone = ""
	try:
		a_user = await message.guild.fetch_member(subargs)
	except:
		a_user = message.author
	try:
		argsuser = [(a_user.id, 'Russian', 0, 10800000,
		             unix_time_millis(message.created_at), 'Disabled', unix_time_millis(message.created_at), "Disabled", unix_time_millis(message.created_at), 0, 0, 0)]
		cursor.executemany(
		    "INSERT OR IGNORE INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
		    argsuser)
		connection.commit()
	except:
		pass
	if a_user.bot == True:
		bot_detector = localization[1][3][7]
	else:
		bot_detector = ""
	if a_user.nick == None:
		nick = "_Отсутствует_"
	else:
		nick = a_user.nick
	result = cursor.execute("SELECT * FROM users WHERE userid = " + str(a_user.id) + ";").fetchone(); 
	try:   
		if result[5] == "Disabled":
			msgcounter = localization[1][3][6]
		else:
			msgcounter = str(result[2]) + str(localization[1][3][5])
	except:
		msgcounter = localization[1][3][6]
	if a_user.raw_status == "online":
		user_status = localization[1][3][11][0]
	if a_user.raw_status == "idle":
		user_status = localization[1][3][11][1]
	if a_user.raw_status == "dnd":
		user_status = localization[1][3][11][2]
	if a_user.raw_status == "offline":
		user_status = localization[1][3][11][3]
	try:
		joindate_ms = int(unix_time_millis(a_user.joined_at) + one_result[3])
		joindate = datetime.datetime.fromtimestamp(
		(joindate_ms) / 1000)  # 25200000 for UTC+7
		regdate_ms = int(unix_time_millis(a_user.created_at) + one_result[3])
		regdate = datetime.datetime.fromtimestamp(
		(regdate_ms) / 1000)  # 25200000 for UTC+7
	except:
		pass
	try:
		if a_user.id == message.author.id:
			prepostdate_ms = int(lastmsgtime + one_result[3])
		else:
			prepostdate_ms = int(result[6] + one_result[3])
	except:
		pass
	try:
		prepostdate = datetime.datetime.fromtimestamp(
		    (prepostdate_ms) / 1000)  # 25200000 for UTC+7
	except:
		pass
	try:
	  dbregdate_ms = result[4]
	  dbregdate = datetime.datetime.fromtimestamp(dbregdate_ms / 1000)
	except:
		pass
	member_roles_a = ""
	for member_roles in a_user.roles:
		if member_roles.name != "@everyone":
			if a_user.roles.index(member_roles) < len(a_user.roles) - 1:
				member_roles_a += str(member_roles.name) + ", "
			else:
				member_roles_a += str(member_roles.name)
		else:
			member_roles_a += ""
	if member_roles_a == "" or member_roles_a == None:
		member_roles_a = "_Нет_"
	try:
		rep = "\n**" + str(localization[1][3][14]) + ": **" + str(one_result[7])
	except:
		rep = ""
	userprofile_content = discord.Embed(
	    title=bot_detector + str(localization[1][3][0]) + str(a_user),
	    description="**ID: **" + str(a_user.id) + rep,
	    color=embed_color)
	userprofile_content.add_field(
	    name=str(localization[1][3][1]), value=str(nick), inline=True)
	userprofile_content.add_field(
	    name=str(localization[1][3][10]), value=user_status, inline=False)
	try:
	  userprofile_content.add_field(
	    name=str(localization[1][3][4]) + dbregdate.strftime("%Y-%m"),
	    value=msgcounter,
	    inline=False)
	except:
		pass
	userprofile_content.add_field(
	    name=str(localization[1][3][2]),
	    value=joindate.strftime("%Y-%m-%d %H:%M:%S") + " (UTC" + your_timezone
	    + ")",
	    inline=False)
	userprofile_content.set_thumbnail(
	    url=str(
	        a_user.avatar_url_as(format=None, static_format="jpeg",
	                             size=4096)))
	try:
		userprofile_content.add_field(
	    name=str(localization[1][3][3]),
	    value=regdate.strftime("%Y-%m-%d %H:%M:%S") + " (UTC" + your_timezone +
	    ")",
	    inline=False)
	except:
		pass
	try:
		userprofile_content.add_field(
		    name=str(localization[1][3][12]) + "(" +
		    str(len(a_user.roles) - 1) + ")",
		    value=member_roles_a,
		    inline=False)
	except:
		userprofile_content.add_field(
		    name=str(localization[1][3][12]) + "(" + str(0) + ")",
		    value="(пусто)",
		    inline=False)
	try:
		userprofile_content.add_field(
		    name=str(localization[1][3][13]),
		    value=prepostdate.strftime("%Y-%m-%d %H:%M:%S") + " (UTC" +
		    your_timezone + ")",
		    inline=False)
	except:
		pass
	if a_user.bot == False:
	  try:
		  userprofile_content.add_field(
			    name=str(localization[1][3][15]),
			    value="**{0}** ({1}/{2})".format(str(one_result[9]), str(one_result[8]), str(((one_result[9]) * (50 + ((one_result[9]) * 10)) * (one_result[9] + 1)))),
			    inline=False)
	  except:
		  pass
	msg = await message.channel.send(embed=userprofile_content)
	if str(a_user.avatar_url_as(
	    format=None, static_format="jpeg", size=4096)) != "" or str(
	        a_user.avatar_url_as(format=None, static_format="jpeg",
	                             size=4096)) != None:
		await msg.add_reaction(emoji="ℹ️")
		await msg.add_reaction(emoji="🖼️")
	avatar_content = discord.Embed(
	    title=str(localization[1][3][8]) + str(a_user) + str(
	        localization[1][3][9]),
	    color=embed_color)
	avatar_content.set_image(
	    url=str(
	        a_user.avatar_url_as(format=None, static_format="jpeg",
	                             size=4096)))
	updated = 0

	@bot.event
	async def on_member_update(before, after):
		if after.id == a_user.id and msg.guild.id == after.guild.id:
			print(after.name + " | " + str(after.raw_status))
			if after.raw_status == "online":
				user_status = localization[1][3][11][0]
			if after.raw_status == "idle":
				user_status = localization[1][3][11][1]
			if after.raw_status == "dnd":
				user_status = localization[1][3][11][2]
			else:
				user_status = localization[1][3][11][3]
			if after.nick == None:
				nick = "_Отсутствует_"
			else:
				nick = after.nick
			userprofile_changed = discord.Embed(
			    title=bot_detector + str(localization[1][3][0]) + str(after),
			    description="**ID: **" + str(after.id) + rep,
			    color=embed_color)
			userprofile_changed.add_field(
			    name=str(localization[1][3][1]), value=str(nick), inline=True)
			userprofile_changed.add_field(
			    name=str(localization[1][3][10]),
			    value=user_status,
			    inline=False)
			userprofile_changed.add_field(
			    name=str(localization[1][3][4]) + dbregdate.strftime("%Y-%m"),
			    value=msgcounter,
			    inline=False)
			userprofile_changed.add_field(
			    name=str(localization[1][3][2]),
			    value=joindate.strftime("%Y-%m-%d %H:%M:%S") + " (UTC" +
			    your_timezone + ")",
			    inline=False)
			userprofile_changed.set_thumbnail(
			    url=str(
			        after.avatar_url_as(
			            format=None, static_format="jpeg", size=4096)))
			try:
			  userprofile_changed.add_field(
			    name=str(localization[1][3][3]),
			    value=regdate.strftime("%Y-%m-%d %H:%M:%S") + " (UTC" +
			    your_timezone + ")",
			    inline=False)
			except:
				pass
			try:
				userprofile_changed.add_field(
				    name=str(localization[1][3][13]),
				    value=prepostdate.strftime("%Y-%m-%d %H:%M:%S") + " (UTC" +
				    your_timezone + ")",
				    inline=False)
			except:
				pass
			if a_user.bot == False:
				try:
					userprofile_changed.add_field(
					name=str(localization[1][3][15]),
					value="**{0}** ({1}/{2})".format(str(one_result[9]), str(one_result[8]), str(((one_result[9]) * (50 + ((one_result[9]) * 10)) * (one_result[9] + 1)))),
					inline=False)
				except:
					pass
			await msg.edit(embed=userprofile_changed)

	@bot.event
	async def on_reaction_add(reaction, user):
		channel = reaction.message.channel
		if reaction.emoji == "ℹ️" and user.id != bot.user.id:
			await msg.edit(embed=userprofile_content)
		if reaction.emoji == "🖼️" and user.id != bot.user.id:
			await msg.edit(embed=avatar_content)
		if reaction.emoji == "🗨️" and user.id != bot.user.id:
			await msg.edit(embed=userprofile_content)


async def get_help(bot, discord, message, botconfig, platform, os, datetime,
                   one_result, localization, args, unix_time_millis,
                   connection, cursor, embed_color, prefix):
	if one_result[3] < 0:
		your_timezone = "-" + str(-round(one_result[3] / 60 / 60 / 1000, 1))
	if one_result[3] > 0:
		your_timezone = "+" + str(round(one_result[3] / 60 / 60 / 1000, 1))
	if one_result[3] == 0:
		your_timezone = ""
	if one_result[5] == "Disabled":
		msgcounter = str(localization[1][5][7])
	else:
		msgcounter = str(localization[1][5][3])
	profilehelp_content = discord.Embed(
	    title=str(localization[1][5][0]),
	    description=str(localization[1][5][2]).format(prefix) + msgcounter + ", " + str(
	        localization[1][5][4]) + your_timezone + str(localization[1][5][5])
	    + ", " + str(localization[1][5][6]) + "\n\n" + str(
	        localization[1][5][1]).format(prefix),
	    color=embed_color)
	await message.channel.send(embed=profilehelp_content)


async def get_guild(bot, discord, message, botconfig, platform, os, datetime,
                    one_result, localization, args, unix_time_millis,
                    connection, cursor, guild_result, intents, embed_color):
	if one_result[3] < 0:
		your_timezone = "-" + str(-round(one_result[3] / 60 / 60 / 1000, 1))
	if one_result[3] > 0:
		your_timezone = "+" + str(round(one_result[3] / 60 / 60 / 1000, 1))
	if one_result[3] == 0:
		your_timezone = ""
	if message.guild.explicit_content_filter == "disabled":
		explicit_cf = str(localization[1][4][14][0])
	else:
		explicit_cf = str(localization[1][4][14][1])
	if message.guild.mfa_level == 0:
		mfa_level = str(localization[1][4][13][0])
	if message.guild.mfa_level == 1:
		mfa_level = str(localization[1][4][13][1])
	if message.guild.mfa_level == 2:
		mfa_level = str(localization[1][4][13][2])
	if message.guild.mfa_level == 3:
		mfa_level = str(localization[1][4][13][3])
	birthdate_ms = int(
	    unix_time_millis(message.guild.created_at) + one_result[3])
	birthdate = datetime.datetime.fromtimestamp(
	    (birthdate_ms - 25200000) / 1000)  # 25200000 for UTC+7
	guildprofile_content = discord.Embed(
	    title=str(localization[1][4][0]) + str(message.guild.name) + str(
	        localization[1][4][1]),
	    description="**ID: **" + str(message.guild.id),
	    color=embed_color)
	guild_community = ""
	guild_online_members = []
	for guild_members in message.guild.members:
		if guild_members.status != discord.Status.offline:
			guild_online_members.append(str(guild_members))
	for guild_features in message.guild.features:
		if guild_features == "COMMUNITY":
			guild_community = "COMMUNITY"
	if guild_community == "COMMUNITY":
		rules_ch = "<#" + str(message.guild.rules_channel.id) + ">"
		description = message.guild.description
	else:
		rules_ch = localization[1][4][14][2]
		description = localization[1][4][14][2]
	if message.guild.afk_channel != None:
		afk_ch = message.guild.afk_channel.name
	else:
		afk_ch = localization[1][4][14][3]
	if guild_result[4] == "Disabled":
		msgcounter = localization[1][4][17]
	else:
		msgcounter = str(guild_result[2])
	owner = await message.guild.fetch_member(message.guild.owner_id)
	guildprofile_content.add_field(
	    name=str(localization[1][4][2]), value=str(description), inline=False)
	guildprofile_content.add_field(
	    name=str(localization[1][4][3]),
	    value=str(owner.name + "#" + owner.discriminator),
	    inline=True)
	guildprofile_content.add_field(
	    name=str(localization[1][4][4]),
	    value=str(
	        birthdate.strftime("%Y-%m-%d %H:%M:%S") + " (UTC" + your_timezone +
	        ")"),
	    inline=True)
	guildprofile_content.add_field(
	    name=str(localization[1][4][16]), value=str(msgcounter), inline=True)
	guildprofile_content.add_field(
	    name=str(localization[1][4][5]),
	    value=str(localization[1][4][15][0]) + str(
	        message.guild.premium_subscription_count) + str(
	            localization[1][4][15][1]) + str(
	                len(message.guild.premium_subscribers)),
	    inline=True)
	guildprofile_content.add_field(
	    name=str(localization[1][4][6]),
	    value=str(localization[1][4][15][2]) + str(
	        len(message.guild.text_channels)) + str(localization[1][4][15][3])
	    + str(len(message.guild.voice_channels)),
	    inline=True)
	guildprofile_content.add_field(
	    name=str(localization[1][4][7]),
	    value=str(localization[1][4][15][4]) + str(message.guild.member_count)
	    + str(localization[1][4][15][5]) + str(len(guild_online_members)),
	    inline=True)
	guildprofile_content.add_field(
	    name=str(localization[1][4][8]), value=explicit_cf, inline=True)
	guildprofile_content.add_field(
	    name=str(localization[1][4][9]), value=rules_ch, inline=True)
	guildprofile_content.add_field(
	    name=str(localization[1][4][10]), value=afk_ch, inline=True)
	guildprofile_content.set_thumbnail(
	    url=str(
	        message.guild.icon_url_as(
	            format=None, static_format="jpeg", size=4096)))
	await message.channel.send(embed=guildprofile_content)
