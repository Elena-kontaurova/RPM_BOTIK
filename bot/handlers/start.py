"""Модуль обработки команды старт"""
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import BotCommand, Message
from bot.models import User


router = Router()

@router.message(Command("start"))
async def start_handler(message: Message):
    """Обработчик команды старт"""
    User.get_or_create(tg_user=message.from_user.id)
    await message.bot.set_my_commands([
        BotCommand(command='start', description='Запуск бота'),
        BotCommand(command='set_time', description='Задать время рассылки')
    ])
    await message.answer("Привет дорогой пользователь")
