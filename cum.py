#tset

from telethon import events
import asyncio
import requests

@borg.on(events.NewMessage(pattern=r"\.bruh", outgoing=True))
async def _(event):
    strings = {'name': 'bruh'}
    #if event.fwd_from:
    #    return
    test = requests.get('https://unshorten.me/s/goo.gl/IGL1lE')
    
    await event.edit(str(test.text))
    
