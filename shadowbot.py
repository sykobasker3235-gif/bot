# SHADOW.py  [MERGED ULTIMATE + BIG NC RAILS]
# tokens: shadow | nc: paglu2+shadow BIGGEST | name: SHADOW everywhere
import asyncio, json, os, random, time, logging, sys, io, getpass
from typing import Dict, List
from datetime import datetime, timezone, timedelta
from telegram import Update
from telegram.ext import Application, PrefixHandler, ContextTypes
from telegram import error as telegram_error

if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

TOKENS = [
    "8502418525:AAFnWuVlaQmy4W7MJmo1OEI0yO_La3TJG5E",
    "8854742568:AAEke6wl2nyerCCXYbi1zk-RiwSDtV2UkAc",
    "8556053647:AAHOfcf19tLmop5HM3M6x4BkxuNAUS0IOg4",
    "8948609410:AAHqbVcI6UrED4yucnxy0SVW92FzRMa_D_8",
    "8957239850:AAE7OXVpABHvsXEagC9_pl6Cf5C-pXQAnmE",
    "8820416521:AAH1T3f04qPX526_CS-o7cuh-DyMXIrVVow",
    "8837388559:AAFJxt0x10buFZ0Im1MbiRCl_C7MhRuxW3E",
    "8951225648:AAHz0xugz84SuE615s01OIotzvJ0yWRTjfU",
    "8861458784:AAHRhAoKrW94ynUvYJbONjY2GJFNKyGK3Lw",
    "8515028748:AAF-sTBOukid5kcBoNSxuZ6KPqD-7QUIGtE",
]
OWNER_ID = 7263812907
SUDO_FILE = "sudo_shadow.json"
start_time = time.time()
GLOBAL_DELAY = 0.01
shutdown_event = asyncio.Event()

HELP_VIDEO_URL = "https://files.catbox.moe/fhd4ft.mp4"
HELP_IMAGE_URL = "https://d.uguu.se/kEbaOVGQ.jpg"
STATUS_IMAGE_URL = "https://files.catbox.moe/bh902c.jpg"
OVER_IMAGE_URL = "https://files.catbox.moe/ck86h6.jpg"

apps = []
bots = []

nc1_tasks: Dict[int, List[asyncio.Task]] = {}
nc2_tasks: Dict[int, List[asyncio.Task]] = {}
nc3_tasks: Dict[int, List[asyncio.Task]] = {}
nc4_tasks: Dict[int, List[asyncio.Task]] = {}
sf_nc_tasks: Dict[int, List[asyncio.Task]] = {}
lovenc_tasks: Dict[int, List[asyncio.Task]] = {}
mutthinc_tasks: Dict[int, List[asyncio.Task]] = {}
bloodnc_tasks: Dict[int, List[asyncio.Task]] = {}
mega_nc_tasks: Dict[int, List[asyncio.Task]] = {}
ncknot_tasks: Dict[int, List[asyncio.Task]] = {}
ncheavy_tasks: Dict[int, List[asyncio.Task]] = {}
ncheart_tasks: Dict[int, List[asyncio.Task]] = {}
spam1_tasks: Dict[int, List[asyncio.Task]] = {}
spam2_tasks: Dict[int, List[asyncio.Task]] = {}
spam3_tasks: Dict[int, List[asyncio.Task]] = {}
spam4_tasks: Dict[int, List[asyncio.Task]] = {}
spam5_tasks: Dict[int, List[asyncio.Task]] = {}
slide1_tasks: Dict[int, List[asyncio.Task]] = {}
slide2_tasks: Dict[int, List[asyncio.Task]] = {}
slide3_tasks: Dict[int, List[asyncio.Task]] = {}
slide4_tasks: Dict[int, List[asyncio.Task]] = {}
photo_tasks: Dict[int, List[asyncio.Task]] = {}
chat_photos: Dict[int, List[str]] = {}
nc_tasks: Dict[int, List[asyncio.Task]] = {}
nc_counters: Dict[int, int] = {}
nc_modes: Dict[int, str] = {}
group_tasks: Dict[int, Dict] = {}

HEART_EMOJIS = ["❤️","🧡","💛","💚","🩵","💙","💜","🤎","🖤","🩶","🤍","🩷","💘","💝","💖","💗","💓","💞","💕","💌","💟","♥️","❣️","❤️‍🩹","💔","❤️‍🔥"]
WEATHER_SPACE_EMOJIS = ["💠","🌊","🌬️","❄️","🌀","🌪️","⚡","☔","🌈","🌑","🌒","🌓","🌔","🌕","🌖","🌗","🌘","✨","🌞","🌝","🌚","🌜","🌛","🌙","⭐","🌟","✨","🪐"]
NATURE_FLAGS_EMOJIS = ["🌿","🌱","🍃","☘️","🌹","🥀","🌺","🌷","🪷","🌸","💮","🏵️","🪻","🌻","🌼","🍂","🍁","🫧","🪼","🕸️","🪽","🎏","🎐","🏁","🚩","🎌","🏴","🏳️","🏳️‍🌈","🏳️‍⚧️","🏴‍☠️","🇦🇨","🇦🇩","🇦🇪","🇦🇫","🇦🇬","🇦🇮","🇦🇱","🇦🇲","🇦🇴","🇦🇶","🇦🇷","🇦🇸","🇦🇹","🇦🇺","🇦🇼","🇦🇽","🇦🇿","🇧🇦","🇧🇧","🇧🇩","🇧🇪","🇧🇫","🇧🇬","🇧🇭","🇧🇮","🇧🇯","🇧🇱","🇧🇲","🇧🇳","🇧🇴","🇧🇶","🇧🇷","🇧🇸","🇧🇹","🇧🇻","🇧🇼","🇧🇾","🇧🇿","🇨🇦","🇨🇨","🇨🇩","🇨🇫","🇨🇬","🇨🇭","🇨🇮","🇨🇰","🇨🇱","🇨🇲","🇨🇳","🇨🇴","🇨🇵","🇨🇶","🇨🇷","🇨🇺","🇨🇻","🇨🇼","🇩🇰","🇨🇽","🇨🇾","🇨🇿","🇩🇬","🇩🇲","🇬🇧","🇬🇩","🇬🇫","🇬🇬","🇬🇭","🇭🇲","🇬🇺","🇮🇨","🇮🇲","🇮🇪","🇰🇪","🇰🇲","🇱🇧","🇰🇿","🇰🇬","🇰🇾","🇱🇷","🇲🇩","🇲🇶","🇱🇾","🇱🇰","🇰🇷","🇯🇵","🇿🇲","🇻🇮","🇺🇸","🇹🇻","🇹🇲","🇺🇲","🇻🇪"]
FLOWER_EMOJIS = ["💐","🌹","🥀","🌺","🌷","🪷","🌸","💮","🏵️","🪻","🌻","🌼","🍂","🍁","🌿","🌱","🍃","☘️","🍀"]
BLOOD_EMOJIS = ["🩸"]
MUTTHI_EMOJIS = ["💦","💨","💧","🌊"]

NC1_WORDS = [
    "𝐒ʜᴀᴅᴏᴡ 𝐓ᴇʀɪ ᴍᴀᴀ ᴄʜᴏᴅ ᴋʀ 𝐍ᴀᴀʟɪ ᴍɪᴇ ꜰᴇᴋ 𝐃ᴜɢᴀ",
    "𝐓ᴇʀɪ 𝐌ᴀᴀ ᴋᴇ 𝐅ᴀᴛᴇ 𝐁ʜᴏꜱᴅᴇ ᴍɪᴇ 𝐒ʜᴀᴅᴏᴡ 𝐂ʜᴏᴡᴍɪɴ ʙɴᴀᴜɢᴀ",
    "𝐂ʜʟ ᴜᴛʜ ɢᴜʟᴀᴍ ɢᴜʟᴀᴍɪ ᴋʀ 𝐑𝐑 ɴᴀɪ",
    "𝐓ᴜ ᴀᴜʀ 𝐓ᴇʀɪ 𝐌ᴀᴀ + 𝐓ᴇʀᴀ 𝐁ᴀᴀᴘ ꜱʙ 𝐒ʜᴀᴅᴏᴡ ᴋᴇ ɢᴜʟᴀᴍ ᴀᴀᴊ ꜱᴇ !!",
    "𝐌ᴇɴᴇ ꜱᴜɴᴀ ᴛᴇʀɪ 𝐁ʜᴇɴ ʀɴᴅʏ ᴇʏ !!",
    "𝐒ʜᴀᴅᴏᴡ ᴋᴇ ʟᴀᴅᴋᴇ 𝐓ᴍᴋᴄ ..!!",
    "𝐒ʜᴀᴅᴏᴡ ᴋᴇ ʟᴀᴅᴋᴇ 𝐓ᴍᴋʙ...!!",
    "𝐒ʜᴀᴅᴏᴡ ᴋᴇ ʟᴀᴅᴋᴇ 𝐓ʙᴋᴄ...!!",
    "𝐒ʜᴀᴅᴏᴡ ᴋᴇ ʟᴀᴅᴋᴇ 𝐓ʙᴋʙ...!!",
    "𝐂ʜʟ ꜱɪᴅᴇ ʜᴀᴛ 𝐆ᴜʟᴀᴍ ᴡʀɴᴀ ᴛᴇʀɪ 𝐌ᴀᴀ ɴᴀɴɢɪ ᴋʀ ᴅᴜɢᴀ !!",
    "𝐂ʜᴜᴘ 𝐌ᴀᴅᴀʀᴄʜᴏᴅ","𝐂ʜᴜᴘ ᴋᴜᴛɪʏᴀ","𝐂ʜᴜᴘ 𝐑ɴᴅʏᴘᴜᴛʀᴀ",
    "𝐂ʜᴜᴘ 𝐁ʜᴇɴᴄʜᴏᴅᴅ","𝐂ʜᴜᴘ 𝐆ᴜʟᴀᴍ","𝐂ʜᴜᴘ 𝐌ᴀᴊᴅᴜʀ ᴋᴇ 𝐋ᴀᴅᴋᴇ",
    "𝐂ʜᴜᴘ 𝐁ʜᴏꜱᴅɪᴋᴇ","𝐓ᴇʀɪ ᴍᴀᴀ ᴋᴏ 𝐔ɴɪᴠᴇʀꜱᴇ ᴍɪᴇ 𝐂ʜᴏᴅᴜɢᴀ",
    "𝐓ᴇʀɪ 𝐁ʜᴇɴ ᴋᴏ 𝐍ᴀꜱᴀ ᴍɪᴇ 𝐂ʜᴏᴅᴜɢᴀ",
    "𝐓ᴇʀɪ ᴍᴀᴜꜱɪ ᴋᴏ 𝐔ꜱᴀ ᴍɪᴇ 𝐂ʜᴏᴅᴜɢᴀ",
    "𝐓ᴇʀɪ ʙᴜᴀᴀ ᴋᴏ 𝐁ᴇᴇᴄʜ ʙᴀᴢᴀʀ ᴍɪᴇ ᴄʜᴏᴅᴜɢᴀ",
    "𝐔ᴛʜ ʀɴᴅʏ ᴋᴇ ᴋᴇᴇᴅᴇ ᴀᴜᴋᴀᴛ ʙɴᴀ",
    "𝐓ᴍᴋʙ 𝐑ɴᴅʏ ᴋᴇ 𝐋ᴀᴅᴋᴇ 😈🖕🏻😈🖕🏻😈",
    "𝐓ᴇʀɪ ᴍᴀᴀ ᴍᴀʀ ɢʏɪ ¿😆😆😆",
    "𝐀ᴀʀ ꜱᴀᴍᴀɴᴅᴀʀ ᴘᴀᴀʀ ꜱᴀᴍᴀɴᴅᴀʀ ʙᴇᴇᴄʜ ᴍɪᴇ ʜᴀɪ 𝐒ʜᴀᴅᴏᴡ 🥰🖕🏻🥰",
    "𝐓ᴇʀɪ 𝐌ᴀᴀ ʜᴜᴍᴇꜱʜᴀ ᴍᴜᴊʜꜱᴇ ʜɪ ᴋʏᴜ चुडती है ¡! 😡🤬😡🤬😡",
    "𝐃ᴇᴋʜ ᴀᴀᴊ ᴛᴇʀɪ 𝐌ᴀᴀ ᴋᴀ ɴᴀɴɢᴀ ᴅᴀɴᴄᴇ ᴅɪᴋʜᴀᴜ ! 🩰🧑🏻‍🩰",
    "𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐊ɪ 𝐆ᴜʟᴀʙɪ 𝐂ʜᴜᴛ ᴍɪᴇ 𝐌ᴜᴛ ᴋʀ ʙʜᴀɢ ᴊᴀᴜɢᴀ 𝐁ꜱᴅᴋ ! 😆",
    "𝐓ᴇʀɪ 𝐌ᴀᴀ ᴄʜᴏᴅɴᴇ ᴀʀʜᴀ ʜᴜ ʀᴜᴋ ᴡʜɪ ɢᴜʟᴀᴍ ! 😾",
    "𝐓ᴇʀɪ ʙʜᴇɴ ᴋᴇ ʙᴏᴏʙɪᴇꜱ ᴋᴇ ʙᴇᴇᴄʜ ᴍɪᴇ ʟɴᴅ ꜰᴀꜱᴀ ᴋʀ ᴍᴜᴛʜ ᴍᴀᴀʀ ᴅᴜɢᴀ ʙꜱᴅᴋ 😆",
    "𝐓ᴇʀɪ ᴍᴀᴀ ᴋɪ ᴄʜᴜᴛ ᴍɪᴇ ᴍᴀɢɢɪᴇ ʙɴᴀ ᴋʀ ᴍᴜᴛʜ ʙʜᴀʀ ᴅᴜɢᴀ ! 😆",
    "𝐓ᴇʀɪ ᴍᴀᴀ ʙʜᴛ ʀᴏᴛɪ ᴇʏ ʙɪʟᴋᴜʟ 𝐓ᴇʀɪ ᴛʀʜ ᴅᴏɴᴏ ʀɴᴅʏ ʀᴏɴᴀ ᴋʀᴛᴇ ʜᴏ ᴇᴡᴡ ! 😆",
    "𝐓ᴇʀɪ ʙʜᴇɴ ᴋɪ ɢᴜʟᴀʙɪ ᴄʜᴛ ᴋᴀᴀᴛ ᴅᴜɢᴀ ɢᴜʟᴀᴍ ! 😆",
    "𝐂ʜʟ ɢᴜʟᴀᴍ ɢᴜʟᴀᴍɪ ᴋʀ ! 😾",
]

NC2_WORDS = [
    "ᴛᴇʀɪ ᴍᴀᴀ ᴋɪ ᴄʜᴜᴛ","ʀɴᴅʏᴘᴜᴛʀᴀ","ᴛᴇʀɪ ᴍᴀᴀ ᴋᴀ ʙʜᴏꜱᴅᴀ",
    "ᴍᴀᴅᴀʀᴄʜᴏᴅ","ᴍᴀᴀ ᴋᴇ ʟᴀɴᴅ","ʙʜᴇɴᴄʜᴏᴅ","ʙʜᴇɴ ᴋᴇ ʙʜᴏꜱᴅᴇ",
    "ʙʜᴏꜱᴅɪᴋᴇ","ᴛᴇʀᴇ ʙᴀᴀᴘ ᴋɪ ᴄʜᴜᴛ","ᴄʜᴀᴍᴀʀ","ʀᴀɴᴅʏ","ʜᴀʀᴀᴍɪ",
    "ᴛᴀᴛᴛɪ ᴋᴇ ᴋᴇᴇᴅᴇ","ᴛᴍᴋʙ","ᴛᴍᴋᴄ","ᴛʙᴋᴄ","ᴛʙᴋʙ","ɢᴀʀᴇᴇʙ",
    "ɢᴜʟᴀᴍ","ᴄʜᴜᴅ","ʙᴄ","ᴍᴄ","ᴋᴜᴛᴛɪ","ᴋᴜᴛᴛᴀ",
]

NC3_WORDS = [
    "𝙏𝙈𝙆𝘾 𝙈𝙄𝙀 𝙆𝙐𝙏𝙏𝙀 𝙆𝘼 𝙇𝙉𝘿",
    "𝙊𝙔𝙀 𝙏𝙐 𝙈𝘼𝙍𝘼 𝙆𝘼𝙄𝙎𝙀 𝙂𝘼𝙍𝙀𝙀𝘽 𝘾𝙑𝙍 𝙆𝙍",
    "𝙊𝙔𝙀 𝙏𝙀𝙍𝙄 𝙈𝘼𝙐𝙎𝙄 𝙆𝙄 𝘾𝙃𝙐𝙏 𝙈𝘼𝘼𝙍 𝘿𝙐 𝙍𝙊𝙔𝙀𝙂𝘼 𝙏𝙊 𝙉𝘼‌𝙄 ?",
    "𝙏𝙈𝙆𝘾 𝙍𝙉𝘿𝙔 𝙆𝙀 𝙂𝙐𝙇𝘼𝙈𝙄 𝙆𝙍 𝘾𝙃𝙐𝙋 𝘾𝙃𝘼𝙋",
    "𝙊𝙔𝙀 𝘽𝙎𝘿𝙆 𝙃𝘼𝙒𝘼𝘽𝘼𝘼𝙕 𝙏𝘼𝙏𝙏𝙀 𝘽𝙃𝘼𝙂 𝙈𝙏",
    "𝙏𝙈𝙆𝙁𝘽","𝙍𝙉𝘿𝙔","𝙏𝙀𝙍𝙄 𝙈𝘼𝘼 𝙈𝘼𝙍 𝙂𝙔𝙄","𝙏𝘽𝙆𝘾",
    "𝙏𝙈𝙆𝘾 𝙈𝙄𝙀 𝙈𝘼𝙂𝙂𝙄𝙀","𝙏𝘽𝙆𝘽 𝙈𝙄𝙀 𝙇𝙉𝘿","𝙏𝙀𝙍𝙄 𝙂𝙉𝘿 𝙈𝙄𝙀 𝙆𝙐𝙏𝙏𝘼",
    "𝙂𝙐𝙇𝘼‌𝙈𝙄 𝙆𝙍","𝙆𝙀𝙀𝘿𝙀","𝘼𝙐𝙆𝘼𝘼𝙏 𝘽𝙉𝘼","𝙂𝘼𝙍𝙀𝙀𝘽","𝘽𝙎𝘿𝙆","𝘾𝙃𝙈𝙍",
    "𝙏𝙈𝙆𝘾 𝙈𝙄𝙀 𝙇𝘼𝙏𝙏 𝙂𝙐𝙇𝘼𝙈𝙄 𝙆𝙍",
    "𝙏𝙀𝙍𝙄 𝙈𝘼 𝙆𝘼 𝘽𝙃𝙊𝙎𝘿𝘼 𝙈𝙀 𝙈𝙐𝙏𝙃 𝘽𝙃𝘼𝙍",
    "𝙏𝙀𝙍𝙄 𝘽𝙃𝙀𝙉 𝙆𝙄 𝘾𝙃𝙐𝙏 𝙈𝙀 𝙋𝘼𝙄𝙍 𝙈𝘼𝙍",
]

NC1_PATTERN = "{text} {word} 𓏲 ๋࣭   ࣪ ˖ {emoji} 𓂃 ࣪˖ ִֶ♱ ྀིྀ"
NC2_PATTERN = "{text} {word} ˚˖𓍢ִ໋˚{emoji}ೀ"
NC3_PATTERN = "{text} ⋆.ೃ࿔*:･{emoji}⋆.ೃ࿔*:･"
NC4_PATTERN = "{text}{emoji}ܓ"
SFNC_PATTERN = "˚⊱{emoji}⊰˚ {text} ˚⊱{emoji}⊰˚"
LOVENC_PATTERN = "{text} {word} {emoji}"
MUTTHINC_PATTERN = "{text}ᵀᵉʳⁱ ᵐᵃᵃ ᵏᵉ ᵇᵘʳ ᵐᵃⁱ{word}sailab"
BLOODNC_PATTERN = "{text}★彡 𝗧𝗲𝗿𝗶 𝗺𝗮𝗮 𝗸𝗶 𝗰𝗵𝘅𝘁 𝘀𝗲 彡★{word} 𝗞𝗮 𝗯𝗮𝗿𝗶𝘀𝗵"

# ═══════════════════════════════════════════
# BIG NC RAILS — 3x + mega size
# ═══════════════════════════════════════════
NC_HEAVY_RAIL = "𒈙🌌𒈙✨𒈙💎𒈙🦄𒈙🔮𒈙🕊️" * 3
NC_KNOT_RAIL  = "꧅" * 120
NC_HEART_RAIL = "𓆩♡𓆪" * 30
NC_BLOOD_RAIL = "🩸" * 60
NC_STAR_RAIL  = "✨" * 60
NC_MOON_RAIL  = "🌙" * 30
NC_SPIKE_RAIL = "𒐫𒐫𒐫💠" * 12

RAIL_LOVE  = "𓆩♡𓆪 " * 20
RAIL_HEAVY = "𒐫𒐫𒐫💠" * 10
RAIL_SPIKE = "𒐫" * 15 + "💠" + "𒐫" * 15 + "💠"
RAIL_MEGA  = RAIL_LOVE + RAIL_HEAVY

SHADOW_HDR = "⚡ 𝐒 𝐇 𝐀 𝐃 𝐎 𝐖 ⚡"

MEGA_NC = [
    "⚡ 𝐒 𝐇 𝐀 𝐃 𝐎 𝐖 ⚡ {text} {word} " + RAIL_MEGA,
    "⚡ 𝐒 𝐇 𝐀 𝐃 𝐎 𝐖 ⚡ {text} {word} ⚡ 𝐆 𝐔 𝐋 𝐀 𝐌 ⚡ " + RAIL_MEGA,
    "{text} {word} " + RAIL_SPIKE + RAIL_LOVE,
    "⚡ 𝐒 𝐇 𝐀 𝐃 𝐎 𝐖 ⚡ {text} " + ("{word} " * 6) + RAIL_MEGA,
    RAIL_LOVE + " ⚡ {text} {word} ⚡ " + RAIL_HEAVY,
    RAIL_MEGA + " ⚡{text}⚡ " + RAIL_MEGA,
    "𓆩♡𓆪" * 10 + "𒐫💠" * 8 + "⚡ {text} {word} ⚡ " + "𒐫💠" * 8 + "𓆩♡𓆪" * 10,
    "▀▄▀▄ 𝐒𝐇𝐀𝐃𝐎𝐖 ▄▀▄▀ ⚡ {text} {word} ⚡ " + RAIL_MEGA,
    # heavy rail (new)
    "{text} {word} Tmkc 🤪 " + NC_HEAVY_RAIL + " >>  <{emoji}> . ݁₊ ⊹ . ݁",
    # knot wall (new)
    "{text} ˚⊱━━😈━━⊰˚Cʜᴜᴘ Cʜᴀᴘ Cʜᴜᴅ Rɴᴅʏᴋ\n" + NC_KNOT_RAIL + " {emoji}⋆ ִֶָ˖·˳˖𓂃 ִֶָ",
    # heart 3x (new)
    "{text} ⋆｡°✩ " + NC_HEART_RAIL + " ✩°｡⋆ {word} " + NC_HEART_RAIL,
    # shadow + heart sandwich (new)
    SHADOW_HDR + " " + NC_HEART_RAIL + " {text} {word} " + NC_HEART_RAIL + " " + SHADOW_HDR,
    # blood flood (new)
    "{text} " + NC_BLOOD_RAIL + " {word} " + NC_BLOOD_RAIL + " <{emoji}>",
    # spike + knot (new)
    "{text} " + NC_SPIKE_RAIL + " {word}\n" + NC_KNOT_RAIL + " {emoji}",
    # star + moon (new)
    "{text} " + NC_STAR_RAIL + " {word} " + NC_MOON_RAIL + " {emoji}",
    # shadow block header (new)
    "▀▄▀▄ 𝐒 𝐇 𝐀 𝐃 𝐎 𝐖 ▄▀▄▀ {text} {word} " + NC_HEART_RAIL + " <{emoji}>",
]

MEGA_WORDS = [
    "𝐒ʜᴀᴅᴏᴡ","𝐓ᴍᴋᴄ","𝐑ɴᴅʏᴘᴜᴛʀᴀ","𝐌ᴀᴅᴀʀᴄʜᴏᴅ","𝐁ʜᴇɴᴄʜᴏᴅ",
    "𝐆ᴜʟᴀᴍ","𝐊ᴇᴇᴅᴇ","𝐂ʜᴜᴘ","𝐆ᴀʀᴇᴇʙ","𝐇ᴀʀᴀᴍɪ",
    "𝐓ᴍᴋʙ","𝐓ᴍᴋᴄ 𝐁ᴏᴍʙ","𝐁ꜱᴅᴋ","𝐒ʜᴀᴅᴏᴡ 𝐆ᴜʟᴀᴍ",
]

# ─── h8rs line block with name slot ───
def h8rs_line(name: str, emoji: str = "❄️") -> str:
    n = (name or "shadow")[:20]
    return f"𓆩{n}𓆪 #𝐎ყᴇ #𝐁ᴇᴛꪖ #𝐓ʀყ #𝐌ꪮ𝐌 #𝐑ᴀɴᴅყ ({emoji})"

def h8rs_block(name: str, emoji: str = "❄️", count: int = 20) -> str:
    line = h8rs_line(name, emoji)
    return "\n".join([line] * count)

# ─── dedicated ncknot / ncheavy / ncheart patterns ───
NCKNOT_PATTERNS = [
    "{text} " + NC_KNOT_RAIL + " {emoji}",
    "{text} ˚⊱━━😈━━⊰˚Cʜᴜᴘ Cʜᴀᴘ Cʜᴜᴅ Rɴᴅʏᴋ\n" + NC_KNOT_RAIL + " {emoji}⋆",
    NC_KNOT_RAIL + " ⚡{text}⚡ " + NC_KNOT_RAIL,
    "{text} " + ("꧅" * 60) + " {word} " + ("꧅" * 60),
]

NCHEAVY_PATTERNS = [
    "{text} {word} Tmkc 🤪 " + NC_HEAVY_RAIL + " >>  <{emoji}> . ݁₊ ⊹ . ݁",
    "⚡ 𝐒 𝐇 𝐀 𝐃 𝐎 𝐖 ⚡ {text} {word} " + NC_HEAVY_RAIL + " <{emoji}>",
    "{text} " + NC_HEAVY_RAIL + " {word} " + NC_HEAVY_RAIL + " <{emoji}>",
    NC_HEAVY_RAIL + " ⚡{text} {word}⚡ " + NC_HEAVY_RAIL,
]

NCHEART_PATTERNS = [
    "{text} ⋆｡°✩ " + NC_HEART_RAIL + " ✩°｡⋆ {word} " + NC_HEART_RAIL,
    SHADOW_HDR + " " + NC_HEART_RAIL + " {text} {word} " + NC_HEART_RAIL + " " + SHADOW_HDR,
    NC_HEART_RAIL + " ⚡ {text} {word} ⚡ " + NC_HEART_RAIL,
    "{text} " + NC_HEART_RAIL + " {word} " + NC_HEART_RAIL + " {emoji}",
]

# ─── SPAM ───
SPAM1_LINE_PATTERN = "{text} 𝐓ꫀʀɪ 𝐌ꫝꫝ ꫝꜱᴍᴀɴ ᴍɪꫀ ᥴʜᴜᴅꫀɢɪ   ⊹ ࣪ ˖{emoji}⊹ ࣪˖"
SPAM2_LINE_PATTERN = "{text} 𝐑ᴀɴᴅᴏᴍ 𝐊ᴜᴛᴛɪ ᴋᴇ ʟᴀᴅᴋᴇ 𝐄ɴᴊᴏʏ ʏᴏᴜʀ ꜱᴡᴇᴇᴛ 𝐂ʜᴜᴅᴀɪ  {emoji}ܓ"
SPAM3_LINE_PATTERN = "{text} 𝐓ᴇʀɪ 𝐁ʜᴇɴ 𝐄ᴋ 𝐔ɴɪᴠᴇʀꜱᴀʟ 𝐑ɴᴅʏ ᴇʏ ʙᴀᴀᴛ ᴋʜᴛᴍ !!\n\n━━━━━━━━━━━━━━━{emoji}"
SPAM4_LINE_PATTERN = "⁺‧₊˚ ཐི {text} ཋྀ ˚₊‧⁺ 𝐒𝐇𝐀𝐃𝐎𝐖 papa का 𝐋ᴀᴜᴅᴀ 𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐊ɪ 𝐏ᴜꜱꜱʏ 𝐌ᴇ hold tight 💦 <{emoji}>"
SPAM5_LINE_PATTERN = "𓆩{text}𓆪 𝐓ᴇʀɪ 𝐌𝐚𝐚 𝐊ɪ 𝐂ʜᴜᴛ 𝐏ʀ 𝐒𝐇𝐀𝐃𝐎𝐖 ka lamba lumnd ⃟🌷꙰⃟𓆩"

def gen_spam1(t,e): return "\n".join([SPAM1_LINE_PATTERN.format(text=t,emoji=e),""]*10)
def gen_spam2(t,e): return "\n".join([SPAM2_LINE_PATTERN.format(text=t,emoji=e),""]*10)
def gen_spam3(t,e): return "\n".join([SPAM3_LINE_PATTERN.format(text=t,emoji=e),""]*10)
def gen_spam4(t,e): return "\n".join([SPAM4_LINE_PATTERN.format(text=t,emoji=e),""]*10)
def gen_spam5(t):   return "\n".join([SPAM5_LINE_PATTERN.format(text=t),""]*10)

SLIDE1_MESSAGES = [
    "𝑯𝒆𝒚 !¡ 𝒊 𝒈𝒖𝒆𝒔𝒔 𝒚𝒐𝒖𝒓 𝒎𝒐𝒎𝒎𝒚 𝒓𝒂𝒕𝒆 𝒊𝒔 𝒕𝒐𝒐 𝒍𝒐𝒘 𝒊𝒔 𝒊𝒕 𝒓𝒆𝒂𝒍 🙁",
    "𝑯𝒆𝒚 𝒌𝒊𝒅𝒅𝒐 𝒈𝒐 𝒂𝒏𝒅 𝒕𝒆𝒍𝒍 𝒖𝒓 𝒎𝒐𝒎 𝒕𝒉𝒂𝒕 𝒉𝒆𝒓 𝒉𝒖𝒔𝒃𝒂‌𝒏𝒅 𝒊𝒔 𝒃𝒂𝒄𝒌 𝒉𝒐𝒎𝒆 !! 😆",
    "𝒀𝒐𝒖 𝒓𝒂𝒏𝒅𝒐𝒎 𝒏𝒊𝒈𝒈𝒂 𝒇𝒖𝒄𝒌 𝒚𝒐𝒖𝒓𝒔𝒆𝒍𝒇 𝒘𝒊𝒕𝒉 𝒕𝒉𝒊𝒔 𝒅𝒊𝒍𝒅𝒐 ! 😡",
    "𝒀𝒐𝒖 𝒏𝒈 𝒌𝒊𝒅 𝒄𝒐𝒎𝒆 𝒂𝒏𝒅 𝒈𝒊𝒗𝒆 𝒂 𝒔𝒂𝒍𝒖𝒕𝒆 𝒕𝒐 𝒚𝒐𝒖𝒓 𝑫𝒂𝒅 ! 😏",
    "𝑶𝒌𝒂𝒚 𝑰 𝒘𝒊𝒍𝒍 𝒔𝒕𝒐𝒑 𝒇𝒖𝒄𝒌𝒊𝒏𝒈 𝒚𝒐𝒖𝒓 𝒎𝒐𝒎 𝒃𝒖𝒕 𝒊𝒏 𝒑𝒍𝒂𝒄𝒆 𝒐𝒇 𝒉𝒆𝒓 𝑰 𝒏𝒆𝒆𝒅 𝒚𝒐𝒖𝒓 𝑺𝒊𝒔 ! 🥰",
    "𝑰 𝒔𝒂𝒊𝒅 𝒄𝒍𝒆𝒂𝒏 𝒕𝒉𝒆 𝒇𝒍𝒐𝒐𝒓 𝒑𝒓𝒐𝒑𝒆𝒓𝒍𝒚 𝒏𝒐𝒕 𝒔𝒐 𝑰 𝒘𝒊𝒍𝒍 𝒄𝒖𝒕 𝒚𝒐𝒖𝒓 𝒔𝒂𝒍𝒂𝒓𝒚 𝒚𝒐𝒖 𝒃𝒍𝒐𝒐𝒅𝒚 𝒃𝒆𝒈𝒈𝒂𝒓 ! 😠",
    "𝐖ᴏ ʙʜɪ ᴋʏᴀ ᴅɪɴ ᴛʜᴇ ᴊᴀʙ 𝐒ʜᴀᴅᴏᴡ ᴍᴜᴊʜᴇ 𝐀ᴘɴᴀ 𝐂ʜᴜᴛ 𝐃ᴇᴛɪ ᴛʜɪ ʏᴀᴀʀ 💔🥀👌🏻",
    "𝐀ᴡᴀᴢ 𝐍ɪᴄʜᴇ 𝐆ᴜʟᴀᴀᴍ 🤢👇🏻",
    "𝐓ʀʏ 𝐌ᴀᴀ ɴᴇ 𝐂ʜᴜᴅɴᴇ 𝐌ᴀɪ ɢᴏʟᴅ 𝐌ᴇᴅᴀʟ 𝐉ᴇᴇᴛᴀ ᴇʏ 𝐃ᴏꜱᴛ 🤩👑",
    "𝐓ᴇʀɪ 𝐌ᴀᴀ ᴋɪ 𝐂ʜᴜᴛ 𝐌ᴇ 𝐌ᴇʀᴀ 𝐋ᴜɴᴅ 🖕🏻😈",
    "𝐁ʜᴏꜱᴀᴅɪᴋᴇ 𝐀ᴘɴɪ 𝐁ᴇʜᴇɴ 𝐂ʜᴜᴅᴀ 🖕🏻😈",
    "𝐑ᴀɴᴅɪ ᴋᴇ 𝐁ᴀᴄᴄʜᴇ 𝐀ᴜᴋᴀᴛ 𝐌ᴇ 𝐑ᴇʜ 🖕🏻😈",
    "𝐌ᴀᴅᴀʀᴄʜᴏᴅ 𝐓ᴇʀɪ 𝐌ᴀᴀ ᴋɪ 𝐂ʜᴜᴛ 🖕🏻😈",
    "𝐓ᴇʀɪ 𝐌ᴀᴀ ᴋᴀ 𝐁ʜᴏꜱᴅᴀ ᴋʜᴏʟ ᴅᴜɴɢᴀ 🔓😈",
    "𝐁ʜᴇɴᴄʜᴏᴅ 𝐀ᴘɴɪ 𝐀ᴜᴋᴀᴛ 𝐌ᴇ 𝐑ᴇʜ 🤡💩",
    "𝐓𝐌𝐊𝐂 ᴘᴇ 𝐂ʜᴀᴘᴘᴀʟ 𝐌ᴀᴀʀᴜɴɢᴀ 👟💥",
    "𝐁ʜᴏꜱᴅɪᴋᴇ 𝐓ᴇʀɪ 𝐊ʜᴀɴᴅᴀɴ ᴋɪ 𝐁𝐊𝐂 💀🖕🏻",
    "𝐑ᴀɴᴅɪ ᴋɪ 𝐀ᴜʟᴀᴅ ᴄʜᴜᴘ ʜᴏ ᴊᴀ 🔇😒",
    "𝐆ᴜʟᴀᴀᴍ ʜᴇɪ ᴛᴜ 𝐒ʜᴀᴅᴏᴡ ᴋᴀ ᴀʙ ᴀᴜʀ ʀᴀʜᴇɢᴀ ʙʜɪ 👑😎",
    "𝐓ᴇʀɪ 𝐁ᴇʜᴇɴ ᴋɪ 𝐂ʜᴜᴛ 𝐌ᴇ 𝐌ɪʀᴄʜɪ 🌶️🖕🏻",
    "𝐌ᴀᴅᴀʀᴄʜᴏᴅ 𝐓ᴇʀɪ 𝐌ᴀᴀ ᴋɪ 𝐂ʜᴜᴛ 𝐌ᴇ 𝐏ᴀɪʀ 🦶🏻😈",
    "𝐁ʜᴏꜱᴀᴅɪᴋᴇ 𝐓ᴇʀɪ 𝐁ᴇʜᴇɴ ᴋᴀ 𝐁ʜᴏꜱᴅᴀ 🗑️😏",
    "𝐑ᴀɴᴅɪ ᴋᴀ 𝐏ɪʟʟᴀ ʜᴀɪ ᴛᴜ 🐕💩",
    "𝐓ᴇʀɪ 𝐌ᴀᴀ ᴋᴏ 𝐁ᴀᴢᴀᴀʀ 𝐌ᴇ 𝐂ʜᴏᴅᴜɴɢᴀ 🌃😈",
    "𝐓ᴇʀɪ 𝐌ᴀᴀ ᴋɪ 𝐂ʜᴜᴛ 𝐌ᴇ 𝐆ᴀʀᴀᴍ 𝐓ᴇʟ 🌡️🖕🏻",
    "𝐌ᴀᴅᴀʀᴄʜᴏᴅ 𝐓ᴇʀɪ 𝐁ᴇʜᴇɴ ᴍᴇʀɪ 𝐑ᴀɴᴅɪ 💋👿",
    "𝐑ᴀɴᴅɪ ᴋᴇ 𝐁ᴀᴄᴄʜᴇ 𝐓ᴇʀɪ 𝐌ᴀᴀ ᴋɪ 𝐂ʜᴜᴛ 🖕🏻😈",
    "𝐓ᴇʀɪ 𝐁ᴇʜᴇɴ ᴋᴏ 𝐑ᴀᴀᴛ ʙʜᴀʀ 𝐂ʜᴏᴅᴜɴɢᴀ 🌙😈",
    "𝐑ᴀɴᴅɪ ᴋᴀ 𝐁ᴀᴄᴄʜᴀ ʜᴀɪ ᴛᴜ ꜱᴀᴀʟᴇ 🤡💀",
    "𝐓ᴇʀɪ 𝐌ᴀᴀ ᴋɪ 𝐂ʜᴜᴛ 𝐌ᴇ 𝐌ᴇʀᴀ 𝐉ᴏᴏᴛᴀ 👞🖕🏻",
    "𝐒ʜᴀᴅᴏᴡ 𝐃ᴀᴅʏ ᴋᴀ 𝐆ᴜʟᴀᴀᴍ ʜᴀɪ ᴛᴜ 🥀😤",
    "ᴊɪꜱ ᴅɪɴ ᴛᴜ ᴘᴀɪᴅᴀ ʜᴜᴀ 𝐓ᴇʀɪ 𝐌ᴀᴀ ɴᴇ ꜱᴏᴄʜᴀ ᴛʜᴀ ᴋᴀꜱʜ ᴀʙᴏʀᴛ ᴋᴀʀ ᴅᴇᴛɪ 💀🥀",
    "𝐀ᴘɴɪ 𝐀ᴜᴋᴀᴛ ᴅᴇᴋʜ ᴋᴜᴛᴛᴇ 🐕😂",
    "𝐆ᴀʟɪ ᴋᴀ 𝐊ᴜᴛᴛᴀ ʜᴀɪ ᴛᴜ 🐕🗑️",
    "𝐓ᴇʀɪ 𝐌ᴀᴀ ɴᴇ ᴍᴜᴊʜᴇ ᴅᴇᴋʜ ᴋᴇ ꜱᴏᴄʜᴀ ᴋᴀꜱʜ ʏᴇ 𝐒ʜᴀᴅᴏᴡ ʜᴏᴛᴀ 🫦😏",
    "𝐂ʜᴜᴘ ᴋᴀʀ 𝐌ᴀᴅᴀʀᴄʜᴏᴅ ᴛᴇʀɪ ᴀᴜᴋᴀᴛ ɴᴀʜɪ 𝐒ʜᴀᴅᴏᴡ ᴋᴇ ꜱᴀᴀᴍɴᴇ ʙᴏʟɴᴇ ᴋɪ 🤐💀",
    "𝐓ᴇʀɪ 𝐌ᴀᴀ ᴋɪ 𝐂ʜᴜᴅᴀɪ ᴍᴇ ᴊᴀʙ 𝐒ʜᴀᴅᴏᴡ ᴛʜᴀ ᴛᴏ ᴛᴜ ᴘᴀɪᴅᴀ ʜᴜᴀ 💀😂",
    "𝐁ʜᴀɢ ʏᴀʜᴀɴ ꜱᴇ ᴋᴜᴛᴛᴇ ᴋᴇ ᴘɪʟʟᴇ 🐕💨",
    "𝐓ᴇʀɪ 𝐁ᴇʜᴇɴ ᴋɪ ꜱᴀᴅɪ 𝐌ᴇ 𝐒ʜᴀᴅᴏᴡ ᴋᴀ ʟᴜɴᴅ 💍😈",
    "𝐌ᴀᴅᴀʀᴄʜᴏᴅ ᴀᴘɴɪ 𝐌ᴀᴀ ᴍᴀᴛ ᴄʜᴜᴅᴀ 𝐒ʜᴀᴅᴏᴡ 🖕🏻👹",
]

SLIDE2_MESSAGES = [
    "𝗧𝗔𝗧𝗧𝗘","𝗚𝗨𝗟𝗔𝗠","𝗠𝗔𝗗𝗔𝗥𝗖𝗛𝗢𝗗","𝗕𝗛𝗘𝗡𝗞𝗟𝗡𝗗","𝗧𝗠𝗞𝗖","𝗧𝗠𝗞𝗕",
    "𝗥𝗡𝗗𝗬","𝗚𝗔𝗥𝗘𝗘𝗕","𝗦𝗛𝗔𝗗𝗢𝗪 𝗞𝗘 𝗟𝗔𝗗𝗞𝗘","𝗚𝗡𝗗𝗨","𝗖𝗛𝗔𝗣𝗥𝗜","𝗖𝗛𝗠𝗥",
    "𝗕𝗦𝗗𝗞","𝗞𝗘𝗘𝗗𝗘","𝗖𝗛𝗨𝗗","𝗧𝗕𝗞𝗟","𝗛𝗔𝗥𝗔𝗠𝗞𝗛𝗢𝗥","𝗥𝗥 𝗠𝗧 𝗞𝗥",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗠𝗔𝗥 𝗚𝗬𝗜","𝗧𝗘𝗥𝗜 𝗕𝗛𝗘𝗡 𝗖𝗛𝗨𝗗𝗚𝗬𝗜","𝗚𝗨𝗟𝗔𝗠𝗜 𝗞𝗥",
    "𝑮𝑪 𝑳𝑬𝑭𝑻 𝑳𝑬 लंगड़ी ᴍᴀᴀ ᴋᴇ ʙᴀᴄʜᴇ 🤮",
    "Tmkc pe chppl hi chppl marunga !! 🔥😂🩴",
    "𝐂ʜʟ 𝐇ᴀʀᴍᴢᴀᴅ𝐈 𝐊ᴇ लड़के 💛🤍🩵",
    "sort nhi krunga chud tu bina ruke 🤢🔥",
    "काले Doraemon रोता reh 🤣🤣",
    "Awaz neeche rndy k bacche 🤢🔥",
    "𝙇𝙐𝙉𝘿 𝘾𝙃𝙐𝙎 🥶➿🩵 𝙈𝘼𝘿𝘼𝙍𝘾𝙃𝙊𝘿",
    "Sawal mt puch tery ma k bosda 😹🖕🏻",
    "Are try maa ka bosda 🤢᭄᭄᭄ 🌟 𝙇𝙐𝙉𝘿 𝘾𝙃𝙐𝙎 🤪᭄᭄",
    "fyter bnege langde madarchod 😂💥",
    "𝟏𝐱 𝐀ɴ𝐘 𝐂ʜ𝐋 𝐏ɪʟʟ𝐄 𝐍ᴏᴛ𝐈 𝐂ʟᴀɪ𝐌 𝐊ᴀ𝐑 🩷🩵🩶",
    "try maa > Mia Khalifa 🥵💯",
    "baap se fyt krega 😂😂 ?",
    "ATMKBFJ 🥀",
    "Mᴀᴀ Kᴇ Sᴀᴛʜ bhen ᗷᕼI ᥴᕼꪊ໓ ᭙ꫝꪶi 🤢🔥",
    "Teri maa ko Gachar Gachar codunga 😹❌🔥",
    "रंडीꪻ ♡︎ 🎀",
    "𝐓𝐆 𝐅𝐘𝐓𝐄𝐑 𝐁𝐍𝐄𝐆𝐀 ?? 𝐂𝐇𝐎𝐃𝐔 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 😂😂",
    "𝐓𝐎𝐓𝐋𝐄 𝐓𝐌𝐊𝐂 𝐌𝐄 𝐁𝐎𝐌𝐁 𝐅𝐄𝐊𝐃𝐔 💣💥",
    "Ｔᴏʜᴀʀ Ｍᴀɪʏᴀ Ｃʜᴀɪʏᴀ Ｃʜᴀɪʏᴀ 🤢🔥🤢🔥",
    "𝙏𝙚𝙧𝙞 𝙢𝙖𝙖 𝙠𝙚 𝙗𝙝𝙤𝙨𝙙𝙚 𝙢𝙚 𝙡𝙖𝙩 𝙥𝙙𝙚𝙣𝙜𝙚 𝙗𝙝𝙤𝙩 𝙩𝙚𝙯 👻💥",
    "🦅🔥 Tᴇʀɪ 🦅🔥 Mᴀᴀ 🦅🔥 Rɴᴅɪ 🦅🔥",
    "कि बेहन 𝗧𝗔𝗞𝗟𝗜 💙",
    "𝗚𝗨𝗟𝗔𝗠 🥱👞",
    "ʙꪊʟʟʏ केन्द्र ᥫ😂᭄",
    "तेरी माँ कि 𝘾ʜᴜᴛ में જ⁀➴🧨᭄",
    "𝘙𝘈𝘕𝘋 𝘽𝙃𝙀𝙀𝙆 𝙈𝘼𝙉𝙂 😹😹",
    "𝙎𝙐𝙋𝙋𝙊𝙍𝙏 𝙇𝘼 🤲🏿",
    "༆🤮꧂तेरी मांँ 売春婦 ᥫ😆᭄",
    "𝘽𝘼𝙐𝙉𝙀 मादरचोद ꧁🤮꧂",
    "𝐓𝐌𝐊𝐁 😹",
]

SLIDE3_MESSAGES = [
    "𝐒ʜᴀᴅᴏᴡ 𝐓ᴍᴋʙ 𝐑ɴᴅʏ ᴋᴇ 𝐋ᴀᴅᴋᴇ 😈🖕🏻😈🖕🏻😈",
    "𝐓ᴇʀɪ ᴍᴀᴀ ᴍᴀʀ ɢʏɪ ¿😆😆😆",
    "𝐒ʜᴀᴅᴏᴡ ᴋᴇ ꜱᴀᴍᴀɴᴅᴀʀ 🥰🖕🏻🥰🖕🏻🥰🖕🏻",
    "𝐓ᴇʀɪ 𝐌ᴀᴀ ʜᴜᴍᴇꜱʜᴀ ᴍᴜᴊʜꜱᴇ ʜɪ ᴋʏᴜ चुडती है ¡! 😡🤬😡🤬😡",
    "𝐃ᴇᴋʜ ᴀᴀᴊ ᴛᴇʀɪ 𝐌ᴀᴀ ᴋᴀ ɴᴀɴɢᴀ ᴅᴀɴᴄᴇ ᴅɪᴋʜᴀᴜ ! 🩰🧑🏻‍🩰",
    "𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐊ɪ 𝐆ᴜʟᴀʙɪ 𝐂ʜᴜᴛ ᴍɪᴇ 𝐌ᴜᴛ ᴋʀ ʙʜᴀɢ ᴊᴀᴜɢᴀ 𝐁ꜱᴅᴋ ! 😆",
    "𝐓ᴇʀɪ 𝐌ᴀᴀ ᴄʜᴏᴅɴᴇ ᴀʀʜᴀ ʜᴜ ʀᴜᴋ ᴡʜɪ ɢᴜʟᴀᴍ ! 😾",
    "𝐓ᴇʀɪ ʙʜᴇɴ ᴋᴇ ʙᴏᴏʙɪᴇꜱ ᴋᴇ ʙᴇᴇᴄʜ ᴍɪᴇ ʟɴᴅ ꜰᴀꜱᴀ ᴋʀ ᴍᴜᴛʜ ᴍᴀᴀʀ ᴅᴜɢᴀ ʙꜱᴅᴋ 😆",
    "𝐓ᴇʀɪ ᴍᴀᴀ ᴋɪ ᴄʜᴜᴛ ᴍɪᴇ ᴍᴀɢɢɪᴇ ʙɴᴀ ᴋʀ ᴍᴜᴛʜ ʙʜᴀʀ ᴅᴜɢᴀ ! 😆",
    "𝐓ᴇʀɪ ᴍᴀᴀ ʙʜᴛ ʀᴏᴛɪ ᴇʏ ʙɪʟᴋᴜʟ 𝐓ᴇʀɪ ᴛʀʜ ᴅᴏɴᴏ ʀɴᴅʏ ʀᴏɴᴀ ᴋʀᴛᴇ ʜᴏ ᴇᴡᴡ ! 😆",
    "𝐓ᴇʀɪ ʙʜᴇɴ ᴋɪ ɢᴜʟᴀʙɪ ᴄʜᴛ ᴋᴀᴀᴛ ᴅᴜɢᴀ ɢᴜʟᴀᴍ ! 😆",
    "𝐂ʜʟ ɢᴜʟᴀᴍ ɢᴜʟᴀᴍɪ ᴋʀ ! 😾",
]

SLIDE4_PATTERN = "{text}     ⃟🌷꙰⃟"

LOVENC_WORDS = [f"I love you {i} {e}" for i, e in enumerate([
    "🌹","❤️","💖","💕","💘","💝","💗","💓","💞","💌","🥰","😘","😍","🌺","🌸","🌷","🪷","💐","🍓","🍒",
    "🍫","🍯","🧸","🫶","🤍","🩷","💜","💙","💚","🧡","💛","🌈","✨","⭐","🌟","☀️","🌙","💫","☁️","🕊️",
    "🦋","🐻","🐼","🐰","🐱","🐶","🦄","🦢","🦩","🐬","🌊","🍀","🌼","🌻","🍁","🍂","🌹❤️","💖🌸","🥺💗","🫂",
    "💍","🎀","🎁","🍭","🍬","🧁","🍰","🎂","☕❤️","🍕❤️","🎵","🎶","🎧","📸","🎬","🎈","🎉","🎊","🔥❤️","⚡❤️",
    "🌍❤️","🪐","☄️","🌌","💎","👑","🕯️","🫰","🤗","😊❤️","♾️❤️","🥹💖","💋","😚","😙","💑","👩‍❤️‍👨","💒","❤️‍🔥","♾️💞",
], 1)]

if os.path.exists(SUDO_FILE):
    try:
        with open(SUDO_FILE, "r", encoding="utf-8") as f:
            _loaded = json.load(f)
            SUDO_USERS = set(int(x) for x in _loaded)
    except Exception:
        SUDO_USERS = {OWNER_ID}
else:
    SUDO_USERS = {OWNER_ID}

def save_sudo():
    with open(SUDO_FILE, "w", encoding="utf-8") as f:
        json.dump(list(SUDO_USERS), f)

UNAUTHORIZED_MSG = "🐉🔥ᴾᵃⁱʳ ᵖᵉ ᵖᵃᵈᵏᵉ ㅤ𝐒𝐇𝐀𝐃𝐎𝐖 ˢᵉ ᵇʰⁱᵏ ᵐᵃᵃⁿᵍ ᵍᵃʳⁱᵇ ᵏᵉ ᵇᵃᶜᶜʰᵉ💦🤪"

def only_sudo(func):
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE):
        if not update.effective_user: return
        uid = update.effective_user.id
        if uid != OWNER_ID and uid not in SUDO_USERS:
            await update.message.reply_text(UNAUTHORIZED_MSG); return
        return await func(update, context)
    return wrapper

def only_owner(func):
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE):
        if not update.effective_user: return
        uid = update.effective_user.id
        if uid != OWNER_ID:
            await update.message.reply_text(UNAUTHORIZED_MSG); return
        return await func(update, context)
    return wrapper

# ═══════════════════════════════════════════
# NC WORKERS
# ═══════════════════════════════════════════
async def nc1_worker(bot, chat_id, base_text, counter_dict):
    while True:
        try:
            emoji = random.choice(FLOWER_EMOJIS); word = random.choice(NC1_WORDS)
            text = NC1_PATTERN.format(text=base_text, word=word, emoji=emoji)
            await bot.set_chat_title(chat_id, text[:250])
            counter_dict[chat_id] = counter_dict.get(chat_id, 0) + 1
        except asyncio.CancelledError: break
        except telegram_error.Forbidden: break
        except telegram_error.BadRequest: pass
        except: pass

async def nc2_worker(bot, chat_id, base_text, counter_dict):
    while True:
        try:
            emoji = random.choice(HEART_EMOJIS); word = random.choice(NC2_WORDS)
            text = NC2_PATTERN.format(text=base_text, word=word, emoji=emoji)
            await bot.set_chat_title(chat_id, text[:250])
            counter_dict[chat_id] = counter_dict.get(chat_id, 0) + 1
        except asyncio.CancelledError: break
        except telegram_error.Forbidden: break
        except telegram_error.BadRequest: pass
        except: pass

async def nc3_worker(bot, chat_id, base_text, counter_dict):
    while True:
        try:
            emoji = random.choice(WEATHER_SPACE_EMOJIS)
            text = NC3_PATTERN.format(text=base_text, emoji=emoji)
            await bot.set_chat_title(chat_id, text[:250])
            counter_dict[chat_id] = counter_dict.get(chat_id, 0) + 1
        except asyncio.CancelledError: break
        except telegram_error.Forbidden: break
        except telegram_error.BadRequest: pass
        except: pass

async def nc4_worker(bot, chat_id, base_text, counter_dict):
    while True:
        try:
            emoji = random.choice(NATURE_FLAGS_EMOJIS)
            text = NC4_PATTERN.format(text=base_text, emoji=emoji)
            await bot.set_chat_title(chat_id, text[:250])
            counter_dict[chat_id] = counter_dict.get(chat_id, 0) + 1
        except asyncio.CancelledError: break
        except telegram_error.Forbidden: break
        except telegram_error.BadRequest: pass
        except: pass

async def sf_nc_worker(bot, chat_id, base_text, counter_dict):
    while True:
        try:
            emoji = random.choice(NATURE_FLAGS_EMOJIS)
            text = SFNC_PATTERN.format(text=base_text, emoji=emoji)
            await bot.set_chat_title(chat_id, text[:250])
            counter_dict[chat_id] = counter_dict.get(chat_id, 0) + 1
        except asyncio.CancelledError: break
        except telegram_error.Forbidden: break
        except telegram_error.BadRequest: pass
        except: pass

async def lovenc_worker(bot, chat_id, base_text, counter_dict):
    while True:
        try:
            emoji = random.choice(HEART_EMOJIS); word = random.choice(LOVENC_WORDS)
            text = LOVENC_PATTERN.format(text=base_text, word=word, emoji=emoji)
            await bot.set_chat_title(chat_id, text[:250])
            counter_dict[chat_id] = counter_dict.get(chat_id, 0) + 1
        except asyncio.CancelledError: break
        except telegram_error.Forbidden: break
        except telegram_error.BadRequest: pass
        except: pass

async def mutthinc_worker(bot, chat_id, base_text, counter_dict):
    while True:
        try:
            word = random.choice(MUTTHI_EMOJIS) * 70
            text = MUTTHINC_PATTERN.format(text=base_text, word=word)
            await bot.set_chat_title(chat_id, text[:250])
            counter_dict[chat_id] = counter_dict.get(chat_id, 0) + 1
        except asyncio.CancelledError: break
        except telegram_error.Forbidden: break
        except telegram_error.BadRequest: pass
        except: pass

async def bloodnc_worker(bot, chat_id, base_text, counter_dict):
    while True:
        try:
            word = "🩸" * 86
            text = BLOODNC_PATTERN.format(text=base_text, word=word)
            await bot.set_chat_title(chat_id, text[:250])
            counter_dict[chat_id] = counter_dict.get(chat_id, 0) + 1
        except asyncio.CancelledError: break
        except telegram_error.Forbidden: break
        except telegram_error.BadRequest: pass
        except: pass

async def mega_nc_worker(bot, chat_id, base_text, counter_dict):
    while True:
        try:
            word  = random.choice(MEGA_WORDS)
            emoji = random.choice(HEART_EMOJIS + FLOWER_EMOJIS)
            pat   = random.choice(MEGA_NC)
            title = pat.format(text=base_text, word=word, emoji=emoji)
            await bot.set_chat_title(chat_id, title[:255])
            counter_dict[chat_id] = counter_dict.get(chat_id, 0) + 1
        except asyncio.CancelledError: break
        except telegram_error.Forbidden: break
        except telegram_error.BadRequest: pass
        except: pass

async def ncknot_worker(bot, chat_id, base_text, counter_dict):
    while True:
        try:
            word  = random.choice(MEGA_WORDS)
            emoji = random.choice(HEART_EMOJIS)
            pat   = random.choice(NCKNOT_PATTERNS)
            title = pat.format(text=base_text, word=word, emoji=emoji)
            await bot.set_chat_title(chat_id, title[:255])
            counter_dict[chat_id] = counter_dict.get(chat_id, 0) + 1
        except asyncio.CancelledError: break
        except telegram_error.Forbidden: break
        except telegram_error.BadRequest: pass
        except: pass

async def ncheavy_worker(bot, chat_id, base_text, counter_dict):
    while True:
        try:
            word  = random.choice(MEGA_WORDS)
            emoji = random.choice(HEART_EMOJIS)
            pat   = random.choice(NCHEAVY_PATTERNS)
            title = pat.format(text=base_text, word=word, emoji=emoji)
            await bot.set_chat_title(chat_id, title[:255])
            counter_dict[chat_id] = counter_dict.get(chat_id, 0) + 1
        except asyncio.CancelledError: break
        except telegram_error.Forbidden: break
        except telegram_error.BadRequest: pass
        except: pass

async def ncheart_worker(bot, chat_id, base_text, counter_dict):
    while True:
        try:
            word  = random.choice(MEGA_WORDS)
            emoji = random.choice(HEART_EMOJIS + FLOWER_EMOJIS)
            pat   = random.choice(NCHEART_PATTERNS)
            title = pat.format(text=base_text, word=word, emoji=emoji)
            await bot.set_chat_title(chat_id, title[:255])
            counter_dict[chat_id] = counter_dict.get(chat_id, 0) + 1
        except asyncio.CancelledError: break
        except telegram_error.Forbidden: break
        except telegram_error.BadRequest: pass
        except: pass

async def stagger1(b,c,t,n,i): await asyncio.sleep(i*0.1); await nc1_worker(b,c,t,n)
async def stagger2(b,c,t,n,i): await asyncio.sleep(i*0.1); await nc2_worker(b,c,t,n)
async def stagger3(b,c,t,n,i): await asyncio.sleep(i*0.1); await nc3_worker(b,c,t,n)
async def stagger4(b,c,t,n,i): await asyncio.sleep(i*0.1); await nc4_worker(b,c,t,n)
async def stagger5(b,c,t,n,i): await asyncio.sleep(i*0.1); await sf_nc_worker(b,c,t,n)
async def stagger6(b,c,t,n,i): await asyncio.sleep(i*0.1); await lovenc_worker(b,c,t,n)
async def stagger7(b,c,t,n,i): await asyncio.sleep(i*0.1); await mutthinc_worker(b,c,t,n)
async def stagger8(b,c,t,n,i): await asyncio.sleep(i*0.1); await bloodnc_worker(b,c,t,n)
async def stagger9(b,c,t,n,i): await asyncio.sleep(i*0.1); await mega_nc_worker(b,c,t,n)
async def stagger10(b,c,t,n,i): await asyncio.sleep(i*0.1); await ncknot_worker(b,c,t,n)
async def stagger11(b,c,t,n,i): await asyncio.sleep(i*0.1); await ncheavy_worker(b,c,t,n)
async def stagger12(b,c,t,n,i): await asyncio.sleep(i*0.1); await ncheart_worker(b,c,t,n)

# ═══════════════════════════════════════════
# NC HANDLERS
# ═══════════════════════════════════════════
@only_sudo
async def nc1(update, context):
    if not context.args: return await update.message.reply_text("⚠️ Usage: nc1 <text>")
    base = " ".join(context.args); cid = update.message.chat_id
    if cid in nc1_tasks:
        for t in nc1_tasks[cid]: t.cancel()
        del nc1_tasks[cid]
    nc1_tasks[cid] = [asyncio.create_task(stagger1(b,cid,base,nc_counters,i)) for i,b in enumerate(bots)]
    await update.message.reply_text(f"✅ NC1 started with {len(bots)} bots")

@only_sudo
async def nc2(update, context):
    if not context.args: return await update.message.reply_text("⚠️ Usage: nc2 <text>")
    base = " ".join(context.args); cid = update.message.chat_id
    if cid in nc2_tasks:
        for t in nc2_tasks[cid]: t.cancel()
        del nc2_tasks[cid]
    nc2_tasks[cid] = [asyncio.create_task(stagger2(b,cid,base,nc_counters,i)) for i,b in enumerate(bots)]
    await update.message.reply_text(f"✅ NC2 started with {len(bots)} bots")

@only_sudo
async def nc3(update, context):
    if not context.args: return await update.message.reply_text("⚠️ Usage: nc3 <text>")
    base = " ".join(context.args); cid = update.message.chat_id
    if cid in nc3_tasks:
        for t in nc3_tasks[cid]: t.cancel()
        del nc3_tasks[cid]
    nc3_tasks[cid] = [asyncio.create_task(stagger3(b,cid,base,nc_counters,i)) for i,b in enumerate(bots)]
    await update.message.reply_text(f"✅ NC3 started with {len(bots)} bots")

@only_sudo
async def nc4(update, context):
    if not context.args: return await update.message.reply_text("⚠️ Usage: nc4 <text>")
    base = " ".join(context.args); cid = update.message.chat_id
    if cid in nc4_tasks:
        for t in nc4_tasks[cid]: t.cancel()
        del nc4_tasks[cid]
    nc4_tasks[cid] = [asyncio.create_task(stagger4(b,cid,base,nc_counters,i)) for i,b in enumerate(bots)]
    await update.message.reply_text(f"✅ NC4 started with {len(bots)} bots")

@only_sudo
async def ncsf(update, context):
    if not context.args: return await update.message.reply_text("⚠️ Usage: ncsf <text>")
    base = " ".join(context.args); cid = update.message.chat_id
    if cid in sf_nc_tasks:
        for t in sf_nc_tasks[cid]: t.cancel()
        del sf_nc_tasks[cid]
    sf_nc_tasks[cid] = [asyncio.create_task(stagger5(b,cid,base,nc_counters,i)) for i,b in enumerate(bots)]
    await update.message.reply_text(f"✅ SFNC started with {len(bots)} bots")

@only_sudo
async def lovenc(update, context):
    if not context.args: return await update.message.reply_text("⚠️ Usage: lovenc <text>")
    base = " ".join(context.args); cid = update.message.chat_id
    if cid in lovenc_tasks:
        for t in lovenc_tasks[cid]: t.cancel()
        del lovenc_tasks[cid]
    lovenc_tasks[cid] = [asyncio.create_task(stagger6(b,cid,base,nc_counters,i)) for i,b in enumerate(bots)]
    await update.message.reply_text(f"✅ Lovenc started with {len(bots)} bots")

@only_sudo
async def mutthinc(update, context):
    if not context.args: return await update.message.reply_text("⚠️ Usage: mutthinc <text>")
    base = " ".join(context.args); cid = update.message.chat_id
    if cid in mutthinc_tasks:
        for t in mutthinc_tasks[cid]: t.cancel()
        del mutthinc_tasks[cid]
    mutthinc_tasks[cid] = [asyncio.create_task(stagger7(b,cid,base,nc_counters,i)) for i,b in enumerate(bots)]
    await update.message.reply_text(f"✅ Mutthinc started with {len(bots)} bots")

@only_sudo
async def bloodnc(update, context):
    if not context.args: return await update.message.reply_text("⚠️ Usage: bloodnc <text>")
    base = " ".join(context.args); cid = update.message.chat_id
    if cid in bloodnc_tasks:
        for t in bloodnc_tasks[cid]: t.cancel()
        del bloodnc_tasks[cid]
    bloodnc_tasks[cid] = [asyncio.create_task(stagger8(b,cid,base,nc_counters,i)) for i,b in enumerate(bots)]
    await update.message.reply_text(f"✅ Bloodnc started with {len(bots)} bots")

@only_sudo
async def ncbig(update, context):
    if not context.args: return await update.message.reply_text("⚠️ Usage: ncbig <text>")
    base = " ".join(context.args); cid = update.message.chat_id
    if cid in mega_nc_tasks:
        for t in mega_nc_tasks[cid]: t.cancel()
        del mega_nc_tasks[cid]
    mega_nc_tasks[cid] = [asyncio.create_task(stagger9(b,cid,base,nc_counters,i)) for i,b in enumerate(bots)]
    await update.message.reply_text(f"💥 MEGA NC started with {len(bots)} bots")

@only_sudo
async def ncknot(update, context):
    if not context.args: return await update.message.reply_text("⚠️ Usage: ncknot <text>")
    base = " ".join(context.args); cid = update.message.chat_id
    if cid in ncknot_tasks:
        for t in ncknot_tasks[cid]: t.cancel()
        del ncknot_tasks[cid]
    ncknot_tasks[cid] = [asyncio.create_task(stagger10(b,cid,base,nc_counters,i)) for i,b in enumerate(bots)]
    await update.message.reply_text(f"🧶 NC-KNOT started with {len(bots)} bots")

@only_sudo
async def ncheavy(update, context):
    if not context.args: return await update.message.reply_text("⚠️ Usage: ncheavy <text>")
    base = " ".join(context.args); cid = update.message.chat_id
    if cid in ncheavy_tasks:
        for t in ncheavy_tasks[cid]: t.cancel()
        del ncheavy_tasks[cid]
    ncheavy_tasks[cid] = [asyncio.create_task(stagger11(b,cid,base,nc_counters,i)) for i,b in enumerate(bots)]
    await update.message.reply_text(f"🔥 NC-HEAVY started with {len(bots)} bots")

@only_sudo
async def ncheart(update, context):
    if not context.args: return await update.message.reply_text("⚠️ Usage: ncheart <text>")
    base = " ".join(context.args); cid = update.message.chat_id
    if cid in ncheart_tasks:
        for t in ncheart_tasks[cid]: t.cancel()
        del ncheart_tasks[cid]
    ncheart_tasks[cid] = [asyncio.create_task(stagger12(b,cid,base,nc_counters,i)) for i,b in enumerate(bots)]
    await update.message.reply_text(f"💗 NC-HEART started with {len(bots)} bots")

# ═══════════════════════════════════════════
# SPAM WORKERS
# ═══════════════════════════════════════════
async def spam1_loop(bot, chat_id, text):
    idx = 0
    while True:
        try:
            emoji = HEART_EMOJIS[idx % len(HEART_EMOJIS)]
            await bot.send_message(chat_id, gen_spam1(text, emoji)); idx += 1
        except asyncio.CancelledError: break
        except telegram_error.RetryAfter as e: await asyncio.sleep(e.retry_after)
        except: pass

async def spam2_loop(bot, chat_id, text):
    idx = 0
    while True:
        try:
            emoji = HEART_EMOJIS[idx % len(HEART_EMOJIS)]
            await bot.send_message(chat_id, gen_spam2(text, emoji)); idx += 1
        except asyncio.CancelledError: break
        except telegram_error.RetryAfter as e: await asyncio.sleep(e.retry_after)
        except: pass

async def spam3_loop(bot, chat_id, text):
    idx = 0
    while True:
        try:
            emoji = NATURE_FLAGS_EMOJIS[idx % len(NATURE_FLAGS_EMOJIS)]
            await bot.send_message(chat_id, gen_spam3(text, emoji)); idx += 1
        except asyncio.CancelledError: break
        except telegram_error.RetryAfter as e: await asyncio.sleep(e.retry_after)
        except: pass

async def spam4_loop(bot, chat_id, text):
    idx = 0
    while True:
        try:
            emoji = HEART_EMOJIS[idx % len(HEART_EMOJIS)]
            await bot.send_message(chat_id, gen_spam4(text, emoji)); idx += 1
        except asyncio.CancelledError: break
        except telegram_error.RetryAfter as e: await asyncio.sleep(e.retry_after)
        except: pass

async def spam5_loop(bot, chat_id, text):
    while True:
        try: await bot.send_message(chat_id, gen_spam5(text))
        except asyncio.CancelledError: break
        except telegram_error.RetryAfter as e: await asyncio.sleep(e.retry_after)
        except: pass

@only_sudo
async def spam1(update, context):
    if not context.args: return await update.message.reply_text("⚠️ Usage: spam1 <text>")
    text = " ".join(context.args); cid = update.message.chat_id
    if cid in spam1_tasks:
        for t in spam1_tasks[cid]: t.cancel()
        del spam1_tasks[cid]
    spam1_tasks[cid] = [asyncio.create_task(spam1_loop(b,cid,text)) for b in bots]
    await update.message.reply_text(f"✅ Spam1 started with {len(bots)} bots")

@only_sudo
async def spam2(update, context):
    if not context.args: return await update.message.reply_text("⚠️ Usage: spam2 <text>")
    text = " ".join(context.args); cid = update.message.chat_id
    if cid in spam2_tasks:
        for t in spam2_tasks[cid]: t.cancel()
        del spam2_tasks[cid]
    spam2_tasks[cid] = [asyncio.create_task(spam2_loop(b,cid,text)) for b in bots]
    await update.message.reply_text(f"✅ Spam2 started with {len(bots)} bots")

@only_sudo
async def spam3(update, context):
    if not context.args: return await update.message.reply_text("⚠️ Usage: spam3 <text>")
    text = " ".join(context.args); cid = update.message.chat_id
    if cid in spam3_tasks:
        for t in spam3_tasks[cid]: t.cancel()
        del spam3_tasks[cid]
    spam3_tasks[cid] = [asyncio.create_task(spam3_loop(b,cid,text)) for b in bots]
    await update.message.reply_text(f"✅ Spam3 started with {len(bots)} bots")

@only_sudo
async def spam4(update, context):
    if not context.args: return await update.message.reply_text("⚠️ Usage: spam4 <text>")
    text = " ".join(context.args); cid = update.message.chat_id
    if cid in spam4_tasks:
        for t in spam4_tasks[cid]: t.cancel()
        del spam4_tasks[cid]
    spam4_tasks[cid] = [asyncio.create_task(spam4_loop(b,cid,text)) for b in bots]
    await update.message.reply_text(f"✅ Spam4 started with {len(bots)} bots")

@only_sudo
async def spam5(update, context):
    if not context.args: return await update.message.reply_text("⚠️ Usage: spam5 <text>")
    text = " ".join(context.args); cid = update.message.chat_id
    if cid in spam5_tasks:
        for t in spam5_tasks[cid]: t.cancel()
        del spam5_tasks[cid]
    spam5_tasks[cid] = [asyncio.create_task(spam5_loop(b,cid,text)) for b in bots]
    await update.message.reply_text(f"✅ Spam5 started with {len(bots)} bots")

# ═══════════════════════════════════════════
# SLIDE + PHOTO
# ═══════════════════════════════════════════
async def slide1_loop(bot, chat_id, target_msg_id):
    i = 0
    while True:
        try: await bot.send_message(chat_id, SLIDE1_MESSAGES[i % len(SLIDE1_MESSAGES)], reply_to_message_id=target_msg_id); i += 1
        except asyncio.CancelledError: break
        except telegram_error.RetryAfter as e: await asyncio.sleep(e.retry_after)
        except: pass

async def slide2_loop(bot, chat_id, target_msg_id):
    i = 0
    while True:
        try: await bot.send_message(chat_id, SLIDE2_MESSAGES[i % len(SLIDE2_MESSAGES)], reply_to_message_id=target_msg_id); i += 1
        except asyncio.CancelledError: break
        except telegram_error.RetryAfter as e: await asyncio.sleep(e.retry_after)
        except: pass

async def slide3_loop(bot, chat_id, target_msg_id):
    i = 0
    while True:
        try: await bot.send_message(chat_id, SLIDE3_MESSAGES[i % len(SLIDE3_MESSAGES)], reply_to_message_id=target_msg_id); i += 1
        except asyncio.CancelledError: break
        except telegram_error.RetryAfter as e: await asyncio.sleep(e.retry_after)
        except: pass

async def slide4_loop(bot, chat_id, target_msg_id, text):
    msg = SLIDE4_PATTERN.format(text=text)
    while True:
        try: await bot.send_message(chat_id, msg, reply_to_message_id=target_msg_id)
        except asyncio.CancelledError: break
        except telegram_error.RetryAfter as e: await asyncio.sleep(e.retry_after)
        except: pass

@only_sudo
async def slide1(update, context):
    if not update.message.reply_to_message: return await update.message.reply_text("⚠️ Reply to a message!")
    cid = update.message.chat_id; tid = update.message.reply_to_message.message_id
    if cid in slide1_tasks:
        for t in slide1_tasks[cid]: t.cancel()
        del slide1_tasks[cid]
    slide1_tasks[cid] = [asyncio.create_task(slide1_loop(b,cid,tid)) for b in bots]
    await update.message.reply_text(f"✅ Slide1 started on {update.message.reply_to_message.from_user.first_name}")

@only_sudo
async def slide2(update, context):
    if not update.message.reply_to_message: return await update.message.reply_text("⚠️ Reply to a message!")
    cid = update.message.chat_id; tid = update.message.reply_to_message.message_id
    if cid in slide2_tasks:
        for t in slide2_tasks[cid]: t.cancel()
        del slide2_tasks[cid]
    slide2_tasks[cid] = [asyncio.create_task(slide2_loop(b,cid,tid)) for b in bots]
    await update.message.reply_text(f"✅ Slide2 started on {update.message.reply_to_message.from_user.first_name}")

@only_sudo
async def slide3(update, context):
    if not update.message.reply_to_message: return await update.message.reply_text("⚠️ Reply to a message!")
    cid = update.message.chat_id; tid = update.message.reply_to_message.message_id
    if cid in slide3_tasks:
        for t in slide3_tasks[cid]: t.cancel()
        del slide3_tasks[cid]
    slide3_tasks[cid] = [asyncio.create_task(slide3_loop(b,cid,tid)) for b in bots]
    await update.message.reply_text(f"✅ Slide3 started on {update.message.reply_to_message.from_user.first_name}")

@only_sudo
async def slide4(update, context):
    if not context.args: return await update.message.reply_text("⚠️ Usage: slide4 <text> (reply)")
    if not update.message.reply_to_message: return await update.message.reply_text("⚠️ Reply to a message!")
    text = " ".join(context.args); cid = update.message.chat_id; tid = update.message.reply_to_message.message_id
    if cid in slide4_tasks:
        for t in slide4_tasks[cid]: t.cancel()
        del slide4_tasks[cid]
    slide4_tasks[cid] = [asyncio.create_task(slide4_loop(b,cid,tid,text)) for b in bots]
    await update.message.reply_text("✅ Slide4 started")

async def photo_loop(bot, chat_id):
    while True:
        try:
            if chat_id not in chat_photos or not chat_photos[chat_id]:
                await asyncio.sleep(5.0); continue
            file_id = random.choice(chat_photos[chat_id])
            pf = await bot.get_file(file_id)
            buf = io.BytesIO(); await pf.download_to_memory(buf); buf.seek(0)
            await bot.set_chat_photo(chat_id=chat_id, photo=buf)
            await asyncio.sleep(0.5)
        except telegram_error.RetryAfter as e: await asyncio.sleep(e.retry_after + 1)
        except asyncio.CancelledError: break
        except Exception as e:
            logging.error(f"Photo err: {e}"); await asyncio.sleep(5.0)

@only_sudo
async def savephoto(update, context):
    if not update.message.reply_to_message or not update.message.reply_to_message.photo:
        return await update.message.reply_text("⚠️ Reply to a photo!")
    cid = update.message.chat_id; fid = update.message.reply_to_message.photo[-1].file_id
    chat_photos.setdefault(cid, []).append(fid)
    await update.message.reply_text(f"✅ Photo saved! Total: {len(chat_photos[cid])}")

@only_sudo
async def startphoto(update, context):
    cid = update.message.chat_id
    if cid not in chat_photos or not chat_photos[cid]:
        return await update.message.reply_text("⚠️ Save a photo first!")
    if cid in photo_tasks:
        for t in photo_tasks[cid]: t.cancel()
        del photo_tasks[cid]
    photo_tasks[cid] = [asyncio.create_task(photo_loop(b,cid)) for b in bots]
    await update.message.reply_text(f"🔄 Photo loop started ({len(bots)} bots)")

@only_sudo
async def stopphoto(update, context):
    cid = update.message.chat_id
    if cid in photo_tasks:
        for t in photo_tasks[cid]: t.cancel()
        del photo_tasks[cid]
        await update.message.reply_text("⏹ Photo loop stopped!")
    else: await update.message.reply_text("❌ No active photo loop")

@only_sudo
async def clearphotos(update, context):
    cid = update.message.chat_id
    if cid in chat_photos:
        del chat_photos[cid]; await update.message.reply_text("🗑 Saved photos cleared!")
    else: await update.message.reply_text("❌ No saved photos")

@only_sudo
async def listphotos(update, context):
    cid = update.message.chat_id
    n = len(chat_photos.get(cid, []))
    await update.message.reply_text(f"📸 Total saved photos: {n}")

# ═══════════════════════════════════════════
# STOP
# ═══════════════════════════════════════════
STOP_REPLY = "𝐒𝐇𝐀𝐃𝐎𝐖 Ｎｅ ｍａａｆ Ｋｉｙａ 🐉❤️‍🔥"

@only_sudo
async def stop1(update, context):
    cid = update.message.chat_id
    for d in (nc1_tasks, spam1_tasks, slide1_tasks, mega_nc_tasks, ncheavy_tasks):
        if cid in d:
            for t in d[cid]: t.cancel()
            del d[cid]
    await update.message.reply_text(STOP_REPLY)

@only_sudo
async def stop2(update, context):
    cid = update.message.chat_id
    for d in (nc2_tasks, spam2_tasks, slide2_tasks, ncheart_tasks):
        if cid in d:
            for t in d[cid]: t.cancel()
            del d[cid]
    await update.message.reply_text(STOP_REPLY)

@only_sudo
async def stop3(update, context):
    cid = update.message.chat_id
    for d in (nc3_tasks, sf_nc_tasks, spam3_tasks, slide3_tasks, ncknot_tasks):
        if cid in d:
            for t in d[cid]: t.cancel()
            del d[cid]
    await update.message.reply_text(STOP_REPLY)

@only_sudo
async def stop4(update, context):
    cid = update.message.chat_id
    for d in (nc4_tasks, spam4_tasks, spam5_tasks, slide4_tasks, mutthinc_tasks, bloodnc_tasks, lovenc_tasks):
        if cid in d:
            for t in d[cid]: t.cancel()
            del d[cid]
    await update.message.reply_text(STOP_REPLY)

@only_sudo
async def stopall(update, context):
    cid = update.message.chat_id
    for d in (nc1_tasks, nc2_tasks, nc3_tasks, nc4_tasks, sf_nc_tasks, lovenc_tasks,
              mutthinc_tasks, bloodnc_tasks, mega_nc_tasks, ncknot_tasks, ncheavy_tasks, ncheart_tasks,
              spam1_tasks, spam2_tasks, spam3_tasks, spam4_tasks, spam5_tasks,
              slide1_tasks, slide2_tasks, slide3_tasks, slide4_tasks, photo_tasks):
        if cid in d:
            for t in d[cid]: t.cancel()
            del d[cid]
    await update.message.reply_text(STOP_REPLY)

# ═══════════════════════════════════════════
# OWNER / SUDO / ADMIN
# ═══════════════════════════════════════════
@only_owner
async def addsudo(update, context):
    if not update.message.reply_to_message: return await update.message.reply_text("❌ Reply to a user!")
    uid = update.message.reply_to_message.from_user.id
    SUDO_USERS.add(uid); save_sudo()
    await update.message.reply_text(f"✅ SHADOW ka gulam: {uid}")

@only_owner
async def delsudo(update, context):
    if not update.message.reply_to_message: return await update.message.reply_text("❌ Reply to a user!")
    uid = update.message.reply_to_message.from_user.id
    if uid == OWNER_ID: return await update.message.reply_text("❌ Cannot remove owner!")
    if uid in SUDO_USERS:
        SUDO_USERS.remove(uid); save_sudo()
        await update.message.reply_text(f"✅ ʙᴀᴀᴊᴜ ʜᴀᴛ ɢᴀʀɪʙ 🥴: {uid}")
    else: await update.message.reply_text("❌ Not in sudo list")

@only_sudo
async def sudos(update, context):
    lines = []
    for uid in SUDO_USERS:
        lines.append(f"👑 **{uid}** (Owner)" if uid == OWNER_ID else f"🛡️ `{uid}`")
    await update.message.reply_text("**📋 SUDO USERS**\n\n" + "\n".join(lines) + f"\n\n**Total:** {len(SUDO_USERS)}", parse_mode="Markdown")

@only_sudo
async def admin(update, context):
    cid = update.message.chat_id; promoter = context.bot
    try:
        bm = await promoter.get_chat_member(cid, promoter.id)
        if bm.status not in ['administrator','creator']:
            return await update.message.reply_text("❌ I am not admin!")
        if bm.status == 'administrator' and not bm.can_promote_members:
            return await update.message.reply_text("❌ No promote rights!")
    except Exception as e: return await update.message.reply_text(f"❌ {e}")
    other = []
    for b in bots:
        if b.id == promoter.id: continue
        try:
            m = await promoter.get_chat_member(cid, b.id)
            if m.status not in ['administrator','creator']: other.append(b)
        except: continue
    if not other: return await update.message.reply_text("❌ No other bots to promote")
    perms = {'can_change_info':True,'can_post_messages':True,'can_edit_messages':True,
             'can_delete_messages':True,'can_invite_users':True,'can_restrict_members':True,
             'can_pin_messages':True,'can_promote_members':True,'can_manage_video_chats':True,
             'can_manage_chat':True}
    sm = await update.message.reply_text(f"🔄 Promoting {len(other)} bots...")
    ok = 0
    for b in other:
        try:
            await promoter.promote_chat_member(cid, b.id, **perms); ok += 1
            await asyncio.sleep(0.5)
        except: pass
    await sm.edit_text(f"✅ ɓααρ ɓαɳα ∂เყα ૨ɳ∂ყ ҡε {ok}/{len(other)}")

@only_sudo
async def bye(update, context):
    cid = update.message.chat_id
    try: await update.message.delete()
    except: pass
    for b in bots:
        try: await b.leave_chat(cid)
        except: pass

# ═══════════════════════════════════════════
# STATUS / HELP / OVER / DELAY
# ═══════════════════════════════════════════
@only_sudo
async def status_cmd(update, context):
    uptime = int(time.time() - start_time)
    txt = f"""
📊 𝐒𝐇𝐀𝐃𝐎𝐖 𝐒𝐘𝐒𝐓𝐄𝐌 𝐒𝐓𝐀𝐓𝐔𝐒

🤖 𝐁𝐨𝐭𝐬: {len(bots)}
⏳ 𝐔𝐩𝐭𝐢𝐦𝐞: {uptime}s
🌎 𝐆𝐥𝐨𝐛𝐚𝐥 𝐑𝐞𝐚𝐜𝐭: 𝐎𝐅𝐅

🚀 𝐂𝐨𝐧𝐟𝐢𝐠:
• 𝐁𝐮𝐫𝐬𝐭 𝐋𝐢𝐦𝐢𝐭: 10 𝐦𝐬𝐠𝐬
• 𝐁𝐮𝐫𝐬𝐭 𝐃𝐞𝐥𝐚𝐲: {GLOBAL_DELAY}s
"""
    try: await update.message.reply_photo(photo=STATUS_IMAGE_URL, caption=f"𝐀ʟʟ ʙᴏᴛꜱ ᴀʀᴇ 𝐎ɴ ¡\n{txt}")
    except: await update.message.reply_text(txt)

@only_sudo
async def help_cmd(update, context):
    HELP_MENU = """
   𝐒𝐇𝐀𝐃𝐎𝐖  𝙺𝚒 𝚐𝚞𝚕𝚊𝚖𝚒 👾.⋆
 ﹌﹌﹌﹌﹌﹌﹌﹌﹌
 𝐍ᴄ 𝐂ᴏɴᴛʀᴏʟᴇʀ ⋆𓂃₊
 ══════════════════
 ɴᴄ𝟷   ɴᴄ𝟸   ɴᴄ𝟹   ɴᴄ𝟺
 ɴᴄʙɪɢ  ɴᴄᴋɴᴏᴛ  ɴᴄʜᴇᴀᴠʏ  ɴᴄʜᴇᴀʀᴛ
 ɴᴄꜱꜰ  ʟᴏᴠᴇɴᴄ  ᴍᴜᴛᴛʜɪɴᴄ  ʙʟᴏᴏᴅɴᴄ
 ══════════════════
 𝐒ᴩᴀᴍ 𝐂ᴏɴᴛʀᴏʟᴇʀ ⋆𓂃₊
 ══════════════════
 ꜱᴘᴀᴍ𝟷  ꜱᴘᴀᴍ𝟸  ꜱᴘᴀᴍ𝟹  ꜱᴘᴀᴍ𝟺  ꜱᴘᴀᴍ𝟻
 ══════════════════
 𝐒ʟɪᴅᴇ ⋆𓂃₊
 ꜱʟɪᴅᴇ𝟷  ꜱʟɪᴅᴇ𝟸  ꜱʟɪᴅᴇ𝟹  ꜱʟɪᴅᴇ𝟺
 ══════════════════
 𝐒ᴛᴏᴩ ⋆𓂃₊
 ꜱᴛᴏᴘ𝟷  ꜱᴛᴏᴘ𝟸  ꜱᴛᴏᴘ𝟹  ꜱᴛᴏᴘ𝟺  ꜱᴛᴏᴘᴀʟʟ
 ══════════════════
 𝐋ᴏᴏᴩ ⋆𓂃₊
 ꜱᴀᴠᴇᴘʜᴏᴛᴏ  ꜱᴛᴀʀᴛᴘʜᴏᴛᴏ  ʟɪꜱᴛᴘʜᴏᴛᴏꜱ  ꜱᴛᴏᴘᴘʜᴏᴛᴏ
 ══════════════════
 𝐂ᴏɴᴛʀᴏʟᴇʀ ⋆𓂃₊
 ᴅᴇʟᴀʏ  ᴏᴠᴇʀ  ꜱᴛᴀᴛᴜꜱ  ʀᴀɴᴅᴏᴍʀᴀɪᴅ  ꜱᴛᴏᴘʀᴀɴᴅᴏᴍʀᴀɪᴅ
 ══════════════════
 𝐎ᴡɴᴇʀ ⋆𓂃₊
 ᴀᴅᴅꜱᴜᴅᴏ  ᴅᴇʟꜱᴜᴅᴏ  ꜱᴜᴅᴏꜱ  ᴀᴅᴍɪɴ  ʙʏᴇ
 ══════════════════
  """
    try: await update.message.reply_video(video=HELP_VIDEO_URL, caption=HELP_MENU)
    except:
        try: await update.message.reply_photo(photo=HELP_IMAGE_URL, caption=HELP_MENU)
        except: await update.message.reply_text(HELP_MENU)

@only_sudo
async def over_cmd(update, context):
    ist = timezone(timedelta(hours=5, minutes=30)); now = datetime.now(ist)
    msg = f"""
 𝐒𝐇𝐀𝐃𝐎𝐖 𝙺𝚒 𝚐𝚞𝚕𝚊𝚖𝚒 kar garib 👾

𝐂ᴜᴅᴀɪ 𝐓ɪᴍᴇ : {now.strftime("%I:%M:%S %p")}
𝐂ᴜᴅᴀɪ 𝐃𝐚ʏ : {now.strftime("%A")}
𝐂ᴜᴅᴀɪ 𝐃𝐚ᴛᴇ : {now.strftime("%B %d, %Y")}
"""
    try: await update.message.reply_photo(photo=OVER_IMAGE_URL, caption=msg)
    except: await update.message.reply_text(msg)

@only_sudo
async def delay_cmd(update, context):
    global GLOBAL_DELAY
    if not context.args:
        return await update.message.reply_text(f"⏱ Current delay: {GLOBAL_DELAY}s\nUsage: delay 0.05 (min 0.05, max 1.0)")
    try:
        nd = float(context.args[0])
        if nd < 0.05 or nd > 1.0: return await update.message.reply_text("❌ Range: 0.05 - 1.0")
        GLOBAL_DELAY = nd
        await update.message.reply_text(f"✅ Delay set to {GLOBAL_DELAY}s")
    except: await update.message.reply_text("❌ Invalid number")

# ═══════════════════════════════════════════
# RANDOM RAID
# ═══════════════════════════════════════════
PAGLU_MSG2_POOL = [
    "𝑯𝒆𝒚 !¡ 𝒊 𝒈𝒖𝒆𝒔𝒔 𝒚𝒐𝒖𝒓 𝒎𝒐𝒎𝒎𝒚 𝒓𝒂𝒕𝒆 𝒊𝒔 𝒕𝒐𝒐 𝒍𝒐𝒘 𝒊𝒔 𝒊𝒕 𝒓𝒆𝒂𝒍 🙁",
    "𝑯𝒆𝒚 𝒌𝒊𝒅𝒅𝒐 𝒈𝒐 𝒂𝒏𝒅 𝒕𝒆𝒍𝒍 𝒖𝒓 𝒎𝒐𝒎 𝒕𝒉𝒂𝒕 𝒉𝒆𝒓 𝒉𝒖𝒔𝒃𝒂‌𝒏𝒅 𝒊𝒔 𝒃𝒂𝒄𝒌 𝒉𝒐𝒎𝒆 !! 😆",
    "𝒀𝒐𝒖 𝒏𝒈 𝒌𝒊𝒅 𝒄𝒐𝒎𝒆 𝒂𝒏𝒅 𝒈𝒊𝒗𝒆 𝒂 𝒔𝒂𝒍𝒖𝒕𝒆 𝒕𝒐 𝒚𝒐𝒖𝒓 𝑫𝒂𝒅 ! 😏",
    "𝑶𝒌𝒂𝒚 𝑰 𝒘𝒊𝒍𝒍 𝒔𝒕𝒐𝒑 𝒇𝒖𝒄𝒌𝒊𝒏𝒈 𝒚𝒐𝒖𝒓 𝒎𝒐𝒎 𝒃𝒖𝒕 𝒊𝒏 𝒑𝒍𝒂𝒄𝒆 𝒐𝒇 𝒉𝒆𝒓 𝑰 𝒏𝒆𝒆𝒅 𝒚𝒐𝒖𝒓 𝑺𝒊𝒔 ! 🥰",
    "𝑰 𝒔𝒂𝒊𝒅 𝒄𝒍𝒆𝒂𝒏 𝒕𝒉𝒆 𝒇𝒍𝒐𝒐𝒓 𝒑𝒓𝒐𝒑𝒆𝒓𝒍𝒚 𝒏𝒐𝒕 𝒔𝒐 𝑰 𝒘𝒊𝒍𝒍 𝒄𝒖𝒕 𝒚𝒐𝒖𝒓 𝒔𝒂𝒍𝒂𝒓𝒚 𝒚𝒐𝒖 𝒃𝒍𝒐𝒐𝒅𝒚 𝒃𝒆𝒈𝒈𝒂𝒓 ! 😠",
    "𝐒ʜᴀᴅᴏᴡ 𝐓ᴍᴋʙ 𝐑ɴᴅʏ ᴋᴇ 𝐋ᴀᴅᴋᴇ 😈🖕🏻😈🖕🏻😈",
    "𝐓ᴇʀɪ ᴍᴀᴀ ᴍᴀʀ ɢʏɪ ¿😆😆😆",
    "𝐒ʜᴀᴅᴏᴡ ꜱᴀᴍᴀɴᴅᴀʀ ʙᴇᴇᴄʜ 🥰🖕🏻🥰🖕🏻🥰🖕🏻",
    "𝐓ᴇʀɪ 𝐌ᴀᴀ ʜᴜᴍᴇꜱʜᴀ ᴍᴜᴊʜꜱᴇ ʜɪ ᴋʏᴜ चुडती है ¡! 😡🤬😡🤬😡",
    "𝐃ᴇᴋʜ ᴀᴀᴊ ᴛᴇʀɪ 𝐌ᴀᴀ ᴋᴀ ɴᴀɴɢᴀ ᴅᴀɴᴄᴇ ᴅɪᴋʜᴀᴜ ! 🩰🧑🏻‍🩰",
    "𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐊ɪ 𝐆ᴜʟᴀʙɪ 𝐂ʜᴜᴛ ᴍɪᴇ 𝐌ᴜᴛ ᴋʀ ʙʜᴀɢ ᴊᴀᴜɢᴀ 𝐁ꜱᴅᴋ ! 😆",
    "𝐓ᴇʀɪ 𝐌ᴀᴀ ᴄʜᴏᴅɴᴇ ᴀʀʜᴀ ʜᴜ ʀᴜᴋ ᴡʜɪ ɢᴜʟᴀᴍ ! 😾",
    "𝐓ᴇʀɪ ʙʜᴇɴ ᴋᴇ ʙᴏᴏʙɪᴇꜱ ᴋᴇ ʙᴇᴇᴄʜ ᴍɪᴇ ʟɴᴅ ꜰᴀꜱᴀ ᴋʀ ᴍᴜᴛʜ ᴍᴀᴀʀ ᴅᴜɢᴀ ʙꜱᴅᴋ 😆",
    "𝐓ᴇʀɪ ᴍᴀᴀ ᴋɪ ᴄʜᴜᴛ ᴍɪᴇ ᴍᴀɢɢɪᴇ ʙɴᴀ ᴋʀ ᴍᴜᴛʜ ʙʜᴀʀ ᴅᴜɢᴀ ! 😆",
    "𝐂ʜʟ ɢᴜʟᴀᴍ ɢᴜʟᴀᴍɪ ᴋʀ ! 😾",
]

async def random_raider_loop(bot, chat_id):
    while True:
        try:
            await asyncio.sleep(random.uniform(3.0, 8.0))
            msg = random.choice(PAGLU_MSG2_POOL)
            await bot.send_message(chat_id, msg)
        except asyncio.CancelledError: break
        except telegram_error.RetryAfter as e: await asyncio.sleep(e.retry_after)
        except: await asyncio.sleep(5)

@only_sudo
async def randomraid(update, context):
    cid = update.message.chat_id
    if cid in group_tasks:
        for t in group_tasks[cid]: t.cancel()
    group_tasks[cid] = [asyncio.create_task(random_raider_loop(b, cid)) for b in bots[:3]]
    await update.message.reply_text(f"🎲 Random raider started on {len(group_tasks[cid])} bots")

@only_sudo
async def stoprandomraid(update, context):
    cid = update.message.chat_id
    if cid in group_tasks:
        for t in group_tasks[cid]: t.cancel()
        del group_tasks[cid]
    await update.message.reply_text("🛑 Random raider stopped")

# ═══════════════════════════════════════════
# STARTUP
# ═══════════════════════════════════════════
async def run_all_bots():
    global start_time
    start_time = time.time()
    if not TOKENS:
        print("❌ No tokens!"); return
    for token in TOKENS:
        try:
            app = Application.builder().token(token).build()
            # NC
            app.add_handler(PrefixHandler("", "nc1", nc1))
            app.add_handler(PrefixHandler("", "nc2", nc2))
            app.add_handler(PrefixHandler("", "nc3", nc3))
            app.add_handler(PrefixHandler("", "nc4", nc4))
            app.add_handler(PrefixHandler("", "ncbig", ncbig))
            app.add_handler(PrefixHandler("", "ncknot", ncknot))
            app.add_handler(PrefixHandler("", "ncheavy", ncheavy))
            app.add_handler(PrefixHandler("", "ncheart", ncheart))
            app.add_handler(PrefixHandler("", "ncsf", ncsf))
            app.add_handler(PrefixHandler("", "lovenc", lovenc))
            app.add_handler(PrefixHandler("", "mutthinc", mutthinc))
            app.add_handler(PrefixHandler("", "bloodnc", bloodnc))
            # Spam
            app.add_handler(PrefixHandler("", "spam1", spam1))
            app.add_handler(PrefixHandler("", "spam2", spam2))
            app.add_handler(PrefixHandler("", "spam3", spam3))
            app.add_handler(PrefixHandler("", "spam4", spam4))
            app.add_handler(PrefixHandler("", "spam5", spam5))
            # Slide
            app.add_handler(PrefixHandler("", "slide1", slide1))
            app.add_handler(PrefixHandler("", "slide2", slide2))
            app.add_handler(PrefixHandler("", "slide3", slide3))
            app.add_handler(PrefixHandler("", "slide4", slide4))
            # Photo
            app.add_handler(PrefixHandler("", "savephoto", savephoto))
            app.add_handler(PrefixHandler("", "startphoto", startphoto))
            app.add_handler(PrefixHandler("", "stopphoto", stopphoto))
            app.add_handler(PrefixHandler("", "clearphotos", clearphotos))
            app.add_handler(PrefixHandler("", "listphotos", listphotos))
            # Stop
            app.add_handler(PrefixHandler("", "stop1", stop1))
            app.add_handler(PrefixHandler("", "stop2", stop2))
            app.add_handler(PrefixHandler("", "stop3", stop3))
            app.add_handler(PrefixHandler("", "stop4", stop4))
            app.add_handler(PrefixHandler("", "stopall", stopall))
            # Random raid
            app.add_handler(PrefixHandler("", "randomraid", randomraid))
            app.add_handler(PrefixHandler("", "stoprandomraid", stoprandomraid))
            # Owner
            app.add_handler(PrefixHandler("", "addsudo", addsudo))
            app.add_handler(PrefixHandler("", "delsudo", delsudo))
            app.add_handler(PrefixHandler("", "sudos", sudos))
            app.add_handler(PrefixHandler("", "admin", admin))
            app.add_handler(PrefixHandler("", "bye", bye))
            # Utility
            app.add_handler(PrefixHandler("", "status", status_cmd))
            app.add_handler(PrefixHandler("", "help", help_cmd))
            app.add_handler(PrefixHandler("", "over", over_cmd))
            app.add_handler(PrefixHandler("", "delay", delay_cmd))

            apps.append(app); bots.append(app.bot)
            await app.initialize()
            await app.start()
            await app.updater.start_polling()
            print(f"🚀 SHADOW bot started: {token[:10]}...")
        except Exception as e:
            print(f"❌ Failed: {e}")

    print(f"\n🌙 𝐒𝐇𝐀𝐃𝐎𝐖 𝐁ʜᴀɢᴡᴀɴ 🕷️")
    print(f"🤖 Total bots online: {len(bots)}")
    print(f"👑 Owner ID: {OWNER_ID}")
    print(f"⚙️ Prefix: (none)")
    await asyncio.Event().wait()

if __name__ == "__main__":
    print("\n" + "="*50)
    print("𝐒𝐇𝐀𝐃𝐎𝐖 BHAGWAN MULTI-BOT SYSTEM v3")
    print("="*50)
    print("\n✅ ACCESS GRANTED! INITIALIZING BOTS...\n")
    try: asyncio.run(run_all_bots())
    except KeyboardInterrupt: print("\n🛑 Bots stopped.")
    except Exception as e: print(f"❌ Error: {e}")