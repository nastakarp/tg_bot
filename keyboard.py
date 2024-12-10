from telegram import InlineKeyboardButton, InlineKeyboardMarkup

class Keyboard:
    @staticmethod
    def create() -> InlineKeyboardMarkup:
        """Создает клавиатуру выбора категории."""
        return InlineKeyboardMarkup([
            [InlineKeyboardButton("Мотивация", callback_data="мотивация"),
             InlineKeyboardButton("Философия", callback_data="философия")],
            [InlineKeyboardButton("Мат. анализ", callback_data="матанализ")],
            [InlineKeyboardButton("Остановить бота", callback_data="stop_bot")]
        ])
