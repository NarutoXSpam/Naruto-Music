#THIS BOT IS PRIVATE FOR POSITIVE VIBE GROUP

from strings import get_string
from YukkiMusic.misc import SUDOERS
from YukkiMusic.utils.database import (get_lang, is_commanddelete_on,
                                       is_maintenance)


def language(mystic):
    async def wrapper(_, message, **kwargs):
        if await is_maintenance() is False:
            if message.from_user.id not in SUDOERS:
                return await message.reply_text(
                    "𝙒𝙚 𝘼𝙧𝙚 𝘿𝙤𝙞𝙣𝙜 𝙈𝙖𝙞𝙣𝙩𝙚𝙣𝙖𝙣𝙘𝙚 𝙊𝙛 𝙏𝙝𝙚 𝘽𝙤𝙩 𝘿𝙪𝙚 𝙏𝙤 𝙇𝙤𝙖𝙙 𝙊𝙛 𝙈𝙖𝙣𝙮 𝙂𝙧𝙤𝙪𝙥𝙨. 𝙋𝙡𝙚𝙖𝙨𝙚 𝙬𝙖𝙞𝙩 𝙛𝙤𝙧 𝙨𝙤𝙢𝙚 𝙩𝙞𝙢𝙚..."
                )
        if await is_commanddelete_on(message.chat.id):
            try:
                await message.delete()
            except:
                pass
        try:
            language = await get_lang(message.chat.id)
            language = get_string(language)
        except:
            language = get_string("en")
        return await mystic(_, message, language)

    return wrapper


def languageCB(mystic):
    async def wrapper(_, CallbackQuery, **kwargs):
        if await is_maintenance() is False:
            if CallbackQuery.from_user.id not in SUDOERS:
                return await CallbackQuery.answer(
                    "𝙒𝙚 𝘼𝙧𝙚 𝘿𝙤𝙞𝙣𝙜 𝙈𝙖𝙞𝙣𝙩𝙚𝙣𝙖𝙣𝙘𝙚 𝙊𝙛 𝙏𝙝𝙚 𝘽𝙤𝙩 𝘿𝙪𝙚 𝙏𝙤 𝙇𝙤𝙖𝙙 𝙊𝙛 𝙈𝙖𝙣𝙮 𝙂𝙧𝙤𝙪𝙥𝙨. 𝙋𝙡𝙚𝙖𝙨𝙚 𝙬𝙖𝙞𝙩 𝙛𝙤𝙧 𝙨𝙤𝙢𝙚 𝙩𝙞𝙢𝙚...",
                    show_alert=True,
                )
        try:
            language = await get_lang(CallbackQuery.message.chat.id)
            language = get_string(language)
        except:
            language = get_string("en")
        return await mystic(_, CallbackQuery, language)

    return wrapper


def LanguageStart(mystic):
    async def wrapper(_, message, **kwargs):
        try:
            language = await get_lang(message.chat.id)
            language = get_string(language)
        except:
            language = get_string("en")
        return await mystic(_, message, language)

    return wrapper
