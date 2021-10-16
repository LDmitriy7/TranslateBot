from aiogram import types

import api
from loader import dp


@dp.message_handler()
async def translate(msg: types.Message):
    translation = await api.translate(msg.text)
    if translation != msg.text:
        await msg.reply(translation)
