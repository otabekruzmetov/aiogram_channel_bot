from googletrans import Translator
from aiogram import executor, types, Bot, Dispatcher
import logging
from loader import dp
import wikipedia
logging.basicConfig(level=logging.INFO)

translator = Translator()

@dp.message_handler()
async def get_data(message: types.Message):
    text = message.text
    await message.answer(wikipedia.summary(text))
