import asyncio
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

bot = Bot(token="8441532759:AAFiT6OoA2ZH9ND24ArCqW2_5YoHh3ljjy4")
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    args = message.text.split()
    if len(args) > 1:
        user_id = args[1]
        telegram_id = message.from_user.id

        try:
            response = requests.post(
                "http://127.0.0.1:8000/api/save/",
                json={
                    "telegram_id": telegram_id,
                    "user_id": user_id
                },
                timeout=5
            )

            if response.status_code == 200:
                await message.answer("✅ Your Telegram ID has been saved successfully!")
            else:
                await message.answer(f"⚠️ Server returned error: {response.text}")

        except Exception as e:
            await message.answer(f"❌ Error connecting to server: {e}")
    else:
        await message.answer("Usage: /start <your user_id>")



async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
