#tset

from telethon import events
import asyncio

@borg.on(events.NewMessage(pattern=r"\.bruh", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    for _ in range(100):
        await event.edit("".join("cum" + _))
