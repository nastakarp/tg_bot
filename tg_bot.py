import asyncio
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext
from data import QUOTES, API_TOKEN


def create_keyboard():
    """Создает клавиатуру выбора категории."""
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Мотивация", callback_data="мотивация"),
         InlineKeyboardButton("Философия", callback_data="философия")],
        [InlineKeyboardButton("Мат. анализ", callback_data="матанализ")],
        [InlineKeyboardButton("Остановить бота", callback_data="stop_bot")]
    ])


async def start(update: Update, context: CallbackContext) -> None:
    """Обработка команды /start."""
    print("Команда /start получена")  # Отладка
    reply_markup = create_keyboard()
    await update.message.reply_text(
        "Привет! Я бот 'Цитата дня'. Выберите категорию или отправьте /quote для случайной цитаты.",
        reply_markup=reply_markup
    )


async def quote(update: Update, context: CallbackContext) -> None:
    """Обработка команды /quote."""
    print("Команда /quote выполнена")  # Отладка
    category = random.choice(list(QUOTES.keys()))
    quote = random.choice(QUOTES[category])
    reply_markup = create_keyboard()
    await update.message.reply_text(
        f"Случайная цитата из категории '{category}':\n\n{quote}",
        reply_markup=reply_markup
    )


async def button_handler(update: Update, context: CallbackContext) -> None:
    """Обработка нажатий кнопок."""
    query = update.callback_query
    await query.answer()
    print(f"Нажата кнопка: {query.data}")  # Отладка
    category = query.data

    if category == "stop_bot":
        print("Остановка бота...")  # Отладка
        await query.message.reply_text("Бот остановлен. До встречи!")
        await context.application.stop()
        return

    if category in QUOTES:
        quote = random.choice(QUOTES[category])
        reply_markup = create_keyboard()
        await query.message.reply_text(
            f"Цитата из категории '{category}':\n\n{quote}",
            reply_markup=reply_markup
        )
    else:
        reply_markup = create_keyboard()
        await query.message.reply_text(
            "Категория не найдена.",
            reply_markup=reply_markup
        )


async def main():
    """Главная функция."""
    app = Application.builder().token(API_TOKEN).build()

    # Регистрация обработчиков
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("quote", quote))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Бот запущен...")
    await app.run_polling()


if __name__ == "__main__":
    import nest_asyncio
    nest_asyncio.apply()  # Исправление проблемы с событийным циклом
    asyncio.run(main())
