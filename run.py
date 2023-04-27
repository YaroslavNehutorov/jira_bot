from aiogram.utils import executor
from bot.loader import dp
from bot import handlers


def run():
    executor.start_polling(skip_updates=True, dispatcher=dp)


if __name__ == '__main__':
    run()
