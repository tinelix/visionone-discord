<h1>Vision Bot</h1>
<p>Разработан Тинеликсом в качестве замены бота Highflash. Доступен на данный момент для Discord.<br>
<i>Лицензируется с условиями GNU Affero General Public License версии 3 для веб-приложений.</i>
<p><b>Преимущества перед Highflash</b>
<p>1. Счетчик сообщений
<br>2. Гибкость настроек (часовые пояса, цвета в Embed-сообщениях, языки, т. д.)
<br>3. Интеграция БД SQLite с ботом вместо простого JSON
<br>4. Просмотр рандомных картинок с Unsplash (с оговорками)
<br>5. Написан на Python с использованием библиотек discord.py и sqlite3
<p><b>Скриншоты</b>
<p><img src="https://media.discordapp.net/attachments/794585820312633354/794964876400525332/screenshot_001.png" height="256"></img>
<img src="https://media.discordapp.net/attachments/794585820312633354/794964890414612490/screenshot_002.png" height="256"></img>
<img src="https://media.discordapp.net/attachments/794585820312633354/794964896558743582/screenshot_003.png" height="256"></img>
<p><b>Установка</b>
<p>1. Распаковывайте архив с исходными кодами бота Vision в любое место.
<br>2. Создайте файл <code>.env</code> в корневой директории для хранения одного токена к Discord API и трех токенов к Unsplash API в качестве локальных переменных терминала. Файловые системы в Linux спрячут этот файл сами (могут и не везде, так что советую создавать этот файл <b>в корневой!</b>)
<br>3. Убедитесь, что у Вас установлены необходимые пакеты. Если что, смотрите файлы - <code>bot_d.py</code>, <code>keep_alive.py</code> и <code>pyproject.toml</code>
<br>4. Пошаманить хоть как-то...
<br>5. И наконец-то запускаем.
<br>Для работы бота в круглосуточном режиме, рекомендуется использовать хостинг репозиториев Repl.it и пинг-сервис Freshping.
<pre>DTOKEN=[link: https://discord.com/developers]<br>
UNSAKEY=[link: https://unsplash.com/developers]<br>
UNSSKEY=[link: https://unsplash.com/developers]<br>
UNSRDC=[link: https://unsplash.com/developers]</pre>
<p>Присутствуют английский и русский языки. Вопросы к работе бота направляйте через Issues.
<p><i><a href="https://discord.com/api/oauth2/authorize?client_id=785383439196487720&permissions=8&scope=bot">Добавить бота на Discord-сервер</a> | <a href="https://vk.com/tinelix">Паблик ВК</a> | <a href="https://repl.it/@tinelix/visionbot">"Ночной" альт-репозиторий</i></a>
