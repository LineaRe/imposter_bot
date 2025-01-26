import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Загрузка токена из .env файла
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привет! Как тебя зовут?')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    name = update.message.text
    await update.message.reply_text(f'Рад познакомиться, {name}! Готов пройти тест на синдром самозванца? Напиши "Да" или "Нет".')

def main():
    # Инициализация приложения бота
    application = Application.builder().token(BOT_TOKEN).build()

    # Обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()