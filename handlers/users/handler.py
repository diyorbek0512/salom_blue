from aiogram import types
from aiogram.utils.deep_linking import get_start_link
from aiogram.utils.markdown import quote_html, hbold
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp,db,bot
from data import config

@dp.message_handler(text='👤 Ma\'lumotlar')
async def balans(message: types.Message):
    balans = db.select_user(message.from_user.id)
    text = f"Sizning ballgiz: {balans[0][4]} \n"
    text += f"Sizning id <code>{message.from_user.id}</code>\n"
    text += f"👥<b>Taklif qilgan do'stlaringiz:</b> <code>{len(db.get_invited(referral=message.from_user.id))}</code> odam\n"
    text += f"📱<b>Hisob raqamingiz:</b> {balans[0][5]}"
    kb = InlineKeyboardMarkup().add(
        InlineKeyboardButton(text="🔐 Kanal havolasini olish", callback_data="get_channel_link")
    )
    await bot.send_message(message.from_user.id, text=text, reply_markup=kb)

'''@dp.message_handler(text='🔗 Ishtirok etish')
async def Money(message: types.Message):
    user_id = message.from_user.id
    link = await get_start_link(user_id)
    bot_get = await bot.get_me()
    await message.answer(f"<b>🎈 <a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a> unikal havola-taklifnomasi.</b>\n\n"
                        f"<b>👇 Boshlash uchun bosing:</b>\n")'''
    

@dp.message_handler(text='📍 Ishtirok etish')
async def Money(message: types.Message):
    user_id = message.from_user.id
    link = await get_start_link(user_id)
    bot_get = await bot.get_me()

    
    
    await message.answer_media_group(media=[
        types.InputMediaPhoto(media="https://t.me/olovli_buyruq/12"),
        types.InputMediaPhoto(media="https://t.me/olovli_buyruq/6")
    ])
    
    await message.answer(f"""
🎓 <b>Prezident Maktabi — endi orzuligicha qolmaydi!</b>  
BluePrep sizni <b>BEPUL Live Vebinarga</b> taklif qiladi  
(Prezident Maktabi bitiruvchilaridan hech kim aytmagan <b>SIRLAR</b>ni bilib oling 💡)

📅 <b>Sana:</b> 21-oktabr, 2025  
🕒 <b>Vaqt:</b> 20:00

🎙 <b>Mehmonlarimiz:</b>  
👨‍🎓 <b>Diyorbek Bahodirov</b> — Prezident maktabiga IKKALA BOSQICHdan ham 1-o‘rinda o'tgan, "BluePrep"ning ham-asoschisi, Xalqaro StemCo matematika olimpiadasining "Oltin" medali sohibi, hozirda Toshkent Xalqaro Vestminster universitetida 2-bosqich talabasi.  
👩‍🎓 <b>Laylo Xoshimboyeva</b> — Prezident maktabi bitiruvchisi, 1 yilda 18 nafar o‘quvchilarni Prezident Maktabida o‘qishida shaxsiy metodikasi orqali hissa qo‘shgan, hozirda Yangi O‘zbekiston universitetining 3-bosqich talabasi.  

🔥 <b>Eksklyuziv Vebinarda sizni nimalar kutmoqda:</b>  
💥 PM bitiruvchilarining ishlatgan va kitobda tilga olinmaydigan usullari  
💥 1-o‘rinni olish imkoniyatini yaratadigan aniq fikrlash tarzi va kundalik odatlar  
💥 Tanqidiy fikrlash & matematika savollarining javobini 92%+ to‘g‘ri topish sirlari  
💥 Nega BluePrep o‘quvchilari doimo oldinda?

🎁🎉 <b><u>BONUS (vebinardagi barcha imkoniyatlardan tashqari):</u></b>  
1️⃣ TOP-3 eng ko‘p Prezident Maktabiga qiziquvchi tanishlariga tarqatgan kishilarga — 3 oylik Telegram PREMIUM + PM bitiruvchilaridan tekinga shaxsiy konsultatsiya.  
2️⃣ Vebinar so‘ngida ingliz tili savollari uchun ENG kerakli bo‘ladigan 400 ta so‘z va tarjimalar to‘plangan PDF.  
3️⃣ TOP-7 eng ko‘p Prezident Maktabiga qiziquvchi tanishlariga tarqatgan kishilarga — PM bitiruvchilaridan bepul shaxsiy konsultatsiya.   

🔥 <b>Hayotingizni o‘zgartirishi mumkin bo‘lgan OXIRGI IMKONIYATdan QURUQ QOLMANG!</b>  

<b>Joyingizni hoziroq band qiling👇:</b>  
👉 <a href="{link}">{link}</a>  

<a href="{link}"><b>[start]</b></a> - <a href="{link}"><b>[start]</b></a> - <a href="{link}"><b>[start]</b></a>
""",
    parse_mode="HTML")




    '''await message.answer_photo(photo="https://t.me/olovli_buyruq/9",caption=f"""
🎓 <b>Prezident Maktabi — endi orzuligicha qolmaydi!</b>  
BluePrep sizni <b>BEPUL Live Vebinarga</b> taklif qiladi  
(Prezident Maktabi bitiruvchilaridan hech kim aytmagan <b>SIRLAR</b>ni bilib oling 💡)

📅 <b>Sana:</b> 21-oktabr, 2025  
🕒 <b>Vaqt:</b> 20:00

🎙 <b>Mehmonlarimiz:</b>  
👨‍🎓 <b>Diyorbek Bahodirov</b> — Prezident maktabiga IKKALA BOSQICHdan ham 1-o‘rinda o'tgan, "BluePrep"ning ham-asoschisi, Xalqaro StemCo matematika olimpiadasining "Oltin" medali sohibi, hozirda Toshkent Xalqaro Vestminster universitetida 2-bosqich talabasi.  
👩‍🎓 <b>Laylo Hoshimova</b> — Prezident maktabi bitiruvchisi, 1 yilda 18 nafar o‘quvchilarni Prezident Maktabida o‘qishida shaxsiy metodikasi orqali hissa qo‘shgan, hozirda Yangi O‘zbekiston universitetining 3-bosqich talabasi.  

🔥 <b>Eksklyuziv Vebinarda sizni nimalar kutmoqda:</b>  
💥 PM bitiruvchilarining ishlatgan va kitobda tilga olinmaydigan usullari  
💥 1-o‘rinni olish imkoniyatini yaratadigan aniq fikrlash tarzi va kundalik odatlar  
💥 Tanqidiy fikrlash & matematika savollarining javobini 92%+ to‘g‘ri topish sirlari  
💥 Nega BluePrep o‘quvchilari doimo oldinda?

🎁🎉 <b><u>BONUS (vebinardagi barcha imkoniyatlardan tashqari):</u></b>  
1️⃣ TOP-3 eng ko‘p Prezident Maktabiga qiziquvchi tanishlariga tarqatgan kishilarga — 3 oylik Telegram PREMIUM + PM bitiruvchilaridan tekinga shaxsiy konsultatsiya.  
2️⃣ Vebinar so‘ngida ingliz tili savollari uchun ENG kerakli bo‘ladigan 400 ta so‘z va tarjimalar to‘plangan PDF.  
3️⃣ TOP-7 eng ko‘p Prezident Maktabiga qiziquvchi tanishlariga tarqatgan kishilarga — PM bitiruvchilaridan bepul shaxsiy konsultatsiya.  

🔗 <b>Ishtirok etish tartibi:</b>  
1️⃣ Quyidagi botga kiring 👉 {link}  
2️⃣ Botdagi havola orqali 5 ta do‘stingizni taklif qiling  
3️⃣ 5 nafar do‘stingiz qo‘shilgach, sizga yopiq kanal havolasi yuboriladi 🎯  

🔥 <b>Hayotingizni o‘zgartirishi mumkin bo‘lgan OXIRGI IMKONIYATdan QURUQ QOLMANG!</b>  

<b>Joyingizni hoziroq band qiling👇:</b>  
👉 <a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a> — {link}
        """,
        parse_mode="HTML")'''


   
@dp.inline_handler()
async def referals(inline_query: types.InlineQuery):
    user_id =inline_query.from_user.id
    link = await get_start_link(user_id)
    bot_get = await bot.get_me()
    text = f"{link}"

    input_content = types.InputTextMessageContent(text,disable_web_page_preview=True)
    inl = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("✅ Boshlash ✅", url=f"{link}"))
    referal = types.InlineQueryResultArticle(
        id='01',
        thumb_url=None,
        title="Do'stlarga yuborish 📲",
        description="Do'stlarga yuborish uchun shu yerni bosing",
        input_message_content=input_content,
        reply_markup=inl,
    )
    lis = [referal]
    msg = await inline_query.answer(results=lis, cache_time=1)


@dp.callback_query_handler(text="get_channel_link")
async def get_channel_link(call: types.CallbackQuery):
    user_id = call.from_user.id
    # count invited users using new helper
    invited_count = db.count_invited(referral=user_id)

    # check whether link already granted (and not expired)
    granted = db.is_link_granted(user_id)
    if granted and granted[0] and granted[0] == 1:
        link = granted[1] if len(granted) > 1 else None
        await call.answer("Siz havolani oldingiz — tekshiring chatda.", show_alert=True)
        if link:
            await bot.send_message(user_id, text=f"Sizga berilgan kanal havolasi: {link}")
        return

    required = 4
    if invited_count < required:
        await call.answer(f"Siz hozircha {invited_count} ta odam taklif qilgansiz. {required - invited_count} ta odam yetishmayapti.", show_alert=True)
        return

    # enough invites — create an expiring one-time invite link
    try:
        channel = config.video_kanal[0] if hasattr(config, 'video_kanal') and config.video_kanal else None
        if not channel:
            await call.answer("Kanal sozlanmagan. Admin bilan bog'laning.", show_alert=True)
            return

        import time
        # try to use create_chat_invite_link (if Bot API + aiogram version supports it) for member_limit=1 and 24h expiry
        expire_seconds = 60 * 60 * 24  # 24 hours
        expire_at = int(time.time()) + expire_seconds
        chat_link = None
        try:
            # create_chat_invite_link returns a ChatInviteLink object
            cil = await bot.create_chat_invite_link(chat_id=channel, expire_date=expire_at, member_limit=1)
            chat_link = cil.invite_link if hasattr(cil, 'invite_link') else str(cil)
        except Exception:
            # fallback to export_chat_invite_link (non-expiring) if create not supported
            chat_link = await bot.export_chat_invite_link(chat_id=channel)
            # if fallback used, set a reasonable expiry (e.g., 24h) in DB so it won't be re-granted after expiry

        # store link and expiry
        db.grant_invite_link(user_id=user_id, link=chat_link, granted_at=int(time.time()), expire_at=expire_at)
        await call.answer("Sizga kanal havolasi yuborildi.", show_alert=True)
        await bot.send_message(user_id, text=f"Sizning yopiq kanal havolangiz: {chat_link}")
    except Exception as err:
        await call.answer("Havola yaratishda xatolik: admin huquqlari yo'q yoki boshqa xatolik.", show_alert=True)
        print('Error creating invite link:', err)


@dp.message_handler(text="📊 Reyting")
async def delete(message: types.Message):
    top = db.top()
    balans = db.select_user(message.from_user.id)
    text = "📊 Eng yuqori ball to‘plaganlar:\n\n"

    if len(top) > 0:
        for n, row in enumerate(top, start=1):
            # Suppose your table columns are (id, user_id, name, username, score)
            name = row[2]   # adjust index based on db.top() result
            score = row[4]
            text += f"{hbold(n)}. {name}, {score} ball\n"

    await message.reply(
        text=f"{text}\n\nSizning balingiz: {balans[0][4]}",
        parse_mode="HTML"
    )


@dp.message_handler(text="🎁 Gifts")
async def delete(message: types.Message):
    sovga = db.select_sovga(id=1)
    if not sovga:
        await message.reply(text="Hozircha sovg'alar mavjud emas.")
        return
    await message.reply(text=f"{sovga[0][1]}")

@dp.message_handler(text="💡 Shartlar")
async def shartlar(message: types.Message):
    await message.answer(text="""Vebinarda qatnashish shartlari juda ham oddiy ✅

Shaxsiy havolangizni prezident maktabiga qiziqishi bo'lgan tanishlaringizga ulashing va ularning ham qatnashishlarini so'rang.
                         
Har bir taklif qilingan ishtirokchi uchun sizga 1 ball beriladi
                         
Umumiy 4ta do'stingizni taklif qilsangiz, vebinar tashkil etiladigan YOPIQ kanalning linkini olasiz.
                         
Sizni vebinarda kutib qolamiz 😊""")
