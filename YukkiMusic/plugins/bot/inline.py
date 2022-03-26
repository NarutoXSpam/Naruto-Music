#THIS BOT IS PRIVATE FOR POSITIVE VIBE GROUP
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup,
                            InlineQueryResultPhoto)
from youtubesearchpython.__future__ import VideosSearch

from config import BANNED_USERS, MUSIC_BOT_NAME
from YukkiMusic import app
from YukkiMusic.utils.inlinequery import answer


@app.on_inline_query(~BANNED_USERS)
async def inline_query_handler(client, query):
    text = query.query.strip().lower()
    answers = []
    if text.strip() == "":
        try:
            await client.answer_inline_query(
                query.id, results=answer, cache_time=10
            )
        except:
            return
    else:
        a = VideosSearch(text, limit=20)
        result = (await a.next()).get("result")
        for x in range(15):
            title = (result[x]["title"]).title()
            duration = result[x]["duration"]
            views = result[x]["viewCount"]["short"]
            thumbnail = result[x]["thumbnails"][0]["url"].split("?")[
                0
            ]
            channellink = result[x]["channel"]["link"]
            channel = result[x]["channel"]["name"]
            link = result[x]["link"]
            published = result[x]["publishedTime"]
            description = f"{views} | {duration} Mins | {channel}  | {published}"
            buttons = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="🎥 Watch on Youtube",
                            url=link,
                        )
                    ],
                ]
            )
            searched_text = f"""
❇️**𝙉𝙖𝙢𝙚:** [{title}]({link})

🎥**𝘾𝙝𝙖𝙣𝙣𝙚𝙡 𝙉𝙖𝙢𝙚:** {channel}
⏰**𝙋𝙪𝙗𝙡𝙞𝙨𝙝𝙚𝙙 𝘿𝙖𝙩𝙚:** {published}
⏳**𝘿𝙪𝙧𝙖𝙩𝙞𝙤𝙣:** {duration} Mins
👀**𝙑𝙞𝙚𝙬𝙨:** `{views}`


📎**Channel Link:** [Visit From Here]({channellink})

__Reply with /play 𝘰𝘯 𝘵𝘩𝘪𝘴 𝘴𝘦𝘢𝘳𝘤𝘩𝘦𝘥 𝘮𝘦𝘴𝘴𝘢𝘨𝘦 𝘵𝘰 𝘴𝘵𝘳𝘦𝘢𝘮 𝘪𝘵 𝘰𝘯 𝘷𝘰𝘪𝘤𝘦 𝘤𝘩𝘢𝘵.__

⚡️ ** Inline Search By {MUSIC_BOT_NAME} **"""
            answers.append(
                InlineQueryResultPhoto(
                    photo_url=thumbnail,
                    title=title,
                    thumb_url=thumbnail,
                    description=description,
                    caption=searched_text,
                    reply_markup=buttons,
                )
            )
        try:
            return await client.answer_inline_query(
                query.id, results=answers
            )
        except:
            return
