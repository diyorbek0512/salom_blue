from aiogram import types
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

# from data.config import kanallar
from data.checking import chek
from loader import bot, dp, db

def kanallar():
    royxats = []
    ights = db.select_channels()

    for x in ights:
        print(x)
        royxats.append(x[1])
    return royxats

class Asosiy_checking(BaseMiddleware):
    async def on_pre_process_update(self, xabar:types.Update, data:dict):
        if xabar.message:
            user_id = xabar.message.from_user.id
            if xabar.message.text in ['Raqamni yuborish 📞']:
                return
        elif xabar.callback_query:
            user_id = xabar.callback_query.from_user.id
            if xabar.callback_query.data == "tek":
                return
        else:
            return
        matn = "<b>⚠️ Kechirasiz kanallarga azo bo'lmasdan botdan foydalana olmaysiz!\n\n✔️ Botdan foydalanish uchun pastdagi kanallarga azo bo'ling va <u>'✅ Tekshirish'</u> tugmasini bosing!</b>"
        royxat = []
        dastlabki = True
        bot_info = await bot.get_me()
        try:
            args = xabar.message.text.split("/start ")[1]
            print("Keyingi so'z:", args)
            for k in kanallar() :
                print(k)
                holat = await chek(user_id=user_id, kanal=k)
                dastlabki *= holat
                kanals = await bot.get_chat(k)
                if not holat:
                    link = await kanals.export_invite_link()
                    button = [InlineKeyboardButton(text=f"{kanals.title}", url=f"{link}")]
                    royxat.append(button)
            royxat.append([InlineKeyboardButton(text="✅ Tekshirish", url=f"https://t.me/{bot_info.username}?start={args}")])
            if not dastlabki:
                await bot.send_message(chat_id=user_id, text=matn, disable_web_page_preview=True,
                                       reply_markup=InlineKeyboardMarkup(inline_keyboard=royxat))
                raise CancelHandler()
        except IndexError:
            for k in kanallar():
                print(k)
                holat = await chek(user_id=user_id, kanal=k)
                dastlabki *= holat
                kanals = await bot.get_chat(k)
                if not holat:
                    link = await kanals.export_invite_link()
                    button = [InlineKeyboardButton(text=f"{kanals.title}", url=f"{link}")]
                    royxat.append(button)
            royxat.append(
                [InlineKeyboardButton(text="✅ Tekshirish", url=f"https://t.me/{bot_info.username}?start=start")])
            if not dastlabki:
                await bot.send_message(chat_id=user_id, text=matn, disable_web_page_preview=True,
                                       reply_markup=InlineKeyboardMarkup(inline_keyboard=royxat))
                raise CancelHandler()
        except AttributeError:
            print("Xatolik: Malumotlarni olishda xatolik yuzaga keldi")

@dp.chat_member_handler()
async def chat_memberupdate(message: types.ChatMemberUpdated):
    try:
        user_id = message.from_user.id
        old = message.old_chat_member
        new = message.new_chat_member
        if new.status == "left":
            royxat = []
            dastlabki = True
            bot_info = await bot.get_me()
            old = message.old_chat_member
            new = message.new_chat_member
            for k in kanallar() :
                print(k)
                holat = await chek(user_id=user_id, kanal=k)
                dastlabki *= holat
                kanals = await bot.get_chat(k)
                if not holat:
                    link = await kanals.export_invite_link()
                    button = [InlineKeyboardButton(text=f"❌ {kanals.title}", url=f"{link}")]
                    royxat.append(button)
            royxat.append(
                [InlineKeyboardButton(text="✅ Tekshirish", url=f"https://t.me/{bot_info.username}?start=start")])
            if not dastlabki:
                await bot.send_message(new.user.id,
                                        "<b><i>❌ Siz ba'zi kanallarimizdan chiqib ketdingiz!\n"
                                        "✔️ Iltimos qaytadan kanalga obuna bo'ling va chiqib ketmang ❗️</i></b>",
                                        disable_web_page_preview=True,
                                        reply_markup=InlineKeyboardMarkup(inline_keyboard=royxat))
    except Exception as e:
        print(e)