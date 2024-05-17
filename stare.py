''' Файл для запуска бота)'''
import random
import asyncio
import logging
from datetime import datetime, timedelta
from aiogram import Router
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from parset import list_of_jokes
from tok import TOKEN

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=TOKEN)
# Диспетчер
dp = Dispatcher()
router = Router()

async def send_joke(user_id, sheduled_time):
    ''' Функция для проверки текущего времени'''
    while True:
        now = datetime.now()
        if now >= sheduled_time:
            if list_of_jokes:
                random_joke = random.choice(list_of_jokes)
                list_of_jokes.remove(random_joke)
                await bot.send_message(user_id, random_joke)
            else:
                await bot.send_message(user_id, "К сожалению, у меня закончились шутки.")
            break
        await asyncio.sleep(10)


@router.message(Command("start"))
async def start_handler(message: types.Message):
    '''Хэндлер на команду /start '''
    await message.reply("Приветик. Введите время, в которое хотите получить мем (в формате ЧЧ:MM) ")


@router.message()
async def get_time(message: types.Message):
    '''' Метод отправки сообщения в указанное время'''
    try:
        time_str = message.text
        time_obj = datetime.strptime(time_str, '%H:%M')
        scheduled_time = datetime.now().replace(hour=time_obj.hour,
                                                minute=time_obj.minute, second=0)
        if scheduled_time < datetime.now():
            scheduled_time += timedelta(days=1)
        asyncio.create_task(send_joke(message.chat.id, scheduled_time))
        await message.reply(f'Шутка будет отправлена в {scheduled_time.strftime('%H:%M')}')
    except ValueError:
        await message.reply("Некорректный формат времени. \
                            Пожалуйста, введите время в формате ЧЧ:ММ")


async def main():
    ''' Запуск процесса поллинга новых апдейтов '''
    await dp.start_polling(bot)

dp.include_routers(router)

if __name__ == "__main__":
    asyncio.run(main())