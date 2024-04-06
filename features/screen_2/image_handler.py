import time
import asyncio
import re
from features.screen_2.process import ImageProcess

from aiogram import Router, F,types
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

import keyboards
import config
from states import UserState_2, AppState

router = Router()

@router.message(F.text == keyboards.Keyboards.options[1], AppState.start_state)
async def cmd_num(message: Message, state: FSMContext):
    await config.save_user(message=message)
    await state.set_state(UserState_2.entering_num)
    
    await message.answer("Введите сумму 💰: \n(без точек и пробелов)")

@router.message(UserState_2.entering_num)
async def enter_sum(message: Message, state: FSMContext):
    num = message.text
    
    if num.isnumeric():
        num = int(num)
        await state.update_data(num=num)
        await state.set_state(UserState_2.entering_name)

        await message.answer(f"Введите данные получателя ✍: \n(прим. Иван Иванович И.)")
    else:
        await message.answer(f"❌Неверный формат строки: используйте только цифры, без пробелов и символов!")


@router.message(UserState_2.entering_name)
async def enter_name(message: Message, state: FSMContext):
    name = message.text.replace('\n', '1')
    
    if not re.findall('\d', name):
        await state.update_data(name=name)
        await state.set_state(UserState_2.entering_time)

        await message.answer(f"Введите время 🕑: \n(прим. 12:34)")

    else:
        
        await message.answer(f"❌Неверный формат строки: используйте только буквы, без цифр!")

@router.message(UserState_2.entering_time)
async def enter_name(message: Message, state: FSMContext):
    time = message.text
    
    if bool(re.match(r"[0-2][0-9]:[0-5][0-9]", time)):
        data = await state.get_data()
        num = data['num']
        name = data['name']
        await state.set_state(UserState_2.getting_result)

        await message.answer(f"Получение результата, ждите ⏳")

        # time.sleep(3.0)
        # await asyncio.sleep(3.0)
        process = ImageProcess()
        await process.process_image(name, num, time)

        # await message.answer(f"Вы ввели сумму {num}")
        output = FSInputFile("features/screen_2/output.png")
        # await message.answer_photo(output, caption="Ваша хуйня готова")
        await message.answer_document(output, caption="Ваш скриншот готов ✅", reply_markup=keyboards.Keyboards().keyboard_pick_screenshot)
        await state.set_state(AppState.start_state)

    else:
        
        await message.answer(f"❌Неверный формат строки: попробуйте еще раз!")


@router.message(UserState_2.getting_result)
async def skip_message(message: Message):
    # Скип сообщений
    return

@router.message(UserState_2.getting_result)
async def skip_command(message: Command):
    # Скип команд
    return


# @router.message()
# async def is_not_command(message: Message, state: FSMContext):
#     ustate = await state.get_state()
#     if (not ustate == None):
#         await message.reply("Я не шарю за эту команду")