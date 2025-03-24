import logging
import openai
from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command
import asyncio

API_TOKEN = '7556075521:AAHwfW5apQJgiMgvuhYhD8ajJC6beiUl320'  # Замените на ваш Telegram API токен
OPENAI_API_KEY = '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'  # Замените на ваш OpenAI API ключ

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Создание экземпляра бота
bot = Bot(token=API_TOKEN)

# Создание экземпляра диспетчера
dp = Dispatcher()

# Создание экземпляра роутера
router = Router()

# Установка API-ключа для OpenAI
openai.api_key = OPENAI_API_KEY

async def get_ai_response(prompt: str) -> str:
    """Функция для получения ответа от модели GPT."""
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = response.choices[0].text.strip()
    return message

@router.message(Command('start'))
async def cmd_start(message: types.Message):
    """Обработчик команды /start."""
    await message.answer("Привет! Я бот с искусственным интеллектом. Задай мне вопрос.")

@router.message(Command('help'))
async def cmd_help(message: types.Message):
    """Обработчик команды /help."""
    await message.answer("Отправь мне любое сообщение, и я постараюсь на него ответить.")

@router.message()
async def echo(message: types.Message):
    """Обработчик текстовых сообщений."""
    user_message = message.text.strip()
    if user_message:
        ai_response = await get_ai_response(user_message)
        await message.answer(ai_response)
    else:
        await message.answer("Пожалуйста, отправьте текст для получения ответа.")

async def main():
    # Подключение роутера к диспетчеру
    dp.include_router(router)
    # Запуск поллинга
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
