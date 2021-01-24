from .. import loader, utils
import asyncio
import requests

@register(outgoing=True, pattern="^.unsh (.*)")

async def brhu(self, message):
    '''Расшифровывание укорочённых ссылок (bit.ly, goog.le и т.д.)'''
    test = requests.get('https://unshorten.me/s/goo.gl/IGL1lE')
    test.json()
    