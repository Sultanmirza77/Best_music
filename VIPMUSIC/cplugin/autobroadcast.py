import asyncio
import datetime
from pyrogram import Client
from config import START_IMG_URL, AUTO_GCAST_MSG, AUTO_GCAST, LOGGER_ID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
from typing import Dict, List, Union
from VIPMUSIC.utils.database import get_served_chats_clone
from VIPMUSIC import userbot
from VIPMUSIC.core.mongo import mongodb, pymongodb

AUTO_GCAST = True

START_IMG_URLS = "https://telegra.ph/file/e309e8569e62a971b949e.jpg"

MESSAGES = f"""**ㅤㅤㅤ⚠️⚠️⚠️⚠️⚠️📡
💗 दुश्मन ही क्या जिसमें जलन न हो और वो इश्क़ ही क्या जिसमें टशन न हो 💗
फ्री ऑडिओ  नोट्स के लिए जोइन करे यहा सभी प्रकार के ऑडियो नोट्स मिलता है


🫂Link:-https://t.me/gkaudionotes01  ✅

**"""


BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "๏ Click FREE AUDIO NOTES  ๏",
                url=f"https://t.me/gkaudionotes01",
            )
        ]
    ]
)

MESSAGE = f"""**๏ ᴛʜɪs ɪs ᴀᴅᴠᴀɴᴄᴇᴅ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs + ᴄʜᴀɴɴᴇʟs ᴠᴄ. 💌

🎧 ᴘʟᴀʏ + ᴠᴘʟᴀʏ + ᴄᴘʟᴀʏ 🎧

➥ sᴜᴘᴘᴏʀᴛᴇᴅ ᴡᴇʟᴄᴏᴍᴇ - ʟᴇғᴛ ɴᴏᴛɪᴄᴇ, ᴛᴀɢᴀʟʟ, ᴠᴄᴛᴀɢ, ʙᴀɴ - ᴍᴜᴛᴇ, sʜᴀʏʀɪ, ʟᴜʀɪᴄs, sᴏɴɢ - ᴠɪᴅᴇᴏ ᴅᴏᴡɴʟᴏᴀᴅ, ᴇᴛᴄ... ❤️

🔐ᴜꜱᴇ » [/start](https://t.me/bestmunsicbot?start=help) ᴛᴏ ᴄʜᴇᴄᴋ ʙᴏᴛ

➲ ʙᴏᴛ :** @bestmunsicbot"""

BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "๏ ᴋɪᴅɴᴀᴘ ᴍᴇ ๏",
                url=f"https://t.me/bestmunsicbot?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users",
            )
        ]
    ]
)

caption = MESSAGES

TEXT = """**ᴀᴜᴛᴏ ɢᴄᴀsᴛ ɪs ᴇɴᴀʙʟᴇᴅ sᴏ ᴀᴜᴛᴏ ɢᴄᴀsᴛ/ʙʀᴏᴀᴅᴄᴀsᴛ ɪs ᴅᴏɪɴ ɪɴ ᴀʟʟ ᴄʜᴀᴛs ᴄᴏɴᴛɪɴᴜᴏᴜsʟʏ. **\n**ɪᴛ ᴄᴀɴ ʙᴇ sᴛᴏᴘᴘᴇᴅ ʙʏ ᴘᴜᴛ ᴠᴀʀɪᴀʙʟᴇ [ᴀᴜᴛᴏ_ɢᴄᴀsᴛ = (ᴋᴇᴇᴘ ʙʟᴀɴᴋ & ᴅᴏɴᴛ ᴡʀɪᴛᴇ ᴀɴʏᴛʜɪɴɢ)]**"""


async def send_message_to_chats(client: Client):
    try:
        chats = await get_served_chats_clone()

        for chat_info in chats:
            chat_id = chat_info.get("chat_id")
            if isinstance(chat_id, int):  # Check if chat_id is an integer
                try:
                    await client.send_photo(
                        chat_id,
                        photo=START_IMG_URLS,
                        caption=caption,
                        reply_markup=BUTTONS,
                    )
                    await asyncio.sleep(
                        1
                    )  # Sleep for 100 second between sending messages
                except Exception as e:
                    pass  # Do nothing if an error occurs while sending message
    except Exception as e:
        pass  # Do nothing if an error occurs while fetching served chats


async def continuous_cbroadcast():
    # Send TEXT once when bot starts

    while True:
        if AUTO_GCAST:
            try:
                await send_message_to_chats(client)
            except Exception as e:
                pass

        # Wait for 10000000000000000000 seconds before next broadcast
        await asyncio.sleep(5)


# Start the continuous broadcast loop if AUTO_GCAST is True
if AUTO_GCAST:
    asyncio.create_task(continuous_cbroadcast())
