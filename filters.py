from typing import Union, Dict, Any

from aiogram import Bot
from aiogram.filters import BaseFilter
from aiogram.types import Message


class SubscribeFilter(BaseFilter):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    async def __call__(self, message: Message) -> Union[bool, Dict[str, Any]]:
        user_id = message.from_user.id
        print(user_id)
        member = await self.bot.get_chat_member(chat_id="@GDC_24", user_id=user_id)
        print(member.status.name)
        status = member.status.name
        if status == 'LEFT' or status == 'KICKED' or status == 'RESTRICTED':
            return {"isMember": False}
        else:
            return {"isMember": True}