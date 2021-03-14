import asyncio
import logging
import requests

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class YourMod(loader.Module):
    """unshorten shortened links"""  # Translateable due to @loader.tds
    strings = {"cfg_doc": "This is what is said, you can edit me with the configurator",
               "name": "unsh",
               "after_sleep": "We have finished sleeping!"}

    def __init__(self):
        self.config = loader.ModuleConfig("CONFIG_STRING", "hello", lambda m: self.strings("cfg_doc", m))

    @loader.unrestricted  # Security setting to change who can use the command (defaults to owner | sudo)
    async def unshcmd(self, message):
        """Does something when you type .example (hence, named examplecmd)"""
        logger.debug("We logged something!")
        #await utils.answer(message, self.config["CONFIG_STRING"])
        #await asyncio.sleep(5)  # Never use time.sleep
        #await utils.answer(message, self.strings("after_sleep", message))
        test = requests.get('https://unshorten.me/s/goo.gl/IGL1lE')
        await utils.answer(message, test)
