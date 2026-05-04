import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from models import Base, User

# ЗАМЕНИ ЭТОТ ТЕКСТ НА СВОЙ ТОКЕН
TOKEN = "8639613156:AAEWcHXIvuP9VjSWfRS71vdQKjavZVra-xc"

engine = create_async_engine('sqlite+aiosqlite:///game.db')
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    async with async_session() as session:
        user = await session.get(User, message.from_user.id)
        if not user:
            user = User(id=message.from_user.id, nickname=message.from_user.full_name)
            session.add(user)
            await session.commit()
            msg = f"👊 Ты вступил на улицы города, {user.nickname}! Твой путь начинается с нуля."
        else:
            msg = f"🏮 С возвращением, {user.nickname}! Уровень: {user.level}"
    
    await message.answer(msg)

async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
