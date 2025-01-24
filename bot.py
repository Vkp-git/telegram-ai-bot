import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, CommandHandler, ContextTypes, filters
import openai
from config import TELEGRAM_TOKEN, OPENAI_API_KEY, MODEL_NAME, MAX_TOKENS, TEMPERATURE

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Инициализация OpenAI
openai.api_key = OPENAI_API_KEY

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /start"""
    await update.message.reply_text(
        'Привет! Я ваш ИИ-ассистент. Задайте мне любой вопрос!'
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик текстовых сообщений"""
    try:
        # Получаем сообщение пользователя
        user_message = update.message.text
        
        # Отправляем запрос к OpenAI
        response = openai.ChatCompletion.create(
            model=MODEL_NAME,
            messages=[
                {"role": "user", "content": user_message}
            ],
            max_tokens=MAX_TOKENS,
            temperature=TEMPERATURE
        )
        
        # Получаем ответ от ИИ
        ai_response = response.choices[0].message.content
        
        # Отправляем ответ пользователю
        await update.message.reply_text(ai_response)
        
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        await update.message.reply_text(
            "Извините, произошла ошибка. Попробуйте позже."
        )

def main():
    """Запуск бота"""
    # Создаем приложение
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Добавляем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()