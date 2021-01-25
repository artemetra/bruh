import asyncio
from random import choice, randint
from telethon import functions
from .. import loader, utils
import random
from userbot.events import register
import requests

def register(cb):
	cb(unsh())

class unsh(loader.Module):
    strings = {'name': 'Unshorten Links'}
    async def unsh(self, message):
        
        '''Расшифровывание укорочённых ссылок (bit.ly, goog.le и т.д.)'''
        test = requests.get('https://unshorten.me/s/goo.gl/IGL1lE')
        #test.json()
        reply = await event.get_reply_message()
        await event.client.send_message(event.to_id, test, reply_to=reply)
