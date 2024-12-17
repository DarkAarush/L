from pyrogram.enums import ParseMode

from AviaxMusic import app
from AviaxMusic.utils.database import is_on_off
from config import LOG_GROUP_ID


async def play_logs(message, streamtype):
    if await is_on_off(2):
        logger_text = f"""
<blockquote><b>{app.mention} ᴘʟᴀʏ ʟᴏɢ</b>

<b>𝗖𝗵𝗮𝘁 𝗶𝗱 :</b> <code>{message.chat.id}</code>
<b>𝗖𝗵𝗮𝘁 𝗡𝗮𝗺𝗲 :</b> {message.chat.title}
<b>𝗖𝗵𝗮𝘁 𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲 :</b> @{message.chat.username}

<b>𝗨𝘀𝗲𝗿 𝗜𝗱 :</b> <code>{message.from_user.id}</code>
<b>𝗣𝗿𝗼𝗳𝗶𝗹𝗲 𝗡𝗮𝗺𝗲:</b> {message.from_user.mention}
<b>𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲 :</b> @{message.from_user.username}

<b>𝗦𝗼𝗻𝗴 :</b> {message.text.split(None, 1)[1]}
<b>𝗥𝗲𝗾𝘂𝗲𝘀𝘁 𝗣𝗹𝗮𝘁𝗳𝗼𝗿𝗺:</b> {streamtype}</blockquote>"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    chat_id=LOG_GROUP_ID,
                    text=logger_text,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
