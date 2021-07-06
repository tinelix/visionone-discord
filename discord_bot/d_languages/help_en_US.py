import importlib.util
spec = importlib.util.spec_from_file_location("botconfig", "./discord_bot/discord_botconfig.py")
botconfig = importlib.util.module_from_spec(spec)
spec.loader.exec_module(botconfig)

def get():
    name = botconfig.botconfig['name']
    prefix = botconfig.botconfig['prefix']
    return {
            'calc': {
                'title': 'About calculator',
                'description': 'This is simplest calculator, can calculate simple arithmetic operations. Any variables are excluded.',
                'instruction': '```{0}calc 34*1429\n{0}calc 120/480\n{0}calc 170!```\n\n**Signs:** `+` add\n`-` subtract\n`*` multiply\n`/` divide'
            },
            'codec': {
                'title': 'About codec',
                'description': 'Codec can convert encrypted text and vice versa.',
                'instruction': '```{0}codec -e Hello!\n{0}codec -d SGVsbG8h```',
                'parameters': '`-e [text]` - encrypt (encode)\n`-d [code]` - decrypt (decode)'
            },
            'crystball': {
                'title': 'About crystal ball',
                'description': 'Answers randomly any of your questions, but just be warned that, answers of crystal ball often do not coincide with reality, so do not take it seriously!',
                'instruction': '```{0}crystball [вопрос]```'
            },
            'feedback': {
                'title': 'About developer feedback',
                'description': 'You can contact the bot author at any time with wishes or a bug report. The main thing is the ability to express yourself culturally and not to spam, otherwise he will not be able to help. 😉',
                'instruction': '```{0}feedback [question or wish]```'
            },
            'info': {
                'title': 'About "info" command',
                'description': 'About {0} bot and links'.format(name),
            },
            'music': {
                'title': 'About music player',
                'description': 'Search and play music from YouTube on voice channel. Playlist supported on each server.',
                'requirements': 'Be sure to connect to the voice channel.',
                'instruction': '```{0}music [request]```'
            },
            'photo': {
                'title': 'About random photo viewer',
                'description': 'View random photos from Reddit and Unsplash.',
                'instruction': '```{0}photo -u```',
                'parameters': '`-u` - from Unsplash\n`-r` - from subreddits',
            },
            'poll': {
                'title': 'About poll',
                'description': 'Conducts a vote limited by an end date',
                'instruction': '```{0}poll What do you like the most? -o [90s],[2000s],[2010s],[2020s] 2021-07-10=18:00```\n\n_Space between `],` and `[` must not be!_'
            },
            'post': {
                'title': 'About self-posting messages',
                'description': 'Will immediately send your message from the news channel.',
                'requirements': '1. Community features are required, you can enable them in your Discord server settings.\n2. Publishing is possible only on news channels (channels with announcements).\n3. Requires \'Manage messages\' permission.',
                'instruction': '```{0}post [message]```'
            },
            'profile': {
                'title': 'About command "profile"',
                'description': 'Shows server and member information',
                'instruction': '```{0}profile -g\n{0}profile -u [case insensitive username]```',
                'parameters': '`-g` - about guild (server)\n`-u` - about user'
            },
            'rep': {
                'title': 'About reputation counter',
                'description': 'Promoting or demoting the reputation of a Discord member.',
                'instruction': '```{0}rep [member ID]```'
            },
            'settings': {
                'title': 'About bot settings',
                'description': 'Bot {0} allows a little more flexibility to adapt not only for your server, but also for yourself. For example, he can send his branded message about the arrival or departure of participants from the server.'.format(name),
                'requirements': 'To configure a bot for a server, you need a member\'s \'Manage Server\' permission.',
                'instruction': '```{0}settings\n{0}set -pfx v!```',
            },
            'state': {
                'title': 'About "state" command',
                'description': 'Checking technical bot health.',
                'instruction': '```{0}state```'
            },
            'weather': {
                'title': 'About "weather" command',
                'description': 'Weather in your area.\n_Uses OpenWeatherMap API_',
                'instruction': '```{0}weather [city]```'
            }
    }
