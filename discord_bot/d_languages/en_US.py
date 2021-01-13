import importlib.util
spec = importlib.util.spec_from_file_location("botconfig", "/home/runner/visionbot/discord_bot/discord_botconfig.py")
botconfig = importlib.util.module_from_spec(spec)
spec.loader.exec_module(botconfig)
def get():
    name = botconfig.botconfig['name'] 
    prefix = botconfig.botconfig['prefix'] 
    return [
        'English', # 0
        [ # 1
            [ # 1.0
                ' - simple and slightly extensible. Developed by Tinelix.\n**Prefix:** `{0}`\n\n**Did you know that...** {1}', # 1.0.0
                [ # 1.0.1
                  'General', # 1.0.1.0
                  '`help` `state` `profile` `feedback` `info`' # 1.0.1.1
                ],
                [ # 1.0.2
                  'Fun', # 1.0.2.0
                  '`=photo`' # 1.0.2.1
                ],
                [ # 1.0.3
                  'Management', # 1.0.3.0
                  '`=settings`' # 1.0.3.1
                ],
                [ # 1.0.4
                  'Miscellaneous', # 1.0.4.0
                  '`calc` `weather` `codec` `poll`' # 1.0.4.1
                ],
                '**Prefix:** ' # 1.0.5
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
                'Bot author', # 1.1.9
                'Links' # 1.1.10
            ],
            [ # 1.2
                'Settings', # 1.2.0
                'To access the desired setting, click on one of the appropriate reactions.\n\n**🗣️ Bot language**\n**🕓 Timezone**\n**🗨️ Messages count**\n**🌈 Custom embed color**', # 1.2.1
                [ # 1.2.2
                    'Bot language', # 1.2.2.0
                    'To change the value, enter the commands below.\n\n**🇷🇺 Russian**\n```{0}set -l ru-RU```\n\n**🇺🇸 English**\n```{0}set -l en-US```'.format(prefix) # 1.2.2.1
                ],
                [ # 1.2.3
                    'Timezone', # 1.2.3.0
                    'Current time', # 1.2.3.1
                    'Valid values', # 1.2.3.2
                    '-120 to 140 (UTC)', # 1.2.3.3
                    'Example', # 1.2.3.4
                    '```{0}set -tz -80\n{0}set -tz 30\n{0}set -tz 55```'.format(prefix), # 1.2.3.5
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
                    '```{0}set -ec skyblue```'.format(prefix), # 1.2.7.4
                    'Custom embed color (🏠)', # 1.2.7.5
                    'Changes saved.' # 1.2.7.6
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
                    '<:online_emoji:786943382651142145> Online',
                    '<:idle_emoji:786943383721213952> Idle',
                    '<:dnd_emoji:786943382316253204> Do not disturb',
                    '<:offline_emoji:786943380085145651> Offline'
                ],
                'Roles ', # 1.3.12
                'Date of sending the post message', # 1.3.13
                'Reputation' # 1.3.14
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
                '`{0}profile -u [ID]` - find out information about the user.\n`{0}profile -g` - find out information about the server'.format(prefix), # 1.5.1
                'Your parameters (can be changed in `{0}settings`): '.format(prefix), # 1.5.2
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
                '`{0}photo -u` - viewing photos from Unsplash.\n`{0}photo -r` - viewing photos from subreddits.'.format(prefix)
            ],
            [ # 1.9
                'Calculator', # 1.9.0
                'Listing', # 1.9.1
                'Result', # 1.9.2
                'Exception caught!\n', # 1.9.3
                'You forgot to enter an expression.\n```{0}calc 4 * 58```'.format(prefix), # 1.9.4
                'In this version of the Calculator you can only perform simple arithmetic operations.', # 1.9.5
                'Available characters', # 1.9.7
                '`+` - add\n`-` - subtract\n`*` - multiply\n`/` - divide'
            ],
            [ # 1.10
                'Feedback', # 1.10.0
                '{0} Bugtracker'.format(name), # 1.10.1
                'The author bot will reply shortly, please wait...', # 1.10.2
                'You forgot to provide arguments.\n\n```{0}feedback Hi!```'.format(prefix), # 1.10.3
                'You answered:' # 1.10.4
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
                'All matches are random.', # 1.12.3
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
              '`{0}codec -d` - decode text\n`{0}codec -e` - encode text'.format(prefix), # 1.14.5
              'The text could not be decoded. Invalid data type selected.', # 1.14.6
              'Viewing in embed message is not possible.' # 1.14.7
              'You forgot to enter text.\n\n```{0}codec -e Hello!\n{0}codec -d SGVsbG8h```'.format(prefix) # 1.14.8
            ],
            [ # 1.15
              'About bot', # 1.15.0
              '{0} is a simple and extensible bot from Tinelix. This bot is a replacement for the Highflash bot, which was crude enough to run for monitoring bots. But don\'t worry, the Vision bot has (albeit imperfect) integration with the SQlite3 database, when there was only primitive JSON in Highflash. The bot was written from scratch and took into account the mistakes made during the development of the Highflash bot. It develops not only thanks to you, but also to the author (Tinelix) with its productivity. He can ask you the weather, encrypt or decrypt texts, show random and rather interesting photos from Reddit and Unsplash, play Crystal Ball, etc.'.format(name), # 1.15.1
              'Written in', # 1.15.2
              'Author', # 1.15.3
              'Bots Monitoring', # 1.15.4
              '[bots.server-discord.com](https://bots.server-discord.com/785383439196487720)\n[BotiCord](https://boticord.top/bot/785383439196487720)\n[Bots for Discord](https://botsfordiscord.com/bot/785383439196487720)', # 1.15.5
              'Links', # 1.15.6
              '[Invite](https://discord.com/api/oauth2/authorize?client_id=785383439196487720&permissions=8&scope=bot)\n[GitHub](https://github.com/tinelix/visionbot)' # 1.15.7
            ],
            [ # 1.16
              'Polling', # 1.16.0
              '', # 1.16.1
              'Time has gone! End time: {0}', # 1.16.2
              'Polling is over', # 1.16.3
              'You forgot to supply the required arguments to this or to the command enter arguments as arguments with `[` and `],`. Follow the example below.  And yes, between the parentheses, a comma without any spaces is required.\n\n```{0}poll How did you meet 2021? Good or bad? -o [Awesome],[Good],[I don\'t care],[So bad] 2020-01-10=20:00```'.format(prefix), # 1.16.4
              'The voting end date must not be earlier than today.'
            ],
            [ # 1.16
              'Search for a user by discriminator', # 1.16.0
              'Total results: {0}', # 1.16.1
            ],
            [ # 1.17
              'Reputation', # 1.17.0
              'Do you want to promote or demote a person? The selection is made by clicking on the reaction.\n\n👍 **Promote**\n👎 **Demote**', # 1.17.1
              'You cannot promote or demote yourself!', # 1.17.2
              'Okay, you demoted it.', # 1.17.3
              'Okay, you promoted it.', # 1.17.4
              'Example', # 1.17.5
              '```{0}rep <Member ID>```'.format(prefix), # 1.17.6
              'This person is not in our database.', # 1.7.7
              'You already promoted it.', # 1.7.8
              'You already demoted it.' # 1.7.9
            ]
        ]
    ]