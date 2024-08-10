""""
Бот написан на aiogramm 3.11.0


"""




import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = "bot_tocken"

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привет! Я бот помогающий твоему здоровью.")
    print(f"Привет {html.bold(message.from_user.full_name)}! Я бот помогающий твоему здоровью.")


@dp.message()
async def message_handler(message: Message) -> None:
    try:
        if message.text:
            print(f"Введите команду /start, чтобы начать общение.")
            await message.answer("Введите команду /start, чтобы начать общение.")
    except:
        print("Чет не так")


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
