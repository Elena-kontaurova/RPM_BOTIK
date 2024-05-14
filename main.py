''' Файл для запуска бота - анкеты)'''
import random
import asyncio
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.filters.command import Command
from datetime import datetime, timedelta
from parset import list_of_del

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="7069139093:AAHGMroYwnQgEBXwxRRFuUJ5hgSmRVOHoDQ")
# Диспетчер
dp = Dispatcher()

async def send_joke(user_id, sheduled_time):
    while True:
        now = datetime.now()
        if now >= sheduled_time:
            list_of_dels = list_of_del[random.randint(0, len(list_of_del) - 1)]
            await bot.send_message(user_id, list_of_dels)
            break
        await asyncio.sleep(10)


@dp.message_handler(command = ['start'])
async def start(message: types.Message):
    '''Хэндлер на команду /start '''
    await message.reply("Приветик? Введите время, в которое хотите получить мем (в формате ЧЧ:MM) ")


@dp.message_handler()
async def 


async def main():
    ''' Запуск процесса поллинга новых апдейтов '''
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
