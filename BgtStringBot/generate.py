from pyrogram.types import Message
from telethon import TelegramClient
from pyrogram import Client, filters
from asyncio.exceptions import TimeoutError
from telethon.sessions import StringSession
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)
from telethon.errors import (
    ApiIdInvalidError,
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError
)

import config



ask_ques = "**▷ 𝐂𝐡𝐨𝐨𝐬𝐞 𝐓𝐡𝐞 𝐒𝐭𝐫𝐢𝐧𝐠 𝐖𝐡𝐢𝐜𝐡 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 ✔️ :**"
buttons_ques = [
    [
        InlineKeyboardButton("𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦", callback_data="pyrogram"),
        InlineKeyboardButton("𝐓𝐞𝐥𝐞𝐭𝐡𝐨𝐧", callback_data="telethon"),
    ],
    [
        InlineKeyboardButton("𝐏𝐲𝐫𝐨 𝐁𝐨𝐭", callback_data="pyrogram_bot"),
        InlineKeyboardButton("𝐓𝐞𝐥𝐞 𝐁𝐨𝐭", callback_data="telethon_bot"),
    ],
]

gen_button = [
    [
        InlineKeyboardButton(text="🥀 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐞 🥀", callback_data="generate")
    ]
]




@Client.on_message(filters.private & ~filters.forwarded & filters.command(["generate", "gen", "string", "bgt"]))
async def main(_, msg):
    await msg.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))


async def generate_session(bot: Client, msg: Message, telethon=False, is_bot: bool = False):
    if telethon:
        ty = "𝐓𝐞𝐥𝐞𝐭𝐡𝐨𝐧"
    else:
        ty = "𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦"
    if is_bot:
        ty += "𝐁𝐨𝐭"
    await msg.reply(f"◪ 𝐒𝐭𝐚𝐫𝐭 𝐭𝐨 **{ty}** 𝐒𝐭𝐫𝐢𝐧𝐠 ⏎...")
    user_id = msg.chat.id
    api_id_msg = await bot.ask(user_id, "𝐒𝐞𝐧𝐝 𝐘𝐨𝐮𝐫 𝐀𝐩𝐢 𝐈𝐝  \n\n𝐂𝐥𝐢𝐜𝐤 𝐨𝐧 /skip 𝐅𝐨𝐫 𝐮𝐬𝐢𝐧𝐠 𝐁𝐨𝐭 𝐀𝐩𝐢.", filters=filters.text)
    if await cancelled(api_id_msg):
        return
    if api_id_msg.text == "/skip":
        api_id = config.API_ID
        api_hash = config.API_HASH
    else:
        try:
            api_id = int(api_id_msg.text)
        except ValueError:
            await api_id_msg.reply("🥀 𝐍𝐨𝐭 𝐀 𝐕𝐚𝐥𝐢𝐝 **API_ID**.\n\n🥀 𝐏𝐥𝐞𝐚𝐬𝐞 𝐓𝐫𝐲 𝐀𝐠𝐚𝐢𝐧 𝐆𝐞𝐧𝐞𝐫𝐭𝐞 🌺", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
            return
        api_hash_msg = await bot.ask(user_id, "🥀 𝐍𝐨𝐰 𝐒𝐞𝐧𝐝 𝐘𝐨𝐮𝐫 **API_HASH** 🌺", filters=filters.text)
        if await cancelled(api_hash_msg):
            return
        api_hash = api_hash_msg.text
    if not is_bot:
        t = "🥀 𝐍𝐨𝐰 𝐒𝐞𝐧𝐝 𝐘𝐨𝐮𝐫 **PHONE_NUMBER** 𝐖𝐢𝐭𝐡 𝐂𝐨𝐮𝐧𝐭𝐫𝐲 𝐂𝐨𝐝𝐞 🥀\n𝐄𝐱𝐚𝐦𝐩𝐥𝐞 : `+918609472067`'"
    else:
        t = "🥀 𝐒𝐞𝐧𝐝 𝐘𝐨𝐮𝐫 **BOT_TOKEN**.\n𝐄𝐱𝐚𝐦𝐩𝐥𝐞 : `5072196965:bikashahlder`'"
    phone_number_msg = await bot.ask(user_id, t, filters=filters.text)
    if await cancelled(phone_number_msg):
        return
    phone_number = phone_number_msg.text
    if not is_bot:
        await msg.reply("🥀 𝐁𝐠𝐭 𝐒𝐭𝐫𝐢𝐧𝐠 𝐁𝐨𝐭 𝐓𝐫𝐲 𝐓𝐨 𝐒𝐞𝐧𝐝 𝐎𝐭𝐩 𝐚𝐭 𝐓𝐡𝐞 𝐆𝐢𝐯𝐞𝐧 𝐏𝐡𝐨𝐧𝐞 𝐍𝐮𝐦𝐛𝐞𝐫...")
    else:
        await msg.reply("🥀 𝐓𝐫𝐲𝐢𝐧𝐠 𝐓𝐨 𝐋𝐨𝐠𝐢𝐧 𝐯𝐢𝐚 𝐁𝐨𝐭 𝐓𝐨𝐤𝐞𝐧..")
    if telethon and is_bot:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif is_bot:
        client = Client(name="bot", api_id=api_id, api_hash=api_hash, bot_token=phone_number, in_memory=True)
    else:
        client = Client(name="user", api_id=api_id, api_hash=api_hash, in_memory=True)
    await client.connect()
    try:
        code = None
        if not is_bot:
            if telethon:
                code = await client.send_code_request(phone_number)
            else:
                code = await client.send_code(phone_number)
    except (ApiIdInvalid, ApiIdInvalidError):
        await msg.reply("🥀 𝐘𝐨𝐮𝐫 **ᴀᴩɪ_ɪᴅ** & **ᴀᴩɪ_ʜᴀsʜ** 𝐂𝐨𝐦𝐛𝐢𝐧𝐚𝐭𝐢𝐨𝐧 𝐃𝐨𝐞𝐬𝐧'𝐭 𝐌𝐚𝐭𝐜𝐡 🌺\n\n🥀 𝐓𝐫𝐲 𝐀𝐠𝐚𝐢𝐧 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐢𝐧𝐠 ✅.", reply_markup=InlineKeyboardMarkup(gen_button))
        return
    except (PhoneNumberInvalid, PhoneNumberInvalidError):
        await msg.reply("🥀 𝐓𝐡𝐞 **𝐏𝐡𝐨𝐧𝐞_𝐍𝐮𝐦𝐛𝐞𝐫** 𝐃𝐨𝐞𝐬𝐧'𝐭 𝐀𝐧𝐲 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐀𝐜𝐜𝐨𝐮𝐧𝐭 ❌\n\n🥀 𝐓𝐫𝐲 𝐀𝐠𝐚𝐢𝐧 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐞 𝐘𝐨𝐮𝐫 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 🌺.", reply_markup=InlineKeyboardMarkup(gen_button))
        return
    try:
        phone_code_msg = None
        if not is_bot:
            phone_code_msg = await bot.ask(user_id, "🥀 𝐏𝐥𝐞𝐚𝐬𝐞 𝐒𝐞𝐧𝐝 𝐓𝐡𝐞 **𝐎𝐓𝐏** 𝐓𝐡𝐚𝐭 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 𝐘𝐨𝐮𝐫 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 🌺\n🥀 𝐈𝐟 𝐎𝐓𝐏 𝐈𝐬 66678, **𝐎𝐓𝐏 𝐬𝐞𝐧𝐝 𝐀𝐬 𝐓𝐡𝐢𝐬 𝐅𝐨𝐫𝐦𝐚𝐭 ➽** `6 6 6 7 8`.", filters=filters.text, timeout=600)
            if await cancelled(phone_code_msg):
                return
    except TimeoutError:
        await msg.reply("🥀 𝐓𝐢𝐦𝐞 𝐋𝐢𝐦𝐢𝐭 𝐑𝐞𝐚𝐜𝐡𝐞𝐝 𝐎𝐟 5 𝐌𝐢𝐧𝐬 🌺\n\n🥀 𝐓𝐫𝐲 𝐀𝐠𝐚𝐢𝐧 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐢𝐧𝐠 𝐘𝐨𝐮𝐫 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 🌺", reply_markup=InlineKeyboardMarkup(gen_button))
        return
    if not is_bot:
        phone_code = phone_code_msg.text.replace(" ", "")
        try:
            if telethon:
                await client.sign_in(phone_number, phone_code, password=None)
            else:
                await client.sign_in(phone_number, code.phone_code_hash, phone_code)
        except (PhoneCodeInvalid, PhoneCodeInvalidError):
            await msg.reply("🥀 𝐓𝐡𝐞 𝐎𝐓𝐏 𝐘𝐨𝐮'𝐯𝐞 𝐒𝐞𝐧𝐝 𝐢𝐬 𝐖𝐫𝐨𝐧𝐠 ❌\n\n🥀 𝐓𝐫𝐲 𝐀𝐠𝐚𝐢𝐧 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐢𝐧𝐠 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 🌺.", reply_markup=InlineKeyboardMarkup(gen_button))
            return
        except (PhoneCodeExpired, PhoneCodeExpiredError):
            await msg.reply("🥀 𝐎𝐓𝐏 𝐈𝐬 **𝐄𝐱𝐩𝐢𝐫𝐞𝐝**\n\n🥀 𝐓𝐫𝐲 𝐀𝐠𝐚𝐢𝐧 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐢𝐧𝐠 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 🌺", reply_markup=InlineKeyboardMarkup(gen_button))
            return
        except (SessionPasswordNeeded, SessionPasswordNeededError):
            try:
                two_step_msg = await bot.ask(user_id, "🥀 𝐏𝐥𝐞𝐚𝐬𝐞 𝐄𝐧𝐭𝐞𝐫 𝐘𝐨𝐮𝐫 𝐓𝐰𝐨 𝐒𝐭𝐞𝐩 𝐕𝐞𝐫𝐢𝐟𝐢𝐜𝐚𝐭𝐢𝐨𝐧 𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝 𝐓𝐨 𝐂𝐨𝐧𝐭𝐢𝐧𝐮𝐞 🥀.", filters=filters.text, timeout=300)
            except TimeoutError:
                await msg.reply("🥀 𝐓𝐢𝐦𝐞 𝐋𝐢𝐦𝐢𝐭 𝐑𝐞𝐚𝐜𝐡𝐞𝐝 𝐎𝐟 5 𝐌𝐢𝐧𝐬 🌺\n\n🥀 𝐓𝐫𝐲 𝐀𝐠𝐚𝐢𝐧 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐢𝐧𝐠 𝐘𝐨𝐮𝐫 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 🌺.", reply_markup=InlineKeyboardMarkup(gen_button))
                return
            try:
                password = two_step_msg.text
                if telethon:
                    await client.sign_in(password=password)
                else:
                    await client.check_password(password=password)
                if await cancelled(api_id_msg):
                    return
            except (PasswordHashInvalid, PasswordHashInvalidError):
                await two_step_msg.reply("🥀 𝐘𝐨𝐮𝐫 𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝 𝐈𝐬 𝐖𝐫𝐨𝐧𝐠 ❌.\n\n🙂 𝐓𝐫𝐲 𝐀𝐠𝐚𝐢𝐧 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐞 𝐒𝐭𝐫𝐢𝐧𝐠 🌺.", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
                return
    else:
        if telethon:
            await client.start(bot_token=phone_number)
        else:
            await client.sign_in_bot(phone_number)
    if telethon:
        string_session = client.session.save()
    else:
        string_session = await client.export_session_string()
    text = f"**🥀 𝐇𝐞𝐲 𝐓𝐡𝐢𝐬 𝐈𝐬 𝐘𝐨𝐮𝐫 {ty} 𝐒𝐭𝐫𝐢𝐧𝐠 🌺** \n\n`{string_session}` \n\n**🥀 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐞𝐝 𝐁𝐲 :** @BgtStringBot\n✎ **𝐍𝐨𝐭𝐞 :** 𝐃𝐨𝐧'𝐭 𝐒𝐡𝐚𝐫𝐞 𝐘𝐨𝐮𝐫 𝐒𝐭𝐫𝐢𝐧𝐠 𝐀𝐧𝐲𝐨𝐧𝐞 || 𝐉𝐨𝐢𝐧 @Bgt_Chat 🌺"
    try:
        if not is_bot:
            await client.send_message("me", text)
        else:
            await bot.send_message(msg.chat.id, text)
    except KeyError:
        pass
    await client.disconnect()
    await bot.send_message(msg.chat.id, "🥀 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲  𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐞 𝐘𝐨𝐮𝐫 {} 𝐒𝐭𝐫𝐢𝐧𝐠 🌺.\n\n𝐂𝐡𝐞𝐜𝐤 𝐘𝐨𝐮𝐫 𝐒𝐚𝐯𝐞𝐝 𝐌𝐞𝐬𝐬𝐚𝐠𝐞𝐬 🥀\n\n**🥀 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲** @BikashGadgetsTech 🥀".format("𝐓𝐞𝐥𝐞𝐭𝐡𝐨𝐧" if telethon else "𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦"))


async def cancelled(msg):
    if "/cancel" in msg.text:
        await msg.reply("**▷ 𝐂𝐚𝐧𝐜𝐞𝐥 𝐓𝐡𝐞 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐢𝐧𝐠 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 ❌**", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
        return True
    elif "/restart" in msg.text:
        await msg.reply("**▷ 𝐁𝐠𝐭 𝐒𝐭𝐫𝐢𝐧𝐠 𝐁𝐨𝐭 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐑𝐞𝐬𝐭𝐚𝐫𝐭𝐞𝐝 ✅**", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
        return True
    elif "/skip" in msg.text:
        return False
    elif msg.text.startswith("/"):  # Bot Commands
        await msg.reply("**▷ 𝐂𝐚𝐧𝐜𝐞𝐥 𝐓𝐡𝐞 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐢𝐧𝐠 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 ❌**", quote=True)
        return True
    else:
        return False
