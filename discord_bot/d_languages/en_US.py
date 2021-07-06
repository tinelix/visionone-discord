import importlib.util
spec = importlib.util.spec_from_file_location("botconfig", "./discord_bot/discord_botconfig.py")
botconfig = importlib.util.module_from_spec(spec)
spec.loader.exec_module(botconfig)
def get():
    name = botconfig.botconfig['name'] 
    prefix = botconfig.botconfig['prefix'] 
    return [
        'English', # 0
        [ # 1
            [ # 1.0
                ' - simple and slightly extensible. Developed by Tinelix.\n**Prefix:** `{0}`{1}\n\n**Did you know that...** {2}', # 1.0.0
                [ # 1.0.1
                  'General', # 1.0.1.0
                  '`help`, `state`, `profile`, `feedback`, `info`' # 1.0.1.1
                ],
                [ # 1.0.2
                  'Fun', # 1.0.2.0
                  '`photo`, `8ball` (`crystball`), `music`' # 1.0.2.1
                ],
                [ # 1.0.3
                  'Management', # 1.0.3.0
                  '`settings`, `post`' # 1.0.3.1
                ],
                [ # 1.0.4
                  'Miscellaneous', # 1.0.4.0
                  '`calc`, `weather`, `codec`, `poll`, `rep`, `embed`' # 1.0.4.1
                ],
                '**Prefix:** ', # 1.0.5
                [ # 1.0.6
                    'Requirements', # 1.0.6.0
                    'Instruction', # 1.0.6.1
                    'Parameters', # 1.0.6.2
                ]
            ],
            [ # 1.1
                'Bot health', # 1.1.0
                'Latency', # 1.1.1
                ' ms', # 1.1.2
                'Platform', # 1.1.3
                'CPU', # 1.1.4
                'Python version', # 1.1.5
                'Python build date', # 1.1.6
                'Packages versions', # 1.1.7
                'Analytics', # 1.1.8
                ' core', # 1.1.9
                ' cores', # 1.1.10
                ' cores', # 1.1.11
                ' MHz', # 1.1.12
                'RAM', # 1.1.13
                ' kB', # 1.1.14
                ' MB', # 1.1.15
                ' GB', # 1.1.16
                ' free' # 1.1.17
            ],
            [ # 1.2
                'Settings', # 1.2.0
                'To access the desired setting, click on one of the appropriate reactions.\n\n**🗣️ Bot language**\n**🕓 Timezone**\n**🗨️ Messages count**\n**🌈 Custom embed color**\n🚩 **Custom prefix**\n🏆 **Level system**\n👋 **Welcome/goodbye messages**', # 1.2.1
                [ # 1.2.2
                    'Bot language', # 1.2.2.0
                    'To change the value, enter the commands below.\n\n**🇷🇺 Russian**\n```{0}set -l ru-RU```\n\n**🇺🇸 English**\n```{0}set -l en-US```' # 1.2.2.1
                ],
                [ # 1.2.3
                    'Timezone', # 1.2.3.0
                    'Current time', # 1.2.3.1
                    'Valid values', # 1.2.3.2
                    '-120 to 140 (UTC)', # 1.2.3.3
                    'Example', # 1.2.3.4
                    '```{0}set -tz -80\n{0}set -tz 30\n{0}set -tz 55```', # 1.2.3.5
                    '-80 for UTC-8:00, 30 for UTC+3:00 (MSK), 55 for UTC+5:30.' # 1.2.3.6
                ],
                [ # 1.2.4
                    'Error', # 1.2.4.0
                    'This value must be stricly numeric', # 1.2.4.1
                    'You changed your timezone to UTC' # 1.2.4.2
                ],
                [ # 1.2.5
                    'Message counter', # 1.2.5.0
                    'Are you setting up a Vision bot at the level of your server or for yourself? To select an answer, press one of the corresponding reactions.\n||_yes, we are using SQLite DB_||\n\n🏠 - at the server level\n👤 - for yourself', # 1.2.5.1
                    'Message counter enabled.', # 1.2.5.2
                    'Message counter disabled.', # 1.2.5.3
                    'Sorry, but you do not have permission to manage the server. Please use your personal settings.', # 1.2.5.4
                    'Error' # 1.2.5.5
                ],
                [ # 1.2.6
                    'Message counter', # 1.2.6.0
                    'Total messages counted since the beginning of ', # 1.2.6.1
                    ' messages', # 1.2.6.2
                    'Valid values', # 1.2.6.3
                    '`on` - enable, `off` - disable', # 1.2.6.4
                    'Example', # 1.2.6.5
                    '```{0}set -mc on```'.format(prefix) # 1.2.6.6
                ],
                [ # 1.2.7
                    'Custom embed color (🏠)', # 1.2.7.0
                    'Valid values', # 1.2.7.1
                    '`red`, `orange`, `yellow`, `green`, `skyblue`, `blue`, `violet`, `rose`', # 1.2.7.2
                    'Example', # 1.2.7.3
                    '```{0}set -ec skyblue```', # 1.2.7.4
                    'Custom embed color (🏠)', # 1.2.7.5
                    'Changes saved.' # 1.2.7.6
                ],
                [ # 1.2.8
                    'Bot prefix', # 1.2.8.0
                    'Default', # 1.2.8.1
                    'Example', # 1.2.8.2
                    '```{0}set -pfx v!```', # 1.2.8.3
                    'Changes saved.', # 1.2.8.4
                    '**WARNING!** Since you are currently using the latest version of the bot, then, accordingly, this setting may need to be improved.',
                ],
                [ # 1.2.9
                    'Level system', # 1.2.9.0
                    'Valid values', # 1.2.9.1
                    '`on` - enable, `off` - disable', # 1.2.9.2
                    'Example', # 1.2.9.3
                    '```{0}set -lvs on```' # 1.2.9.4
                ],
                [ # 1.2.10
                    'Welcome/goodbye messages', # 1.2.10.0
                    'Valid values', # 1.2.10.1
                    '`[Channel ID] [Text]` - enable or edit\n`off` - disable', # 1.2.10.2
                    'Example', # 1.2.10.3
                    '```{0}set -wl_msg 794585820312633354 Hello, ╭user╮!\n{0}set -gb_msg 794585820312633354 Goodbye, ╭user╮!```', # 1.2.10.4
                    'Autoformat', # 1.2.10.5
                    '`{user}` - username\n`{user_with_discrim}` - username with discriminator\n`{gn}` - guildname\n`{mention}` - user mention',  # 1.2.10.6
                    'Error', # 1.2.10.7
                    'This channel cannot be found on your Discord server.' # 1.2.10.8
                ]
            ],
            [ # 1.3
                'About ', # 1.3.0
                'Nickname', # 1.3.1
                'Date of joining the guild', # 1.3.2
                'Registration date', # 1.3.3
                'Total msg\'s since ', # 1.3.4
                ' messages', # 1.3.5
                '_This user has a message counter disabled_', # 1.3.6
                '[BOT] ', # 1.3.7
                '', # 1.3.8
                '\'s avatar', # 1.3.9
                'Status', # 1.3.10
                [ # 1.3.11
                    '<:online:861861013241856001> Online', # 1.3.11.0
                    '<:idle:861861016043913216> Idle', # 1.3.11.1
                    '<:dnd:861861013347106836> DND', # 1.3.11.2
                    '<:offline:861861010163367947> Offline' # 1.3.11.3
                ],
                'Roles ', # 1.3.12
                'Date of sending the post message', # 1.3.13
                'Reputation', # 1.3.14
                'Level', # 1.3.15
                'Avatar link', # 1.3.16
            ],
            [ # 1.4
                'About ', # 1.4.0 
                ' server', # 1.4.1
                'Description', # 1.4.2
                'Owner', # 1.4.3
                'Birthdate', # 1.4.4
                'Boosts', # 1.4.5
                'Channels', # 1.4.6
                'Members', # 1.4.7
                'Explicit content filter', # 1.4.8
                'Rules channel', # 1.4.9
                'AFK channel', # 1.4.10
                '2FA protection', # 1.4.11
                'Verification level', # 1.4.12
                [ # 1.4.13
                    'No limits', # 1.4.13.0
                    'Easy', # 1.4.13.1
                    'Medium', # 1.4.13.2
                    'Hard', # 1.4.13.3
                    'Strict' # 1.4.13.4
                ],
                [ # 1.4.14
                    'On', # 1.4.14.0
                    'Off', # 1.4.14.1
                    '_Disabled "Community"_', # 1.4.14.2
                    '_No AFK channel_' # 1.4.14.3                
                ],
                [ # 1.4.15
                    '💎 ', # 1.4.15.0
                    ' | 🧙 ', # 1.4.15.1
                    '💬 ', # 1.4.15.2
                    ' | 🔉 ', # 1.4.15.3
                    '👤 ', # 1.4.15.4
                    ' | 🔌 ' # 1.4.15.5
                ],
                'Messages', # 1.4.16
                '_This server has a message counter disabled_', # 1.4.17
            ],
            [ # 1.5
                'Profile', # 1.5.0
                '`{0}profile -u [ID]` - find out information about the user.\n`{0}profile -g` - find out information about the server', # 1.5.1
                'Your parameters (can be changed in `{0}settings`): ', # 1.5.2
                'message counter enabled', # 1.5.3
                'UTC', # 1.5.4
                ' timezone', # 1.5.5
                '🇺🇸', # 1.5.6
                'message counter disabled', # 1.5.7
            ],
            [ # 1.6
                'Tinelix News', # 1.6.0
                'To select an title, press one of the corresponding reactions. (for Russian auditory only)\n\n' # 1.6.1
            ],
            [ # 1.7
                ' ', # 1.7.0
                ' ', # 1.7.1
                ' ', # 1.7.2
                ' ', # 1.7.3
                ' ', # 1.7.4
                ' ', # 1.7.5
                ' ', # 1.7.6
                ' ', # 1.7.7
                ' ', # 1.7.11
                ' ', # 1.7.13
                ' ' # 1.7.14      
            ],
            [ # 1.8
                'Random photos', # 1.8.0
                'Author', # 1.8.1
                'Likes', # 1.8.2
                'Enough for now!', # 1.8.3
                'It will be possible to see more photos in exactly an hour, since the Unsplash API has a limit of no more than 50 requests per hour. We apologize for any inconvenience caused.', # 1.8.4
                '`{0}photo -u` - viewing photos from Unsplash.\n`{0}photo -r` - viewing photos from subreddits.', # 1.8.5
                '`{0}photo -u` - viewing photos from Unsplash.', # 1.8.6
                '`{0}photo -r` - viewing photos from subreddits.', # 1.8.7
                'This command doesn\'t work without acces to two APIs.', # 1.8.8
                'You cannot view photos without access to Unsplash API. To solve this problem, contact bot author.', # 1.8.9
                'You cannot view photos without access to Reddit API. To solve this problem, contact bot author.', # 1.8.10
            ],
            [ # 1.9
                'Calculator', # 1.9.0
                'Listing', # 1.9.1
                'Result', # 1.9.2
                'Exception caught!\n', # 1.9.3
                'You forgot to enter an expression.\n```{0}calc 4 * 58```', # 1.9.4
                'In this version of the Calculator you can only perform simple arithmetic operations.', # 1.9.5
                'Available characters', # 1.9.6
                '`+` - add\n`-` - subtract\n`*` - multiply\n`/` - divide', # 1.9.7
                'Attempt to divide by zero', # 1.9.8
                'The expression is too large', # 1.9.9
                'Variables are not accepted', # 1.9.10
            ],
            [ # 1.10
                'Feedback', # 1.10.0
                '{0} Bugtracker'.format(name), # 1.10.1
                'The author bot will reply shortly, please wait...', # 1.10.2
                'You forgot to provide arguments.\n\n```{0}feedback Hi!```', # 1.10.3
                'You answered:', # 1.10.4
                'Estimated waiting time', # 1.10.5
                'more than 10 minutes', # 1.10.6
                '{0} minutes', # 1.10.7
                'Usually during these hours (after {0} local time) our support service will not be able to send you a reply message.'
            ],
            [ # 1.11
                'Weather | ', # 1.11.0
                'Temperature', # 1.11.1
                'min. ', # 1.11.2
                ', avg. ', # 1.11.3
                ', max. ', # 1.11.4
                'Wind speed', # 1.11.5
                ' MPS', # 1.11.6
                'Humidity', # 1.11.7
                'Forecast for the next 12 hours', # 1.11.8
                'Used by the OpenWeatherMap API', # 1.11.9
                'en', # 1.11.10
                'Error', # 1.11.11
                'The requested city or town cannot be found. Maybe, write differently?', # 1.11.12
                'Errorcode', # 1.11.13
                'You forgot to enter the name of the city.' # 1.11.14
            ],
            [ # 1.12
                'Crystal Ball', # 1.12.0
                'Question', # 1.12.1
                'He says', # 1.12.2
                'All matches are random. Think of it as a game, not as a reality.', # 1.12.3
                'Error', # 1.12.4
                'First ask him a question.' # 1.12.5
            ],
            [ # 1.13
                'Error', # 1.13.0
                'You must make sure that community features are enabled on your Discord server in order to post news.', # 1.13.1
                'You forgot to enter a message to publication.', # 1.13.2
                'This command unavailable, because you don\'t have permisson to manage messages.', # 1.13.3
                'Switch to the news channel first.'
            ],
            [ # 1.14
              'Codec', # 1.14.0 
              'You have to choose the data type to decode into a regular string. The selection is made by clicking on the appropriate reaction.', # 1.14.1
              'You have to choose the data type to encode into a regular string. The selection is made by clicking on the appropriate reaction.', # 1.14.2
              '1️⃣ Base64\n2️⃣ Base32\n3️⃣ Base16\n4️⃣ Binary code', # 1.14.3
              'Result', # 1.14.4
              '`{0}codec -d` - decode text\n`{0}codec -e` - encode text', # 1.14.5
              'The text could not be decoded. Invalid data type selected.', # 1.14.6
              'Viewing in embed message is not possible.' # 1.14.7
              'You forgot to enter text.\n\n```{0}codec -e Hello!\n{0}codec -d SGVsbG8h```' # 1.14.8
            ],
            [ # 1.15
              'About bot', # 1.15.0
              '{0} is a simple and extensible bot from Tinelix. This bot is a replacement for the Highflash bot, which was crude enough to run for monitoring bots. But don\'t worry, the Vision bot has (albeit imperfect) integration with the SQlite3 database, when there was only primitive JSON in Highflash. The bot was written from scratch and took into account the mistakes made during the development of the Highflash bot. It develops not only thanks to you, but also to the author (Tinelix) with its productivity. He can ask you the weather, encrypt or decrypt texts, show random and rather interesting photos from Reddit and Unsplash, play Crystal Ball, etc.'.format(name), # 1.15.1
              'Written in', # 1.15.2
              'Author', # 1.15.3
              'Bots Monitorings', # 1.15.4
              '[bots.server-discord.com](https://bots.server-discord.com/785383439196487720)\n[BotiCord](https://boticord.top/bot/785383439196487720)\n[Bots for Discord](https://botsfordiscord.com/bot/785383439196487720)\n[top.gg](https://top.gg/bot/785383439196487720)\n[discord.bots.gg](https://discord.bots.gg/bots/785383439196487720)', # 1.15.5
              'Links', # 1.15.6
              '[Invite](https://discord.com/api/oauth2/authorize?client_id=785383439196487720&permissions=8&scope=bot)\n[GitHub](https://github.com/tinelix/visionone-discord)\n[Our support server](https://discord.gg/HAt6K2QuJU)', # 1.15.7
              '[Invite](https://discord.com/oauth2/authorize?client_id=769515555765616690&permissions=8&scope=bot)\n[GitHub](https://github.com/tinelix/visionbot)'
            ],
            [ # 1.16
              'Polling', # 1.16.0
              '', # 1.16.1
              'Time has gone! End time: {0}', # 1.16.2
              'Polling is over', # 1.16.3
              'You forgot to supply the required arguments to this or to the command enter arguments as arguments with `[` and `],`. Follow the example below.  And yes, between the parentheses, a comma without any spaces is required.\n\n```{0}poll What do you like the most? -o [90s],[2000s],[2010s],[2020s] 2021-02-12=18:00```', # 1.16.4
              'The voting end date must not be earlier than today.'
            ],
            [ # 1.17
              'Reputation', # 1.17.0
              'Do you want to promote or demote a person? The selection is made by clicking on the reaction.\n\n👍 **Promote**\n👎 **Demote**', # 1.17.1
              'You cannot promote or demote yourself!', # 1.17.2
              'Okay, you demoted it.', # 1.17.3
              'Okay, you promoted it.', # 1.17.4
              'Example', # 1.17.5
              '```{0}rep <Member ID>```', # 1.17.6
              'This person is not in our database.', # 1.7.7
              'You already promoted it.', # 1.7.8
              'You already demoted it.' # 1.7.9
            ],
            [ # 1.18
                'Congratulations!', # 1.18.0
                '{0} has moved to a new level **{1}**! The main thing is to be active.' # 1.18.1
            ],
            [ # 1.19
              'Access denied.' # 1.19.0
            ],
            [ # 1.20
              'Embed messages constructor', # 1.20.0
              'You forgot to supply the required arguments to this or to the command enter arguments as arguments with `[` and `],`. Follow the example below.  And yes, between the parentheses, a comma without any spaces is required.\n\n```{0}embed Text -t [Title],[Footer]```' # 1.20.1
            ],
            [ # 1.21
              'Music player', # 1.21.0
              'No results found. Try another query.', # 1.21.1
              'API is temporarily unavailable.', # 1.21.2
              'Search results', # 1.21.3
              '**Now playing:** {0} ({1}/{2})\n{3} of {4}', # 1.21.4
              'Queues', # 1.21.5
              'First join any voice channel, then try again.', # 1.21.6
              'Listening stopped.', # 1.21.7
              'Are you sure want to clear the playlist?\nTo confirm, you need to collect 3 reactions.', # 1.21.8
              'Playlist cleared.', # 1.21.9
              'Used by the YouTube Data API', # 1.21.10
              'Something went wrong...', # 1.21.11
              'Loading {0} of {1} MB...', # 1.21.12
              'The track should not exceed 30 minutes in duration.', # 1.21.13
              'To play music, just specify a search query on YouTube.\n\n```{0}music Tobu Cacao```', # 1.21.14
              '**Paused:** {0} ({1}/{2})\n{3} of {4}', # 1.21.15
              'There is currently no streaming media playback available.', # 1.21.16
              'There was an error displaying search results. Most likely, this is some kind of issue on the side of the `youtube_search` module. Try searching again.' # 1.21.17
            ]
        ]
    ]

def longdate():
    return ['English', 'January {0}, {1}', 'February {0}, {1}', 'March {0}, {1}', 'April {0}, {1}', 'May {0}, {1}', 'June {0}, {1}', 'July {0}, {1}', 'August {0}, {1}', 'September {0}, {1}', 'October {0}, {1}', 'November {0}, {1}', 'December {0}, {1}']

def longdate_without_year():
    return ['English', 'January {0}', 'February {0}', 'March {0}', 'April {0}', 'May {0}', 'June {0}', 'July {0}', 'August {0}', 'September {0}', 'October {0}', 'November {0}', 'December {0}']

def shortdate_without_year():
    return ['English', 'Jan {0}', 'Feb {0}', 'Mar {0}', 'Apr {0}', 'May {0}', 'Jun {0}', 'Jul {0}', 'Aug {0}', 'Sep {0}', 'Oct {0}', 'Nov {0}', 'Dec {0}']
