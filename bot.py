import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from config import TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Старт
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        "Добро пожаловать! Это бот для тестирования риелторов.\n"
        "Напишите /test чтобы пройти тест."
    )

# Заглушка команды теста (пока без логики)
@dp.message_handler(commands=['test'])
async def test(message: types.Message):
    await message.answer("Тестирование скоро будет доступно. Бот настроен правильно!")

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
