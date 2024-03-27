import asyncio

from aiogram import F
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.context import FSMContext
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.client.telegram import TelegramAPIServer
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, FSInputFile
from aiogram.types.update import Update
from aiogram.methods import DeleteWebhook

import keyboards
import config

import features.screen_1.image_handler as image_handler_1
import features.screen_2.image_handler as image_handler_2

# session = AiohttpSession(api=TelegramAPIServer.from_base('http://localhost'))

bot = config.bot

async def main():
    dp = Dispatcher()

    dp.include_router(image_handler_1.router)
    dp.include_router(image_handler_2.router)

    greeting = "Привет! 👋 Здесь ты можешь получить скрины перевода твоего любимого (или нет) банка!\n"
    greeting = greeting + "\n" + "Платформа: Android \n"
    greeting = greeting + "\n" + "Больше фич на данный момент находятся в разработке 🛠\n"
    greeting = greeting + "\n" + "Чтобы начать, выбери один из вариантов скриншотов ниже 👇"


    @dp.message(F.chat.id == -1001870427118)
    async def ignore_my_chat(message: Message):
        return
    
    
    @dp.message(Command("start"))
    async def cmd_start(message: types.Message, state: FSMContext):
        # print(updates.pop().message.from_user.username + "\n" + updates.pop().message.chat.id)
        await config.save_user(message=message)

        await message.answer_document(FSInputFile("features/screen_1/demo_1.png"))
        await message.answer_document(FSInputFile("features/screen_2/demo_2.png"), caption=greeting, reply_markup=keyboards.Keyboards().keyboard_pick_screenshot)
        # state_name = await state.get_state()
        # print(state_name)

        await state.clear()


    @dp.message(StateFilter(None), F.is_not(Command("start")), F.text.not_in(keyboards.Keyboards.options))
    async def is_not_command(message: Message):
        await config.save_user(message=message)
        await message.reply("Я не шарю за эту команду. Чтобы начать, воспользуйтесь /start")


    await bot.delete_webhook(drop_pending_updates=True)
    # await bot.send_message(chat_id=6718228225, text="Я работаю!")
    # await bot.send_message(chat_id=-1001870427118, text="Я в чате!")
    print("Bot started")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
# asyncio.run(main())