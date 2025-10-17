from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

panel = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🗄 Bazani yuklash",
                callback_data="download_base"
            ),
            InlineKeyboardButton(
                text = "📤 Xabar yuborish",
                callback_data="send_post"
            )
        ],
        [
            InlineKeyboardButton(
                text="➕ Kanal qo'shish",
                callback_data="add_channel"
            ),
            InlineKeyboardButton(
                text="➖ Kanal o'chirish",
                callback_data="del_channel"),
        ],
        [
            InlineKeyboardButton(
                                        text="🎁 Sovg'a Yangilash",
                                        callback_data="update_sovga"
                                    ),
            InlineKeyboardButton(
                                        text="Balni 0 qilish",
                                        callback_data="update_ball"
                                    )
                    ],
        [
            InlineKeyboardButton(
                text = "📊 Bot statistikasi",
                callback_data="statistics"
            ),
            InlineKeyboardButton(
                text = "♻️ Ballni Ko'rish",
                callback_data="ball"
            ),
            InlineKeyboardButton(
                text = "❌ Panelni yopish",
                callback_data="close_panel"
            )
        ]
    ]
)


send_post = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text = "📤 Forward yuborish",
                callback_data="forward_post"
            ),
            InlineKeyboardButton(
                text = "📤 Copy qilib yuborish",
                callback_data="copy_post"
            )
        ],
        [
            InlineKeyboardButton(
                text = "🔙 Orqaga",
                callback_data="back"
            ),
            InlineKeyboardButton(
                text = "❌ Panelni yopish",
                callback_data="close_panel"
            )
        ]
    ]
)

back_to_main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️ Orqaga", callback_data="back")
        ]
    ]
)

# user_group = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(
#                 text="Userga yuborish forward",
#                 callback_data='forward_user'
#             ),
#             InlineKeyboardButton(
#                 text="Guruh yuborish forward",
#                 callback_data='forward_group'
#             )
#         ],
#     ]
# )
