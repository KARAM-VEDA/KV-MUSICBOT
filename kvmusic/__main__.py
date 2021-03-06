from pyrogram import Client as Bot

from .kvmusic import run
from .config import API_HASH
from .config import API_ID
from .config import BOT_TOKEN


bot = Bot(
    ':memory:',
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins={'root': 'kvmusic.handlers'},
).start()
run()
