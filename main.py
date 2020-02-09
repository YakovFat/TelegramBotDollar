import logging
from aiogram import Bot, Dispatcher, executor, types
from key_bot import API_TOKEN, PROXY_URL
from forex_python.converter import CurrencyRates
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
# bot = Bot(token=API_TOKEN, proxy=PROXY_URL)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['usd'])
async def send_welcome(message: types.Message):
    c = CurrencyRates()
    usd = c.get_rate('USD', 'RUB')
    await message.reply(usd)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
