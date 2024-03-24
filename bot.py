import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.fsm.context import FSMContext
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.client.telegram import TelegramAPIServer
from aiogram.filters.command import Command
from aiogram.methods import DeleteWebhook

import image_handler

# session = AiohttpSession(api=TelegramAPIServer.from_base('http://localhost'))

bot = Bot(token="7133511865:AAEvuZ_B02EjazcpeFNeFg4s7nOH6MTb_ts")
dp = Dispatcher()

dp.include_router(image_handler.router)

@dp.message(Command("start"))
async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer("Sieg Heil!")
    await state.clear()


# @dp.message()
# async def is_not_command(message: types.Message):
#     await message.reply("Я не шарю за эту команду")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    print("Bot started")
    await dp.start_polling(bot)

# if __name__ == "__main__":
#     asyncio.run(main())
asyncio.run(main())