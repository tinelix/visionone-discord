def get():
    return [
        'English', # 0
        [ # 1
            [ # 1.0
                ' - a bot written from scratch in Python. While it is in development, gradually adding its new features. Developed by Tinelix. [Invite](https://discord.com/api/oauth2/authorize?client_id=785383439196487720&permissions=8&scope=bot)\n\n`=help` `=state` `=profile` `=settings`' # 1.0.0
            ],
            [ # 1.1
                'Bot health', # 1.1.0
                'Latency', # 1.1.1
                ' ms', # 1.1.2
                'Platform', # 1.1.3
                'CPU', # 1.1.4
                'Python version', # 1.1.5
                'Python build date', # 1.1.6
                'Packages versions' # 1.1.7
            ],
            [ # 1.2
                'Settings', # 1.2.0
                'To access the desired setting, click on one of the appropriate reactions.\n\n**🗣️ Bot language**\n**🕓 Timezone**\n**🗨️ Messages count**\n**🌈 Custom embed color**', # 1.2.1
                [ # 1.2.2
                    'Bot language', # 1.2.2.0
                    'To change the value, enter the commands below.\n\n**🇷🇺 Russian**\n```=set -l ru-RU```\n\n**🇺🇸 English**\n```=set -l en-US```' # 1.2.2.1
                ],
                [ # 1.2.3
                    'Timezone', # 1.2.3.0
                    'Current time', # 1.2.3.1
                    'Valid values', # 1.2.3.2
                    '-120 to 140 (UTC)', # 1.2.3.3
                    'Example', # 1.2.3.4
                    '```=set -tz -80\n=set -tz 30\n=set -tz 55```', # 1.2.3.5
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
                    '```=set -mc on```' # 1.2.6.6
                ],
                [ # 1.2.7
                    'Custom embed color (🏠)', # 1.2.7.0
                    'Valid values', # 1.2.7.1
                    '`red`, `orange`, `yellow`, `green`, `skyblue`, `blue`, `violet`, `rose`', # 1.2.7.2
                    'Example', # 1.2.7.3
                    '```=set -ec skyblue```', # 1.2.7.4
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
                'Date of sending the post message' # 1.3.13
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
                '`=profile -u [ID]` - find out information about the user.\n`=profile -g` - find out information about the server', # 1.5.1
                'Your parameters (can be changed in `=settings`): ', # 1.5.2
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
                'New Year\'s countdown', # 1.7.0
                ' days, ', # 1.7.1
                ' hours, ', # 1.7.2
                ' minutes ', # 1.7.3
                ' seconds', # 1.7.4
                ' (Moscow, UTC+3:00)', # 1.7.5
                ' (Chelyabinsk/Ekaterinburg, UTC+5:00)', # 1.7.6
                ' (Novosibirsk/Barnaul, UTC+7:00)', # 1.7.7
                ' (Ulan-Ude, UTC+8:00)', # 1.7.8
                'Countdown in other cities', # 1.7.9
                '_**New Year already arrived in Moscow!**_', # 1.7.11
                '_**New Year already arrived in Chelyabinsk and Ekaterinburg!**_', # 1.7.12
                '_**New Year already arrived in Novosibirsk and Barnual!**_', # 1.7.13
                '_**New Year already arrived in Ulan-Ude!**_' # 1.7.14      
            ],
            [ # 1.8
                'Random photos', # 1.8.0
                'Author', # 1.8.1
                'Likes', # 1.8.2
                'Enough for now!', # 1.8.3
                'It will be possible to see more photos in exactly an hour, since the Unsplash API has a limit of no more than 50 requests per hour. We apologize for any inconvenience caused.' # 1.8.4
            ],
        ]
    ]
