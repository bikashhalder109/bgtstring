from config import MUST_JOIN

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@Client.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not MUST_JOIN:
        return
    try:
        try:
            await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(
                    photo="https://te.legra.ph/file/3d071cafe30c95f5dad3a.jpg", caption=f"🥀 𝐈𝐟 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 𝐔𝐬𝐞 𝐌𝐞 𝐓𝐡𝐞𝐍 𝐉𝐨𝐢𝐧 𝐎𝐮𝐫 [𝐂𝐡𝐚𝐧𝐧𝐞𝐥™](https://t.me/BikashGadgetsTech) 𝐎𝐫 [𝐂𝐡𝐚𝐭©](https://t.me/Bgt_Chat) 🅱️",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("</>Bikash Gadgets Tech", url=link),
                            ]
                        ]
                    )
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"Promote me as an admin in the MUST_JOIN chat : {MUST_JOIN} !")
