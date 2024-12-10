import random
from telegram import Update
from telegram.ext import CallbackContext
from keyboard import Keyboard
from data import QUOTES


class QuoteBot:
    def __init__(self, application):
        self.application = application

    async def start(self, update: Update, context: CallbackContext) -> None:
        """Обработка команды /start."""
        print("Команда /start получена")
        reply_markup = Keyboard.create()
        await update.message.reply_text(
            "Привет! Я бот 'Цитата дня'. Выберите категорию или отправьте /quote для случайной цитаты.",
            reply_markup=reply_markup
        )

    async def quote(self, update: Update, context: CallbackContext) -> None:
        """Обработка команды /quote."""
        print("Команда /quote выполнена")
        category = random.choice(list(QUOTES.keys()))
        quote = random.choice(QUOTES[category])
        reply_markup = Keyboard.create()
        await update.message.reply_text(
            f"Случайная цитата из категории '{category}':\n\n{quote}",
            reply_markup=reply_markup
        )

    async def button_handler(self, update: Update, context: CallbackContext) -> None:
        """Обработка нажатий кнопок."""
        query = update.callback_query
        await query.answer()
        print(f"Нажата кнопка: {query.data}")
        category = query.data

        if category == "stop_bot":
            print("Остановка бота...")
            await query.message.reply_text("Бот остановлен. До встречи!")
            await self.application.stop()
            return

        if category in QUOTES:
            quote = random.choice(QUOTES[category])
            reply_markup = Keyboard.create()
            await query.message.reply_text(
                f"Цитата из категории '{category}':\n\n{quote}",
                reply_markup=reply_markup
            )
        else:
            reply_markup = Keyboard.create()
            await query.message.reply_text(
                "Категория не найдена.",
                reply_markup=reply_markup
            )
