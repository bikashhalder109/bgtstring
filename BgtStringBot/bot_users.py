from pyrogram.types import Message
from pyrogram import Client, filters

from config import OWNER_ID
from BgtStringBot.db.users import add_served_user, get_served_users


@Client.on_message(filters.private & ~filters.service, group=1)
async def users_sql(_, msg: Message):
    await add_served_user(msg.from_user.id)


@Client.on_message(filters.user(OWNER_ID) & filters.command("stats"))
async def _stats(_, msg: Message):
    users = len(await get_served_users())
    await msg.reply_text(f"⎚ 𝐂𝐮𝐫𝐫𝐞𝐧𝐭 𝐔𝐬𝐞𝐫'𝐬 𝐎𝐟 𝐁𝐠𝐭 𝐒𝐭𝐫𝐢𝐧𝐠 𝐁𝐨𝐭 🥀 :\n\n🥀 𝐔𝐬𝐞𝐫'𝐬 : {users} ", quote=True)
