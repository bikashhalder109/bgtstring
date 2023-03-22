from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""🥀 𝐇𝐞𝐲 {msg.from_user.mention},

▷ 𝐌𝐲 𝐍𝐚𝐦𝐞 𝐈𝐬 {me2},
▷ 𝐈'𝐦 𝐀 𝐒𝐭𝐫𝐢𝐧𝐠 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐢𝐧𝐠 𝐁𝐨𝐭 🥀
▷ 𝐈𝐟 𝐘𝐨𝐮 𝐓𝐫𝐮𝐬𝐭 𝐌𝐞 𝐓𝐡𝐞𝐧 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐞 𝐒𝐞𝐬𝐬𝐢𝐨𝐧
▷ 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐓𝐞𝐥𝐞𝐭𝐡𝐨𝐧 𝐎𝐫 𝐏𝐲𝐫𝐨𝐠𝐫𝐦 𝐁𝐨𝐭𝐡 

🥀 𝐂𝐫𝐞𝐚𝐭𝐨𝐫™ : [𝐁𝐢𝐤𝐚𝐬𝐡🇮🇳](https://t.me/BikashHalder) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="🥀 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐞 🥀", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("📱 𝐘𝐨𝐮𝐓𝐮𝐛𝐞 🥀", url="https://youtube.com/@bikashgadgetstech"),
                    InlineKeyboardButton("♛ 𝐂𝐫𝐞𝐚𝐭𝐨𝐫 ♛", url="https://t.me/BikashHalder")
                ],
                [
                   InlineKeyboardButton("☏ 𝐏𝐫𝐨𝐦𝐨𝐭𝐢𝐨𝐧 ♛", url="https://t.me/BgtPromote")
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
