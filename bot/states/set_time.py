"""Модуль для состояний установки времени"""
from aiogram.fsm.state import State, StatesGroup


class SetTime(StatesGroup):
    """Состояния установки времени"""
    time = State()
