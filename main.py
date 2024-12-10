import asyncio
import nest_asyncio
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from bot import QuoteBot
from config import API_TOKEN

nest_asyncio.apply()  # Исправление проблемы с событийным циклом

async def main():
    """Главная функция."""
    app = Application.builder().token(API_TOKEN).build()

    bot = QuoteBot(app)

    # Регистрация обработчиков
    app.add_handler(CommandHandler("start", bot.start))
    app.add_handler(CommandHandler("quote", bot.quote))
    app.add_handler(CallbackQueryHandler(bot.button_handler))

    print("Бот запущен...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
