import config
import asyncio

from loguru import logger as log
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command


bot = Bot(token=config.BotDatas.token)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Прив")


async def main():
    log.success("Bot has been started.")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())