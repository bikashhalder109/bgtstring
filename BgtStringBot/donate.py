import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("donate"))
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/942400d144776934cd402.jpg",
        caption=f"""**💥 ᴘʟᴇᴀsᴇ ᴅᴏɴᴀᴛᴇ ᴛᴏ ᴍʏ ᴏᴡɴᴇʀ ғᴏʀ ʜɪs ʜᴀʀᴅᴡᴏʀᴋ 🙂. ʏᴏᴜ ᴄᴀɴ ᴄᴏɴᴛᴀᴄᴛ ᴍʏ ᴏᴡɴᴇʀ 🌷 ᴏɴ ᴄʟɪᴄᴋɪɴɢ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ.🌷**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "♕︎ ᴏᴡɴᴇʀ ɪᴅ ♕︎", url=f"https://t.me/BikashHalder")
                ]
                
           ]
        ),
    )
    