from aiogram.fsm.state import State, StatesGroup

class AppState(StatesGroup):
    #Start
    start_state = State()

class UserState_1(StatesGroup):
    #Screen 1
    entering_num = State()
    entering_name = State()
    entering_time = State()
    getting_result = State()

class UserState_2(StatesGroup):
    #Screen 2
    entering_num = State()
    entering_name = State()
    entering_time = State()
    getting_result = State()