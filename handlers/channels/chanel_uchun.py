from aiogram import types
from filters.kanal import Kanal
from loader import dp, bot

@dp.channel_post_handler(Kanal(),content_types=['document'])
async def post_in_channel(post: types.Message):
    chanel_caption = post.caption
    if chanel_caption == None: chanel_caption = ''
    await post.edit_caption(caption=f"{chanel_caption}",reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Ulashish ♻️", url=f"https://t.me/share/url?url=https://t.me/{post.chat.username}/{post.message_id}")))

@dp.channel_post_handler(Kanal(),content_types=['video'])
async def post_in_channel(post: types.Message):
    chanel_caption = post.caption
    if chanel_caption == None: chanel_caption = ''
    await post.edit_caption(caption=f"{chanel_caption}",reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Ulashish ♻️", url=f"https://t.me/share/url?url=https://t.me/{post.chat.username}/{post.message_id}")))

@dp.channel_post_handler(Kanal(),content_types=['photo'])
async def post_in_channel(post: types.Message):
    chanel_caption = post.caption
    if chanel_caption == None: chanel_caption = ''
    await post.edit_caption(caption=f"{chanel_caption}",reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Ulashish ♻️", url=f"https://t.me/share/url?url=https://t.me/{post.chat.username}/{post.message_id}")))

@dp.channel_post_handler(Kanal(),content_types=['audio'])
async def post_in_channel(post: types.Message):
    chanel_caption = post.caption
    if chanel_caption == None: chanel_caption = ''
    await post.edit_caption(caption=f"{chanel_caption}",reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Ulashish ♻️", url=f"https://t.me/share/url?url=https://t.me/{post.chat.username}/{post.message_id}")))

@dp.channel_post_handler(Kanal(),content_types=['voice'])
async def post_in_channel(post: types.Message):
    chanel_caption = post.caption
    if chanel_caption == None: chanel_caption = ''
    await post.edit_caption(caption=f"{chanel_caption}",reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Ulashish ♻️", url=f"https://t.me/share/url?url=https://t.me/{post.chat.username}/{post.message_id}")))

@dp.channel_post_handler(Kanal())
async def post_in_channel(post: types.Message):
    chanel_text = post.text
    if chanel_text == None: chanel_text = ''
    await post.edit_text(f"{chanel_text}",reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Ulashish ♻️", url=f"https://t.me/share/url?url=https://t.me/{post.chat.username}/{post.message_id}")))

