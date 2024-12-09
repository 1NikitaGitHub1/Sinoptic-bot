import asyncio
from aiogram import Bot, Dispatcher

from app.handlers import rt
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
  dp.include_router(rt)
  await dp.start_polling(bot)

if __name__ == "__main__":
  asyncio.run(main())