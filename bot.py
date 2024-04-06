import asyncio

from aiogram import F
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.client.telegram import TelegramAPIServer
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, FSInputFile
from aiogram.types.update import Update
from aiogram.methods import DeleteWebhook
from aiogram.enums import ParseMode

import keyboards
import config

import features.screen_1.image_handler as image_handler_1
import features.screen_2.image_handler as image_handler_2

import filters
from states import AppState

# session = AiohttpSession(api=TelegramAPIServer.from_base('http://localhost'))

bot = config.bot

async def main():
    dp = Dispatcher()

    dp.include_router(image_handler_1.router)
    dp.include_router(image_handler_2.router)

    greeting = "Привет! 👋 Здесь ты можешь получить скрины перевода твоего любимого (или нет) банка!\n"
    greeting = greeting + "\n" + "Платформа: Android \n"
    greeting = greeting + "\n" + "Больше фич на данный момент находятся в разработке 🛠\n"
    greeting = greeting + "\n" + "🔔<b>Подпишись на канал и будь в курсе обновлений: @GDC_24</b>\n"
    greeting = greeting + "\n" + "Чтобы начать, выбери один из вариантов скриншотов ниже 👇"


    @dp.message(F.chat.id == -1001870427118)
    async def ignore_my_chat(message: Message):
        return
    
    
    @dp.message(Command("start"), filters.SubscribeFilter(bot=config.bot))
    async def cmd_start(message: types.Message, state: FSMContext, isMember: bool):
        # print(updates.pop().message.from_user.username + "\n" + updates.pop().message.chat.id)
        # LEFT, MEMBER
        await config.save_user(message=message)

        if isMember:
            await message.answer_document(FSInputFile("features/screen_1/demo_1.png"))
            await message.answer_document(FSInputFile("features/screen_2/demo_2.png"))
            await message.answer(greeting, reply_markup=keyboards.Keyboards().keyboard_pick_screenshot, parse_mode=ParseMode.HTML)
            # state_name = await state.get_state()
            # print(state_name)

            await state.set_state(AppState.start_state)
        else:
            await message.answer("<b>Чтобы начать, подпишись на канал! @GDC_24</b> \n \nНажмите /start, чтобы обновить", parse_mode=ParseMode.HTML)
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