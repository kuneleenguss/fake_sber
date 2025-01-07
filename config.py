from aiogram import Bot
from aiogram.types import Message

class Config:
    
    def __init__(self) -> None:
        self.bot_main = Bot(token="7133511865:AAEvuZ_B02EjazcpeFNeFg4s7nOH6MTb_ts")
        self.bot_test = Bot(token="6736544153:AAEzji3KJM4C5qR1ljgfNL8ZzvgW0Zc4HKI")

    def init_bot(self, flag: str):
        match flag:
            case "test": 
                return self.bot_test
            case _:
                return self.bot_main

    async def save_user(self, message: Message, bot: Bot):
        await bot.send_message(chat_id=-1001870427118, text=f"{message.from_user.username}\n{message.chat.id}\n{message.text}")
        return
    


