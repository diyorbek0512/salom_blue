import uuid
from asyncio import sleep
from aiogram import types

from data.config import video_kanal, ADMINS
from random import choice
from filters.kanal import Kanal
from loader import dp,db,bot
from string import digits


def rand():
    result_str = ''.join(choice(digits) for i in range(4))
    return result_str


@dp.channel_post_handler(Kanal(),content_types=types.ContentTypes.VIDEO,chat_id="-1002014873201")
async def post_in_channel(message: types.Message):
    user_bot =await bot.get_me()
    channel = message.chat.username
    file_id = f"https://t.me/{channel}/{message.message_id}"
    caption = message.caption
    ids = rand()
    db.add_file(
        file_id,
        caption=caption,
        ids=ids
    )
    # await bot.send_message(chat_id=video_kanal[0],
    #                        )
    await bot.send_message(ADMINS[0],text=f"<b>Video kodi:</b> <code>{ids}</code>\n\n{caption}\n\n❗<b>Diqqat videoni bot orqali topishingiz mumkin!</b>",
                           reply_markup=types.InlineKeyboardMarkup(inline_keyboard=[[types.InlineKeyboardButton(text=f"Yuklab olish 📥",url=f"https://t.me/{user_bot.username}?start={ids}")]]))


@dp.message_handler()
async def video(m: types.Message):
    ids = m.text
    link = db.select_video(ids)
    for i in link:
        video = i[1]
        caption = i[2]
        await m.reply_video(video=video,
                            caption=caption,
                            reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Do'stlarga yuborish  📲", switch_inline_query=f"{i[3]}")),disable_notification=True)


@dp.inline_handler()
async def referals(inline_query: types.InlineQuery):
    ids = inline_query.query
    link = db.select_video(ids)
    for i in link:
        video_url=i[1]
        caption=i[2]
        articles = [
            types.InlineQueryResultVideo(
                id=str(uuid.uuid4()),
                title="Obuna Bo'ling",
                video_url=video_url,
                caption=caption,
                description=caption,
                thumb_url="https://example.com/video_thumbnail.jpg",
                mime_type="video/mp4",
                input_message_content=types.InputMediaVideo(media=video_url,caption=caption),
                reply_markup=types.InlineKeyboardMarkup(inline_keyboard=[[types.InlineKeyboardButton("Kino kodlar", url=f"https://t.me/l1movie_uz")]])
            )
        ]
        await inline_query.answer(results=articles, cache_time=60, is_personal=True)



