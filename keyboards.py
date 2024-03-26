from aiogram import types


class Keyboards:
    options = ["Перевод 1️⃣", "Перевод 2️⃣"]

    keyboard_pick_screenshot = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text=options[0]),
                types.KeyboardButton(text=options[1])
            ]
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Выберите скрин перевода"
    )

