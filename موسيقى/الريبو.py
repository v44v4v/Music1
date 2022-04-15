import os
import sys
from datetime import datetime
from time import time
from pyrogram import Client, filters
from pyrogram.types import Message
from config import HNDLR, SUDO_USERS
from MusicTelethon.helpers.decorators import authorized_users_only

START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (    ("Minggu", 60 * 60 * 24 * 7),    ("Hari", 60 * 60 * 24),    ("Jam", 60 * 60),    ("Menit", 60),    ("Detik", 1),)
async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else ""))
    return ", ".join(parts)


@Client.on_message(    filters.user(SUDO_USERS) & filters.command(["تحديث."], prefixes=f"{HNDLR}"))
@authorized_users_only

async def restart(client, m: Message):
    await m.delete()
    loli = await m.reply("1")
    await loli.edit("2")
    await loli.edit("3")
    await loli.edit("4")
    await loli.edit("5")
    await loli.edit("6")
    await loli.edit("7")
    await loli.edit("8")
    await loli.edit("9")
    await loli.edit("**✅ تم تحديث البوت بنجاح**")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()
@Client.on_message(filters.user(SUDO_USERS) & filters.command(["الاوامر"], prefixes=f"{HNDLR}"))
@authorized_users_only
async def help(client, m: Message):
    await m.delete()
    HELP = f"""
<b>👋 اهلا {m.from_user.mention}!

𝘰𝘳𝘥𝘦𝘳𝘴 𝘮𝘶𝘴𝘪𝘤 ꫀٍꪜَ᥆
——————×—————

⧉ | لتشغيل صوتية في المكالمة أرسل ⇦ [ `{HNDLR}ش  + اسم الاغنيه` ]
⧉ | لتشغيل فيديو في المكالمة  ⇦ [ `{HNDLR}فيد  + اسم الاغنية` ]
———————×———————

⧉ | لأيقاف الاغنية او الفيديو مؤقتآ  ⇦ [ `{HNDLR]ايق` ] 
⧉ | لأعاده تشغيل الاغنية ⇦  [ `{HNDLR}شش` ]
⧉ | لأيقاف الاغنية  ⇦ [ `{HNDLR}` ] 
———————×———————

⧉ | لتحميل صوتية أرسل ⇦ [ `{HNDLR}تح + اسم الاغنية او الرابط` ]
⧉ | لتحميل فيديو  ⇦  [ `{HNDLR}تح.فيد + اسم الاغنية او الرابط` ]
———————×———————

⧉ | لأعاده تشغيل التنصيب أرسل ⇦  [ `{HNDLR}تحديث` ]
———————×———————
🛠 """
    await m.reply(HELP)
@Client.on_message(filters.command(["الريبو"], prefixes=f"{HNDLR}"))
async def repo(client, m: Message):
    await m.delete()
    REPO = f"""
<b>👋  اهلا {m.from_user.mention}!
- للمطور : @QooQoQ
"""
    await m.reply(REPO, disable_web_page_preview=True)
