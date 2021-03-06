import asyncio
import logging

from .. import loader, utils

import re

logger = logging.getLogger(__name__)


@loader.tds
class YourMod(loader.Module):
    """sed-like regex substitution"""  # Translateable due to @loader.tds
    strings = {"cfg_doc": "This is what is said, you can edit me with the configurator",
               "name": "regex",
               "after_sleep": "We have finished sleeping!"}

    def __init__(self):
        self.config = loader.ModuleConfig("CONFIG_STRING", "hello", lambda m: self.strings("cfg_doc", m))

    @loader.unrestricted  # Security setting to change who can use the command (defaults to owner | sudo)
    async def regexcmd(self, message):
        pattern = utils.get_args(message)
        pattern = str(pattern[0])
        #pattern = pattern.replace('/', '//')
        await utils.answer(message, str(pattern))
