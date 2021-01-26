import asyncio
from random import choice, randint
from telethon import functions
from .. import loader, utils
import random
# from userbot.messages import register
import requests

#def register(cb):
#	cb(unsh())

class unsh(loader.Module):
    strings = {'name': 'Unshorten Links'}
    async def unsh(self, message):
        
        test = requests.get('https://unshorten.me/s/goo.gl/IGL1lE')
        #test.json()
        reply = await message.get_reply_message()
        await message.client.send_message(message.to_id, test, reply_to=reply)
