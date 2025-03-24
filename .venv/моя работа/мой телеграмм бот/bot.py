import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Ваши токены
WEATHER_API_KEY = "819f3288b49edfbbeaf6b2a73121b823"
TELEGRAM_API_KEY = '7966758694:AAFPUAJj-_2KGsSPtfhe58pBe8rqyswmQEo'


# Функция получения прогноза погоды
async def get_weather(city: str) -> str:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric&lang=ru"
    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        return "Город не найден или ошибка запроса."

    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]
    return f"Температура: {temp}°C\nОписание: {description}"


# Обработчик сообщений от пользователей
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    city = update.message.text  # Получаем текст сообщения (город)
    weather_message = await get_weather(city)
    await update.message.reply_text(weather_message)


# Функция для старта
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Привет! Напиши название города, и я скажу тебе погоду!")


# Главная функция
def main():
    application = Application.builder().token(TELEGRAM_API_KEY).build()

    # Регистрируем обработчики команд и сообщений
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))  # Обработка любых сообщений
    application.add_handler(CommandHandler("start", start))

    # Запуск бота
    application.run_polling()


if __name__ == '__main__':
    main()
