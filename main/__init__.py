#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("29777466", default=None, cast=int)
API_HASH = config("a04b3df726520026f207079aec2f9879", default=None)
BOT_TOKEN = config("8677808521:AAFOPTxHetOquXBBI5byQf6c7FRzsa440NY", default=None)
SESSION = config("BQHGXjoABmMxqKLfb7AU86vPtLbNIBGttHEjSDCoV87Ph_UM_WRZ9ZdIxVcN0i4-6CckEo3qSXw7WRa_Zgj-OZjTVWtRtwFEpAmsvbhUHnQzv7u32dpENOs5DTR0mREjfdlPkcgbrQgLv6-BGcTiDgdmTriyYoigC-_gFcNaqYFkBcrtToBAjaf0XJDXgrxGXoeLAYk3PvgiGYw8HTH117tQ0jPpA7P63HTDNbopuL-CjyXlr-nURojIjAJiSGZofqqdRSlIpxg5knjTFE2ejorLsHitaBO7veaijkGg06yN-Yu7mrwX98ZyBfBq62rKK-wXQ5tR20ISEYcc8Qn07RuXGx6oowAAAAA1FSa2AA", default=None)
FORCESUB = config("8399557684", default=None)
AUTH = config("8399557684", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
