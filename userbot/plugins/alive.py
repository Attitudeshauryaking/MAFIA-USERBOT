
# Thanks to @D3_krish
# Porting in MafiaBot by @H1M4N5HU0P

import asyncio
import random
from telethon import events, version
from userbot import mafiaversion
from userbot.utils import admin_cmd, sudo_cmd
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.cmdhelp import CmdHelp
from userbot.Config import Config
from . import *
# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "𝕄𝔸𝔽𝕀𝔸𝔹𝕆𝕋"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

mafia = bot.uid

MAFIA_IMG = Config.ALIVE_PIC or "https://telegra.ph/file/e97d640332ce5eadb3f89.mp4"
pm_caption = "  __**🔥🔥𝕄𝕠𝕥𝕚 𝕦𝕤𝕖𝕣𝕓𝕠𝕥 𝕚𝕤 𝕒𝕝𝕚𝕧𝕖🔥🔥**__\n\n"

pm_caption += f"**━❣️━━━❣️━━━🔥😈🔥━━❣️━━━❣️━━**\n\n"
pm_caption += (
    f"                 ◦•●◉✿𝐌𝐚𝐬𝐭𝐞𝐫✿◉●•◦\n  **『⚜️[{DEFAULTUSER}](tg://user?id={mafia})⚜️』**\n\n"
)
pm_caption += f"┏━━❣️━━❣️━━❣️━🔽\n"
pm_caption += f"┣🌀 `Telethon:` `{version.__version__}` \n"
pm_caption += f"┣🌀`Version:` `{mafiaversion}`\n"
pm_caption += f"┣🌀 `Sudo:` `{sudou}`\n"
pm_caption += f"┣🌀`Channel:` [ᴊᴏɪɴ](https://t.me/sweetkingdom1)\n"
pm_caption += f"┣🌀`Creator:` [𒆜₳₮₮ł₮ɄĐɆ ₭ł₦₲𒆜](https://t.me/Alone_Shaurya_king)\n"
pm_caption += f"┗━━━❣️━━━❣️━━━❣️━━🌀━▶️\n"
pm_caption += " [🅳🅴🆅🅴🅻🅾🅿🅴🆁](Https://t.me/Alone_Shaurya_king)"

# @command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()   
    await alive.delete()
    on = await borg.send_file(alive.chat_id, MAFIA_IMG,caption=pm_caption)

    
CmdHelp("alive").add_command(
  "alive", None, "To check am i alive"
).add()
