from aiogram import types

import api
from loader import dp


@dp.message_handler(content_types='any')
@dp.edited_message_handler(content_types='any')
async def translate(msg: types.Message):
    text = msg.text or msg.caption

    if not text:
        return

    translation = await api.translate(text)

    if translation != text:
        await msg.reply(translation)
