from aiogram import types
from data.config import kanalar
from keyboards.default import *
from loader import dp,dp,bot


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    pass
