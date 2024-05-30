from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message

from DAXXMUSIC import app
from DAXXMUSIC.core.call import DAXX
from DAXXMUSIC.utils import bot_sys_stats
from DAXXMUSIC.utils.decorators.language import language
from DAXXMUSIC.utils.inline import supp_markup
from config import BANNED_USERS, VERSION_IMG_URL


@app.on_message(filters.command("version", prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & ~BANNED_USERS)
@language
async def version_com(client, message: Message, _):
    start = datetime.now()
    response = await message.reply_photo(
        photo=VERSION_IMG_URL,
        caption=_["version"].format(app.mention),
    )
