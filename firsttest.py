# requires: pydub numpy requests
import io
import math
import re

import numpy as np
import requests
from pydub import AudioSegment, effects

from pyrogram import Client, filters
from pyrogram.types import Message
from ..utils.utils import modules_help, requirements_list, prefix

strings = {
    "name": "AudioEditor",
    "downloading": "<b>[{}]</b> Downloading...",
    "working": "<b>[{}]</b> Working...",
    "exporting": "<b>[{}]</b> Exporting...",
    "set_value": "<b>[{}]</b> Specify the level from {} to {}...",
    "reply": "<b>[{}]</b> reply to audio...",
    "set_fmt": "<b>[{}]</b> Specify the format of output audio...",
    "set_time": "<b>[{}]</b> Specify the time in the format start(ms):end(ms)"
}

# basscmd
@Client.on_message(filters.command('bass', prefix) & filters.me)
async def example_edit(client: Client, message: Message):
    """.bass [level bass'а 2-100 (Default 2)] <reply to audio>
    BassBoost"""
    args = message.command[1:]
    if not args:
        lvl = 2.0
    elif re.match(r'^\d+(\.\d+)?$', args) and (1.0 < float(args) < 100.1):
        lvl = float(args)
    else:
        return await message.reply_text(strings("set_value", message).format('BassBoost', 2.0, 100.0))
    await message.reply_text("beeba")

@Client.on_message(filters.command('example_send', prefix) & filters.me)
async def example_send(client: Client, message: Message):
    await client.send_message(message.chat.id, '<b>This is an example module</b>')

class AudioEditorClass():
        audio = None
        message = None
        duration = None
        voice = None
        pref = None
        reply = None

modules_help.append({'example': '''example_send - example send, example_edit - example edit''',
                     'example module': 'Example_send: example_send, example_edit'})

