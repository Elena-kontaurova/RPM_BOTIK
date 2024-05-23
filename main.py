"""Телеграм бот с примеров установки времени рассылки 
и алгоритмом рассылки сообщений без лишний зхапросов к БД"""
import asyncio
from datetime import time, timedelta, datetime
from aiogram import Bot, Dispatcher
from bot.handlers import include_routers
from bot.models import User
from bot.singleton import GlobalVars
from tok import TOKEN
from parse import parse_image

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def get_time_notify():
    """Получить время ближайшего уведомления"""
    now = datetime.now()
    users = User.filter(User.time > now).order_by(User.time.asc())
    if users.count() > 0:
        return (users.first()).time

async def sending_messages():
    """Рассылка сообщений"""
    GlobalVars.SEND_TIME = await get_time_notify()
    while True:
        now_time = datetime.now().time()
        now_time = time(now_time.hour, now_time.minute)
        if GlobalVars.SEND_TIME and GlobalVars.SEND_TIME == now_time:
            # рассылка уведомлений всем пользователям
            for user in User.filter(time=GlobalVars.SEND_TIME):
                pass


            GlobalVars.SEND_TIME = await get_time_notify()

        now_time = (datetime.now() + timedelta(minutes=1))
        now_time = datetime(now_time.year, now_time.month, now_time.day,
                            now_time.hour, now_time.minute)
        seconds = (now_time - datetime.now()).seconds + 1
        await asyncio.sleep(seconds)

async def update_image():
    ''' паралельный процесс'''
    while True:
        await parse_image('https://pikabu.ru/community/mem/search')
        await asyncio.sleep(3600)

async def on_startup():
    """Обертка что бы запустить параллельный процесс"""
    asyncio.create_task(update_image())
    asyncio.create_task(sending_messages())

async def main():
    '''Старт бота'''
    dp.startup.register(on_startup)
    include_routers(dp)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
