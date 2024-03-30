import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage

from redis_local import redis_client
from settings import get_environment

env = get_environment()


async def main() -> None:
    bot = Bot(env.BOT_KEY, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=RedisStorage(redis_client))

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

    await redis_client.aclose()


if __name__ == '__main__':
    asyncio.run(main())
