import asyncio
from random import choice, randint
from telethon import functions
from .. import loader, utils
import random
from userbot.events import register
import requests


class unsh(loader.Module):
    strings = {'name': 'Unshorten Links'}
    async def unsh(self, message, event):
        test = requests.get('https://unshorten.me/s/goo.gl/IGL1lE')
        #test.json()
        reply = await event.get_reply_message()
        await event.client.send_message(event.to_id, test, reply_to=reply)
