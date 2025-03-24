import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update: Update, _: CallbackContext) -> None:
    update.message.reply_text('Привет! Я бот с искусственным интеллектом. Чем могу помочь?')

def help_command(update: Update, _: CallbackContext) -> None:
    update.message.reply_text('Отправьте мне сообщение, и я постараюсь на него ответить.')

def handle_message(update: Update, _: CallbackContext) -> None:
    user_message = update.message.text
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_message,
        max_tokens=150
    )
    ai_message = response.choices[0].text.strip()
    update.message.reply_text(ai_message)

def main() -> None:
    updater = Updater("7556075521:AAHwfW5apQJgiMgvuhYhD8ajJC6beiUl320")

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
