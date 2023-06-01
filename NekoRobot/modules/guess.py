import random

from telethon import events

from NekoRobot import tbot as neko


@neko.on(events.NewMessage(pattern="/guess ?(.*)"))
async def wish(e):
    if e.is_reply:
        mm = random.randint(1, 100)
        lol = await e.get_reply_message()
        fire = "https://graph.org/file/03e0a8175f7c66e56b8d9.jpg"
        await neko.send_file(
            e.chat_id,
            fire,
            caption=f"**Hey [{e.sender.first_name}](tg://user?id={e.sender.id}), Your Guess is {mm}%__**\n\n__Correct!!!",
            reply_to=lol,
        )
    if not e.is_reply:
        mm = random.randint(1, 100)
        fire = "https://graph.org/file/03e0a8175f7c66e56b8d9.jpg"
        await neko.send_file(
            e.chat_id,
            fire,
            caption=f"**Hey [{e.sender.first_name}](tg://user?id={e.sender.id}), Your Guess is {mm}%__**\n\n__Correct!!!",
            reply_to=e,
        )
