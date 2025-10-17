from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

IELTS = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="IELTS", url="https://t.me/IELTS_theme"),
            InlineKeyboardButton(text="FULL MOCK", url="https://t.me/IELTS_CEFR_fullmock")
        ]
    ]
)

MULTILEVEL = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="MULTILEVEL", url="https://t.me/MULTILEVEL_theme"),
            InlineKeyboardButton(text="FULL MOCK", url="https://t.me/IELTS_CEFR_fullmock")
        ]
    ]
)


