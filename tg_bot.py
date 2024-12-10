import asyncio
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext

# Список цитат
QUOTES = {
    "motivation": [
        "Делай сегодня то, что другие не хотят, завтра будешь жить так, как другие не могут.",
        "Успех приходит к тем, кто верит в свои мечты.",
        "Трудности закаляют сильных."
    ],
    "philosophy": [
        "Познай самого себя, и ты познаешь весь мир и богов. — Сократ",
        "Единственная истинная мудрость — это знание о том, что ты ничего не знаешь. — Сократ",
        "Смысл жизни не в том, чтобы быть счастливым. Он в том, чтобы быть полезным, достойным уважения и сострадания."
    ],
    "math": [
        "Математика — это язык, на котором написана книга природы. — Галилей",
        "Красота математики заключается в том, что она никогда не лжёт.",
        "Математика — это поэзия логики."
    ]
}

async def start(update: Update, context: CallbackContext) -> None:
    """Обработка команды /start."""
    print("Команда /start получена")  # Отладка
    keyboard = [
        [InlineKeyboardButton("Мотивация", callback_data="motivation"),
         InlineKeyboardButton("Философия", callback_data="philosophy")],
        [InlineKeyboardButton("Мат. анализ", callback_data="math")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Привет! Я бот 'Цитата дня'. Выберите категорию или отправьте /quote для случайной цитаты.",
        reply_markup=reply_markup
    )

async def quote(update: Update, context: CallbackContext) -> None:
    """Обработка команды /quote."""
    print("Команда /quote выполнена")  # Отладка
    category = random.choice(list(QUOTES.keys()))
    quote = random.choice(QUOTES[category])
    await update.message.reply_text(f"Случайная цитата из категории '{category}':\n\n{quote}")

async def button_handler(update: Update, context: CallbackContext) -> None:
    """Обработка нажатий кнопок."""
    query = update.callback_query
    await query.answer()
    print(f"Нажата кнопка: {query.data}")  # Отладка
    category = query.data
    if category in QUOTES:
        quote = random.choice(QUOTES[category])
        await query.edit_message_text(f"Цитата из категории '{category}':\n\n{quote}")
    else:
        await query.edit_message_text("Категория не найдена.")

async def main():
    """Главная функция."""
    app = Application.builder().token("7653160844:AAG-hYAnG_2YWRnfEOvZw9Ir_oNkhlGETGA").build()

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
