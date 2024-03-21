import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.client.telegram import TelegramAPIServer
from aiogram.filters.command import Command

import image

# session = AiohttpSession(api=TelegramAPIServer.from_base('http://localhost'))

bot = Bot(token="7133511865:AAEvuZ_B02EjazcpeFNeFg4s7nOH6MTb_ts")
dp = Dispatcher()

dp.include_router(image.router)

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Sieg Heil!")


# @dp.message()
# async def is_not_command(message: types.Message):
#     await message.reply("Я не шарю за эту команду")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())