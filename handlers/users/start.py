import re
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from data.checking import chek
from data.config import ADMINS,kanallar
from keyboards.default import *
from loader import dp,db,bot


@dp.message_handler(CommandStart(deep_link=re.compile("^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$")))
async def bot_start(message: types.Message):
    if db.select_user(user_id=message.from_user.id):
        args = message.get_args()
        if args == 'start':
            await message.answer(text=f"""✅ {message.from_user.full_name}  BluePrep'ning botiga xush kelibsiz!

        Vebinarda ishtirok etish uchun “📍 Ishtirok etish” tugmasini tanlang, referal linkingizni olib PMga qiziqadigan tanishlaringizga yuboring!.

        4ta do'stingizni taklif qilsangiz, vebinar tashkil etiladigan YOPIQ kanalning linkini olasiz. Sovg'alar esa "🎁 Gifts" bo'limida sizni kutmoqda! 

        Yopiq kanal linkini "Ma'lumotlar" bo'limidan olishingiz mumkin. 

        Barchangizga omad tilaymiz! Savollar bo'lsa, @BluePrep_admin ga murojaat qiling.
                    """, reply_markup=menu)
        elif args:
            link = db.select_video(args)
            print(link)
            for i in link:
                video = i[1]
                caption = i[2]
                if db.select_user(message.from_user.id):
                    await message.reply_video(video=video, caption=caption,
                                              reply_markup=types.InlineKeyboardMarkup().add(
                                                  types.InlineKeyboardButton("Do'stlarga yuborish  📲",
                                                                             switch_inline_query=f"{i[3]}")),
                                              disable_notification=True)
        else:
            await message.answer(text=f"""✅ {message.from_user.full_name}  BluePrep'ning botiga xush kelibsiz!

        Vebinarda ishtirok etish uchun “📍 Ishtirok etish” tugmasini tanlang, referal linkingizni olib PMga qiziqadigan tanishlaringizga yuboring!.

        4ta do'stingizni taklif qilsangiz, vebinar tashkil etiladigan YOPIQ kanalning linkini olasiz. Sovg'alar esa "🎁 Gifts" bo'limida sizni kutmoqda! 

        Yopiq kanal linkini "Ma'lumotlar" bo'limidan olishingiz mumkin. 

        Barchangizga omad tilaymiz! Savollar bo'lsa, @BluePrep_admin ga murojaat qiling.
                    """, reply_markup=menu)
    else:
        args = message.get_args()
        name = db.select_user(user_id=args)
        text = f"<b>Salom botimizga xush kelibsiz!</b>\n"\
               f"<b>Sizni <i>{name[0][2]}</i> taklif qildi!</b>"
        await message.answer(text=text)
        await bot.send_message(chat_id=args, text=f"🎉<b>Siz taklif do'stingiz <i><u>{message.from_user.full_name}</u></i> botimizga a'zo bo'ldi va sizga 3 ball taqdim etildi!</b>👏")
        try:
            db.add_user(
                user_id=message.from_user.id,
                full_name=message.from_user.full_name,
                referral=f"{args}",
                number='none',
                ball='0'
            )
            await message.answer(
                text="Telefon raqamingizni yuboring.\n\n❗️Raqamni yuborish uchun pastdagi <b>«Raqamni yuborish 📞»</b> tugmasini bosing👇",
                reply_markup=numbers)
            await Number.Add.set()
            db.update_ball(ball='3', user_id=args)
            user = db.count_users()
            matn = f"🎉 Yangi foydalanuvchi. {message.from_user.get_mention()}\n" \
                   f"🆔 ID: {message.from_user.id}\n" \
                   f"📛 Username: @{message.from_user.username}\n" \
                   f"📝 Fullname: {message.from_user.full_name}\n\n" \
                   f"📊 Bazada {user[0]} ta foydalanuvchi mavjud."
            await bot.send_message(chat_id=ADMINS[0], text=matn)
        except Exception as err:
            print(err)

            
from states.number import Number

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if db.select_user(user_id=message.from_user.id):
        args = message.get_args()
        if args == 'start':
            await message.answer(text=f"""✅ {message.from_user.full_name}  BluePrep'ning botiga xush kelibsiz!

        Vebinarda ishtirok etish uchun “📍 Ishtirok etish” tugmasini tanlang, referal linkingizni olib PMga qiziqadigan tanishlaringizga yuboring!.

        4ta do'stingizni taklif qilsangiz, vebinar tashkil etiladigan YOPIQ kanalning linkini olasiz. Sovg'alar esa "🎁 Gifts" bo'limida sizni kutmoqda! 

        Yopiq kanal linkini "Ma'lumotlar" bo'limidan olishingiz mumkin. 

        Barchangizga omad tilaymiz! Savollar bo'lsa, @BluePrep_admin ga murojaat qiling.
                    """, reply_markup=menu)
        elif args:
            print(args)
            link = db.select_video(args)
            print(link)
            for i in link:
                video = i[1]
                caption = i[2]
                if db.select_user(message.from_user.id):
                    await message.reply_video(video=video, caption=caption,
                                              reply_markup=types.InlineKeyboardMarkup().add(
                                                  types.InlineKeyboardButton("Do'stlarga yuborish  📲",
                                                                             switch_inline_query=f"{i[3]}")),
                                              disable_notification=True)

        else:
            await message.answer(text=f"""✅ {message.from_user.full_name}  BluePrep'ning botiga xush kelibsiz!

        Vebinarda ishtirok etish uchun “📍 Ishtirok etish” tugmasini tanlang, referal linkingizni olib PMga qiziqadigan tanishlaringizga yuboring!.

        4ta do'stingizni taklif qilsangiz, vebinar tashkil etiladigan YOPIQ kanalning linkini olasiz. Sovg'alar esa "🎁 Gifts" bo'limida sizni kutmoqda! 

        Yopiq kanal linkini "Ma'lumotlar" bo'limidan olishingiz mumkin. 

        Barchangizga omad tilaymiz! Savollar bo'lsa, @BluePrep_admin ga murojaat qiling.
                    """, reply_markup=menu)
    else:
        db.add_user(
            user_id=message.from_user.id,
            full_name=message.from_user.full_name,
            referral=f"",
            number='none',
            ball='0'
        )
        await message.answer(text="Telefon raqamingizni yuboring.\n\n❗️Raqamni yuborish uchun pastdagi <b>«Raqamni yuborish 📞»</b> tugmasini bosing👇",reply_markup=numbers)
        await Number.Add.set()

        user = db.count_users()
        matn = f"🎉 Yangi foydalanuvchi. {message.from_user.get_mention()}\n"\
                f"🆔 ID: {message.from_user.id}\n" \
                f"📛 Username: @{message.from_user.username}\n" \
                f"📝 Fullname: {message.from_user.full_name}\n\n" \
                f"📊 Bazada {user[0]} ta foydalanuvchi mavjud."
        await bot.send_message(chat_id=ADMINS[0], text=matn)

@dp.message_handler(state=Number.Add ,content_types=['contact'])
async def number(message: types.Message, state:FSMContext):
    if message.contact.phone_number.startswith("+998") or message.contact.phone_number.startswith("998"):
        raqam = message.contact.phone_number
        await state.update_data({'Raqam':raqam})
        royxat = await state.get_data()
        Raqam = royxat.get('Raqam')
        db.update_number(number=f"{Raqam}", user_id=message.from_user.id)
        await message.answer(text=f"""✅ {message.from_user.full_name}  BluePrep'ning botiga xush kelibsiz!

        Vebinarda ishtirok etish uchun “📍 Ishtirok etish” tugmasini tanlang, referal linkingizni olib PMga qiziqadigan tanishlaringizga yuboring!.

        4ta do'stingizni taklif qilsangiz, vebinar tashkil etiladigan YOPIQ kanalning linkini olasiz. Sovg'alar esa "🎁 Gifts" bo'limida sizni kutmoqda! 

        Yopiq kanal linkini "Ma'lumotlar" bo'limidan olishingiz mumkin. 

        Barchangizga omad tilaymiz! Savollar bo'lsa, @BluePrep_admin ga murojaat qiling.
                    """, reply_markup=menu)
        await state.finish()
    else:
        await message.answer(text="Kechirasiz tanlovda uzbek raqamlardan foydalanish kerak.")
        await state.finish()

        
