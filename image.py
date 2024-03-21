from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

router = Router()

class UserState(StatesGroup):
    entering_num = State()
    getting_result = State()

@router.message(Command("process"))
async def cmd_num(message: Message, state: FSMContext):
    await message.answer(
        text="Введите сумму:"
    )
    
    await state.set_state(UserState.entering_num)

@router.message(UserState.entering_num)
async def enter_sum(message: Message, state: FSMContext):
    num = message.text
    
    if num.isnumeric():
        await state.set_state(UserState.getting_result)
        await message.answer(f"Вы ввели сумму {num}")
    else:
        await message.answer(f"Неверный тип")

@router.message()
async def is_not_command(message: Message):
    await message.reply("Я не шарю за эту команду")