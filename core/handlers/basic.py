from aiogram import Bot
from aiogram.types import CallbackQuery, FSInputFile, InputMediaPhoto, Message, LabeledPrice, PreCheckoutQuery
from core.handlers.messages import *
from core.keyboards.inline import go_to_menu_inline_keyboard
from database.db import Db
from core.settings import settings
from datetime import datetime


async def get_start(message: Message, bot: Bot):
    db = Db()
    created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(created_at)
    await db.save_user(message.from_user.id, message.from_user.username, message.from_user.first_name, created_at,
                       message.from_user.last_name)
    await message.answer(text=WELLCOME_MESSAGE, reply_markup=go_to_menu_inline_keyboard)


async def chat_with_client(message: Message, bot: Bot):
    command_parts = message.text.split(' ')
    if len(command_parts) < 2:
        await bot.send_message(text='Missing user ID.', chat_id=settings.bots.admin_id)
        return

    client_id = command_parts[1]
    await bot.send_message(text=f'{client_id}', chat_id=settings.bots.admin_id)

    admin_id = settings.bots.admin_id
    if message.from_user.id == admin_id:
        await bot.send_message(text=f'Chat with client {client_id} started!', chat_id=admin_id)
        while message.from_user != 'stop':
            _id = int(command_parts[1])
            await bot.forward_message(chat_id=_id, from_chat_id=admin_id, message_id=message.message_id)


async def forwar_admin_message(message: Message, bot: Bot, client_id: int):
    await bot.send_message(text=message.text, chat_id=client_id)
