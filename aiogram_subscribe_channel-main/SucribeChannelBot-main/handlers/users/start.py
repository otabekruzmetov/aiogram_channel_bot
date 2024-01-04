from aiogram import types
from data.config import CHANNELS
from keyboards.inline.subcribe import check_button
from aiogram.dispatcher.filters.builtin import CommandStart
# import logging
from utils.misc import subcribe
from loader import dp, bot


@dp.message_handler(CommandStart())
async def show_channels(message: types.Message):
    channels_format =str()
    for channel in CHANNELS:
        chat = await bot.get_chat(channel)
        invite_link = await chat.export_invite_link()
        channels_format +=f"<a href='{invite_link}'>{chat.title}</a>\n"
    await message.answer(f"Bot foydalanish uchun quyidagi kanallarga a'zo bo'ling\n"
                         f"{channels_format}",
                         reply_markup=check_button,
                         disable_web_page_preview=True)


@dp.callback_query_handler(text="check_subs")
async def checker(call: types.CallbackQuery):
    await call.answer()
    result = str()
    for channel in CHANNELS:
        status = await subcribe.check(user_id=call.from_user.id, channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            result +=f"<b>{channel.title}</b> kanaliga obuna bo'lgansiz\n\n"
        else:
            invite_link =await channel.export_invite_link()
            result += (f"<b>{channel.title} kanaliga obuna bo'lmagansiz!</b>"
                       f"<a href='{invite_link}'> Obuna bo'ling </a>\n\n")

    await call.message.answer(result, disable_web_page_preview=True)





