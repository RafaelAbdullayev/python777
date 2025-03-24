from telegram import Update
from telegram.ext import Application, MessageHandler, filters
import requests


# Функция для обработки сообщений
async def handle_message(update: Update, context) -> None:
    user_message = update.message.text.lower()  # Получаем текст сообщения пользователя

    if 'анализ' in user_message:  # Пример проверки на ключевое слово
        # Получение данных о матче (пример с использованием football-data.org)
        response = requests.get('https://api.football-data.org/v4/matches',
                                headers={'X-Auth-Token': '9dd7a1297a8b4f90abc8c2264286abfe'})
        data = response.json()

        # Анализ данных и формирование ответа
        analysis = 'Анализ матчей: '  # Пример ответа
        for match in data['matches'][:5]:  # Пример анализа первых 5 матчей
            analysis += f"{match['homeTeam']['name']} vs {match['awayTeam']['name']} - {match['score']['fullTime']['homeTeam']}:{match['score']['fullTime']['awayTeam']}\n"

        await update.message.reply_text(analysis)
    else:
        await update.message.reply_text("Привет! Напиши 'анализ' для получения данных о матчах.")


def main() -> None:
    # Создайте объект Application и передайте ему ваш токен
    application = Application.builder().token("7379808165:AAGojRVHxpswzu9zbQfnEiCVXegIl5gsG_c").build()

    # Регистрация обработчика для текстовых сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Запуск бота
    application.run_polling()


if __name__ == '__main__':
    main()
