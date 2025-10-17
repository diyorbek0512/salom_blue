from aiogram import types
from data.config import ADMINS,kanallar
from loader import dp,db,bot
from keyboards.admin import *
from aiogram.dispatcher import FSMContext
from asyncio import sleep


from aiogram.dispatcher.filters.state import StatesGroup, State


class UserForwardState(StatesGroup):
    post = State()

class UserCopyState(StatesGroup):
    post = State()
    
class Users(StatesGroup):
    user = State()

class SuperAdminState(StatesGroup):
    SUPER_ADMIN_ADD_CHANNEL = State()
    SUPER_ADMIN_UPDATE_SOVGA= State()
    SUPER_ADMIN_UPDATE_SOVGA1 = State()
    SUPER_ADMIN_UPDATE_PHOTO = State()


# Admin panelga kirish uchun kommanda

@dp.message_handler(commands=['admin','panel'], chat_id = ADMINS[0])
async def admin_panel(message: types.Message):
    await message.answer("Admin panelga xush kelibsiz!",reply_markup=panel)

# Admin paneldan chiqish uchun kommanda

@dp.callback_query_handler(text = "close_panel", chat_id = ADMINS[0])
async def close_panel(call: types.CallbackQuery):
    await call.message.delete()

@dp.callback_query_handler(text = "back", chat_id = ADMINS[0])
async def back_handler(call: types.CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=panel)

#ball
@dp.callback_query_handler(text="update_ball",chat_id=ADMINS[0])
async def update_ball(call: types.CallbackQuery):
    db.update_all_balls()
    await call.message.answer("Yangilandi",reply_markup=panel)
#ball

# MAJBURIY OBUNA SOZLASH UCHUN
@dp.callback_query_handler(text = "add_channel")
async def add_channel(call: types.CallbackQuery):
    await SuperAdminState.SUPER_ADMIN_ADD_CHANNEL.set()
    await call.message.edit_text(text="<i><b>📛 Kanal usernamesini yoki ID sini kiriting: </b></i>")
    await call.message.edit_reply_markup(reply_markup=back_to_main_menu)


@dp.message_handler(state=SuperAdminState.SUPER_ADMIN_ADD_CHANNEL)
async def add_channel(message: types.Message, state: FSMContext):
    matn = message.text
    if matn.isdigit() or matn.startswith("@"):
        try:
            if db.check_channel(channel=message.text):
                await message.answer("<i>❌Bu kanal qo'shilgan! Boshqa kanal qo'shing!</i>", reply_markup=back_to_main_menu)
            else:
                try:
                    deeellll = await bot.send_message(chat_id=message.text, text=".")
                    await bot.delete_message(chat_id=message.text, message_id=deeellll.message_id)
                    try:
                        db.add_channel(channel=message.text)
                    except:
                        pass
                    await message.answer("<i><b>Channel succesfully added ✅</b></i>")
                    await message.answer("<i>Siz admin panelidasiz. 🧑‍💻</i>", reply_markup=panel)
                    await state.finish()
                except:
                    await message.reply("""<i><b>
Bu kanalda admin emasman!⚙️
Yoki siz kiritgan username ga ega kanal mavjud emas! ❌
Kanalga admin qilib qaytadan urinib ko'ring yoki to'g'ri username kiriting.🔁
                    </b></i>""", reply_markup=back_to_main_menu)
        except Exception as err:
            await message.answer(f"Xatolik ketdi: {err}")
            await state.finish()
    else:
        await message.answer("Xato kiritdingiz.", reply_markup=back_to_main_menu)

@dp.callback_query_handler(text="del_channel")
async def channel_list(call: types.CallbackQuery):
    royxat = db.select_channels()
    text = "🔰 Kanallar ro'yxati:\n\n"
    son = 0
    for o in royxat:
        son +=1
        text += f"{son}. {o[1]}\n💠 Username: {o[1]}\n\n"
    await call.message.edit_text(text=text)
    admins = db.select_all_channel()
    buttons = InlineKeyboardMarkup(row_width=2)
    for admin in admins:
        buttons.insert(InlineKeyboardButton(text=f"{admin[1]}", callback_data=f"delchanel:{admin[1]}"))

    buttons.add(InlineKeyboardButton(text="➕ Kanal qo'shish", callback_data="add_channel"))
    buttons.insert(InlineKeyboardButton(text="⬅️ Orqaga", callback_data="back_to_main_menu"))
    await call.message.edit_text(text=text, reply_markup=buttons)

@dp.callback_query_handler(text_contains="delchanel:", state="*")
async def del_admin_method(call: types.CallbackQuery):
    await call.answer(cache_time=1)
    data = call.data.rsplit(":")
    print(data[1])
    delete_orders = db.delete_channel(channel=data[1])
    await call.answer("🗑 Channel o'chirildi !",show_alert=True)
    await call.message.edit_text("✅ Kanal muvaffaqiyatli o'chirildi!", reply_markup=panel)
# MAJBURIY OBUNA SOZLASH UCHUN

# sovga
@dp.callback_query_handler(text="add_sovga")
async def add_sovga(call: types.CallbackQuery):
    await call.message.answer(
        text="Sov'ga uchun text kiriting"
    )
    await SuperAdminState.SUPER_ADMIN_UPDATE_SOVGA.set()

@dp.message_handler(state = SuperAdminState.SUPER_ADMIN_UPDATE_SOVGA, chat_id = ADMINS[0])
async def add_sovga(message: types.Message, state: FSMContext):
    db.add_sovga(
        text=message.text
    )
    await message.answer(
        text="Sog'a qo'shildi"
    )
    await state.finish()

@dp.callback_query_handler(text="update_sovga")
async def add_sovga(call: types.CallbackQuery):
    await call.message.answer(
        text="Sov'ga uchun text kiriting"
    )
    await SuperAdminState.SUPER_ADMIN_UPDATE_SOVGA1.set()

@dp.message_handler(state = SuperAdminState.SUPER_ADMIN_UPDATE_SOVGA1, chat_id = ADMINS[0])
async def add_sovga(message: types.Message, state: FSMContext):
    db.update_sovga(
        text=message.text,
        id=1
    )
    await message.answer(
        text="Sog'a qo'shildi"
    )
    await state.finish()
# sovga

# foydalanuvchini tekshirish
@dp.callback_query_handler(text = "ball", chat_id = ADMINS[0])
async def send_post_handler(call: types.CallbackQuery):
    await call.message.edit_text("<b>Foydalanuvchi id sni kiriting!?</b>")
    await Users.user.set()
    
@dp.message_handler(state = Users.user, chat_id = ADMINS[0])
async def send_post_message(message: types.Message, state: FSMContext):
    print(message.text)
    balans = db.select_user(message.text)
    for ball in balans:
        text = f"<b>Foydalnuvchi {ball[2]}\n</b>"
        text += f"<b>Foydalnuvchi id si <code>{ball[1]}</code></b>\n"
        text += f"<b>Foydalanuvhi balli {ball[4]} ball</b>"
        await message.answer(text)

    await state.finish()



# Bot staticticasni bilish uchun kommanda

@dp.callback_query_handler(text = "statistics", chat_id = ADMINS[0])
async def statictic(call: types.CallbackQuery):
    user = db.count_users()
    await call.answer(f"📊 Bazada:\n\n{user[0]} ta foydalanuvchi mavjud", show_alert=True)

# Bazani yuklab olish uchun kommanda

@dp.callback_query_handler(text = "download_base", chat_id = ADMINS[0])
async def send_db(call: types.CallbackQuery):
    file = types.InputFile(path_or_bytesio="data.db")
    await call.message.answer_document(document=file, caption="📁 Malumotlar bazasi. Botdagi hamma ma'lumotlar mana shu fayl ichida! ✅")

# Xabar yuborish

@dp.callback_query_handler(text = "send_post", chat_id = ADMINS[0])
async def send_post_handler(call: types.CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=send_post)

# Copy qlib xabar yuborish

@dp.callback_query_handler(text = "copy_post", chat_id = ADMINS[0])
async def copy_post_handler(call: types.CallbackQuery):
    await call.message.answer("Postingizni yuboring:")
    await call.message.delete()
    await UserCopyState.post.set()

@dp.message_handler(state = UserCopyState.post, content_types=types.ContentType.ANY, chat_id = ADMINS[0])
async def send_post_message(message: types.Message, state: FSMContext):
    users = db.select_all_users()
    try:
        send = 0
        cross = 0
        text = ""
        for user in users:
            try:
                await bot.copy_message(chat_id=user[1],
                                        from_chat_id=message.chat.id,
                                        message_id=message.message_id,
                                        caption=message.caption,
                                        reply_markup=message.reply_markup,
                                        parse_mode=types.ParseMode.MARKDOWN)
                send += 1
            except Exception as err:
                cross += 1
        user = await bot.get_me()
        text = f"\n✅ {send} ta foydalanuvchiga yuborildi.\n❌ {cross} ta foydalanuvchiga yuborilmadi!\n\n@{user.username}"
        deletaion = await message.answer(text=text)
        await state.finish()
        await sleep(20)
        await bot.delete_message(chat_id=message.from_user.id, message_id=deletaion.message_id)
    except Exception as err:
        await message.answer(f"Xatolik")

# Forward qilib xabar yuborish

@dp.callback_query_handler(text='forward_post', chat_id = ADMINS[0])
async def forwsff_handler(call: types.CallbackQuery):
    await call.message.answer("Postingizni yuboring:")
    await call.message.delete()
    await UserForwardState.post.set()

@dp.message_handler(state = UserForwardState.post, content_types=types.ContentType.ANY, chat_id = ADMINS[0])
async def send_post_message(message: types.Message, state: FSMContext):
    users = db.select_all_users()
    try:
        send = 0
        cross = 0
        text = ""
        for user in users:
            try:
                await bot.forward_message(chat_id=user[1],
                    from_chat_id=message.chat.id,
                    message_id=message.message_id)
                send += 1
            except Exception as err:
                cross += 1
        user = await bot.get_me()
        text = f"\n✅ {send} ta foydalanuvchiga yuborildi.\n❌ {cross} ta foydalanuvchiga yuborilmadi!\n\n@{user.username}"
        deletaion = await message.answer(text=text)
        await state.finish()
        await sleep(30)
        await bot.delete_message(chat_id=message.from_user.id, message_id=deletaion.message_id)
    except Exception as err:
        await message.answer(f"Xatolik")