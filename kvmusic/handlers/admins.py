from asyncio import QueueEmpty

from pyrogram import Client
from pyrogram.types import Message

from .. import queues
from ..kvmusic import kvmusic
from ..helpers.decorators import authorized_users_only
from ..helpers.decorators import errors
from ..helpers.filters import command
from ..helpers.filters import other_filters


@Client.on_message(command('pause') & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
    (
        await message.reply_text('Paused!')
    ) if (
        kvmusic.pause(message.chat.id)
    ) else (
        await message.reply_text('Nothing is playing!')
    )


@Client.on_message(command('resume') & other_filters)
@errors
@authorized_users_only
async def resume(_, message: Message):
    (
        await message.reply_text('Resumed!')
    ) if (
        kvmusic.resume(message.chat.id)
    ) else (
        await message.reply_text('Nothing is paused!')
    )


@Client.on_message(command('stop') & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    if message.chat.id not in kvmusic.active_chats:
        await message.reply_text('Nothing is playing!')
    else:
        try:
            queues.clear(message.chat.id)
        except QueueEmpty:
            pass
        await kvmusic.stop(message.chat.id)
        await message.reply_text('Cleared the queue and left the call!')


@Client.on_message(command('skip') & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    if message.chat.id not in kvmusic.active_chats:
        await message.reply_text('Nothing is playing!')
    else:
        queues.task_done(message.chat.id)
        if queues.is_empty(message.chat.id):
            await kvmusic.stop(message.chat.id)
        else:
            await kvmusic.set_stream(
                message.chat.id,
                queues.get(message.chat.id)['file'],
            )
        await message.reply_text('Skipped!')


@Client.on_message(command('mute') & other_filters)
@errors
@authorized_users_only
async def mute(_, message: Message):
    result = kvmusic.mute(message.chat.id)
    (
        await message.reply_text('Muted!')
    ) if (
        result == 0
    ) else (
        await message.reply_text('Already muted!')
    ) if (
        result == 1
    ) else (
        await message.reply_text('Not in voice chat!')
    )


@Client.on_message(command('unmute') & other_filters)
@errors
@authorized_users_only
async def unmute(_, message: Message):
    result = kvmusic.unmute(message.chat.id)
    (
        await message.reply_text('Unmuted!')
    ) if (
        result == 0
    ) else (
        await message.reply_text('Not muted!')
    ) if (
        result == 1
    ) else (
        await message.reply_text('Not in voice chat!')
    )
