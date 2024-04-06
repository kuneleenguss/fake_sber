from aiogram import Bot
from aiogram.types import Message

bot = Bot(token="7133511865:AAEvuZ_B02EjazcpeFNeFg4s7nOH6MTb_ts")

async def save_user(message: Message):
    await bot.send_message(chat_id=-1001870427118, text=f"{message.from_user.username}\n{message.chat.id}\n{message.text}")
    # return