<h1>VisionOne</h1>
<p>Разработан Тинеликсом в качестве замены бота Highflash. Доступен на данный момент для Discord.<br>
  (<i>Google Translate, i'm sorry</i>: Developed by Tinelix as a replacement for the Highflash bot. Available for now on Discord)<br>
<i>Лицензируется с условиями GNU Affero General Public License версии 3 для веб-приложений.</i>
<p><b>Преимущества перед Highflash</b>
<br>1. Счетчик сообщений
<br>2. Гибкость настроек (часовые пояса, цвета в Embed-сообщениях, языки, префиксы, т. д.)
<br>3. Интеграция БД SQLite с ботом вместо простого JSON
<br>4. Просмотр рандомных картинок с Unsplash и Reddit
<br>5. Погода от OpenWeatherMap API.
<br>6. Система уровней (пока только глобально)
<br>7. Написан на Python с использованием библиотек discord.py и sqlite3
<br>8. Аудиоплеер с поддержкой очередей.
<p><b>Скриншоты</b>
<p><img src="https://media.discordapp.net/attachments/787270057952542720/798878165325185084/screenshot_001.png" height="256"></img>
<img src="https://media.discordapp.net/attachments/787270057952542720/798878192193634314/screenshot_002.png" height="256"></img>
<img src="https://media.discordapp.net/attachments/787270057952542720/798878179234283520/screenshot_003.png" height="256"></img>
<p><b>Установка</b>
<p>1. Распаковывайте архив с исходными кодами бота Vision в любое место.
<br>2. Создайте файл <code>.env</code> в корневой директории для хранения одного токена к Discord API и трех токенов к Unsplash API в качестве локальных переменных терминала. Файловые системы в Linux спрячут этот файл сами (могут и не везде, так что советую создавать этот файл <b>в корневой!</b>). Формат файла <code>.env</code> увидите чуть ниже (не забывайте подменять на соответствующие токены, а узнать можно по этим ссылкам).
<pre>DTOKEN=[link: https://discord.com/developers]
UNSAKEY=[link: https://unsplash.com/developers]
UNSSKEY=[link: https://unsplash.com/developers]
UNSRDC=[link: https://unsplash.com/developers]</pre>
3. Убедитесь, что у Вас установлены необходимые пакеты. Если что, смотрите файлы - <code>bot_d.py, keep_alive.py и pyproject.toml</code>
<br>4. Авторские команды (в кодах вызовы оставлены) можно либо создавать руками, либо удалять с кода.
<br>5. Пошаманите хоть как-то... Токены в переменные вставьте, если с файлом <code>.env</code> не прокатило.
<br>6. И наконец-то запускаете.
<p>Для работы бота в круглосуточном режиме за бесплатно, рекомендуется использовать хостинг репозиториев Repl.it и пинг-сервис Freshping.
<p>Присутствуют английский и русский языки. Вопросы к работе бота направляйте через Issues.
<p><i><a href="https://discord.com/api/oauth2/authorize?client_id=785383439196487720&permissions=8&scope=bot">Добавить бота на Discord-сервер (Add bot to Discord-server)</a> | <a href="https://vk.com/tinelix">Паблик ВК (VK public group)</a> | <a href="https://repl.it/@tinelix/visionbot">"Ночной" альт-репозиторий (Nightly alt-repository)</i></a>
