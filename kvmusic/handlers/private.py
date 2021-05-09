from pyrogram import Client
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import Message

from ..helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>Hellow {message.from_user.first_name}!
\nI can play music in your group's voice chat
Maintained with ❤ by @Karam_0912
\nTo add in your group contact us at @KV_NETWORK.
 </b>""",

The commands I currently support are:

/play - play the replied audio file or YouTube video
/pause - pause the audio stream
/resume - resume the audio stream
/skip - skip the current audio stream
/mute - mute the userbot
/unmute - unmute the userbot
/stop - clear the queue and remove the userbot from the call""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        'Group', url='https://t.me/KV_NETWORK',
                    ),
                    InlineKeyboardButton(
                        'Channel', url='https://t.me/KV_NETWORK',
                    ),
                ],
            ],
        ),
    )
