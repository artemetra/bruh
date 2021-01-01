#tset

from telethon import events
import asyncio

@borg.on(events.NewMessage(pattern=r"\.bruh", outgoing=True))
async def _(event):
    strings = {'name': 'bruh'}
    if event.fwd_from:
        return
    await event.edit("cum")
