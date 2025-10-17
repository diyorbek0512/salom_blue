from aiogram import types

from keyboards.default import darsliklar, menu
from keyboards.inline import MULTILEVEL, IELTS
from loader import dp, db

@dp.message_handler(text="📔 Darsliklar 📚")
async def dars(message: types.Message):
    await message.answer(
        text="Kerakli Tugmaga Bosing",
        reply_markup=darsliklar
    )

@dp.message_handler(text="⬅️ Ortga")
async def dars(message: types.Message):
    await message.answer(
        text="Kerakli Tugmaga Bosing",
        reply_markup=menu
    )

@dp.message_handler(text="IELTS")
async def dars(message: types.Message):
    await message.answer(
        text="Kerakli Tugmaga Bosing",
        reply_markup=IELTS
    )

@dp.message_handler(text="MULTILEVEL")
async def dars(message: types.Message):
    await message.answer(
        text="Kerakli Tugmaga Bosing",
        reply_markup=MULTILEVEL
    )