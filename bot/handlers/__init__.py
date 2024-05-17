"""Модуль для импорта роутеров"""
from aiogram import Dispatcher
from . import start, set_time


def include_routers(dp: Dispatcher):
    """Добавление всех роутеров в диспетчер"""
    dp.include_routers(
        start.router,
        set_time.router,
    )
