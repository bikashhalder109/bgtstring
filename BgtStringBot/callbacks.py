import traceback

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup

from BgtStringBot.generate import generate_session, ask_ques, buttons_ques


@Client.on_callback_query(filters.regex(pattern=r"^(generate|pyrogram|pyrogram_bot|telethon_bot|telethon)$"))
async def _callbacks(bot: Client, callback_query: CallbackQuery):
    query = callback_query.matches[0].group(1)
    if query == "generate":
        await callback_query.answer()
        await callback_query.message.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))
    elif query.startswith("pyrogram") or query.startswith("telethon"):
        try:
            if query == "pyrogram":
                await callback_query.answer()
                await generate_session(bot, callback_query.message)
            elif query == "pyrogram_bot":
                await callback_query.answer("⇨ 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐞 𝐓𝐨 𝐁𝐞 𝐏𝐲𝐫𝐨 𝐕2 ✔️", show_alert=True)
                await generate_session(bot, callback_query.message, is_bot=True)
            elif query == "telethon_bot":
                await callback_query.answer()
                await generate_session(bot, callback_query.message, telethon=True, is_bot=True)
            elif query == "telethon":
                await callback_query.answer()
                await generate_session(bot, callback_query.message, telethon=True)
        except Exception as e:
            print(traceback.format_exc())
            print(e)
            await callback_query.message.reply(ERROR_MESSAGE.format(str(e)))


ERROR_MESSAGE = "🥀 𝐒𝐨𝐦𝐞𝐭𝐡𝐢𝐧𝐠 𝐖𝐞𝐧𝐭 𝐖𝐫𝐨𝐧𝐠 ❗\n\n**𝐄𝐫𝐫𝐨𝐫** ➰ : {} " \
            "\n\n**🥀 𝐅𝐨𝐫𝐰𝐚𝐫𝐝 𝐓𝐡𝐢𝐬 𝐄𝐫𝐫𝐨𝐫 𝐓𝐨 @Bgt_Chat**, 𝐎𝐫 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 [𝐎𝐰𝐧𝐞𝐫♕](http://t.me/BikashHalder) ™️"