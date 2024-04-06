from aiogram import Bot
from aiogram.types import Message

bot = Bot(token="6736544153:AAEzji3KJM4C5qR1ljgfNL8ZzvgW0Zc4HKI")

async def save_user(message: Message):
    # await bot.send_message(chat_id=-1001870427118, text=f"{message.from_user.username}\n{message.chat.id}\n{message.text}")
    return