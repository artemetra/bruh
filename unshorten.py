import asyncio
from random import choice, randint
from telethon import functions
from .. import loader, utils
import random
from userbot.events import register
import requests

@register(outgoing=True, pattern="^.unsh (.*)")

async def brhu(self, message):
    '''Расшифровывание укорочённых ссылок (bit.ly, goog.le и т.д.)'''
    test = requests.get('https://unshorten.me/s/goo.gl/IGL1lE')
    test.json()
    
