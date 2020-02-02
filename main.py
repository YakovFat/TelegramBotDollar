import logging
import requests
from bs4 import BeautifulSoup
from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = ''
PROXY_URL = ''

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN, proxy=PROXY_URL)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
