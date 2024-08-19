from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import asyncio
api = "7450958579:AAG0jdKJhXpLLobfpGgMraO3o_3mgjBjVFw"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

# Клавиатура по тексту
kb_inline = InlineKeyboardMarkup()
inline_button1 = InlineKeyboardButton(text="information", callback_data='info')
kb_inline.add(inline_button1)

@dp.message_handler(commands=['start2'])
async def starter(message):
    await message.answer("Это инлайн кнопка",  reply_markup =kb_inline)

@dp.callback_query_handler(text = 'info')
async def infor(call):
    print('приииив')
    await call.message.answer("Информация о боте инлайн")
    await call.answer()

# Клавиатура снизу
kb= ReplyKeyboardMarkup()
button1 =KeyboardButton(text="Информация")
button2 =KeyboardButton(text="Начало")
kb.add(button1)
kb.add(button2)

@dp.message_handler(commands=['start'])
async  def start(message):
    await message.answer("Привет!", reply_markup =kb)

@dp.message_handler(text = 'Информация')
async def inform(message):
    await message.answer('Информация о боте')



if __name__== "__main__":
    executor.start_polling(dp,skip_updates=True)



