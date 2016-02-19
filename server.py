import asyncio

from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import AsyncIOOSCUDPServer

import osc_utils
import audio_utils


def say_handler(*args):
    if len(args) > 1:
        return
    msg = args[0]
    text = msg.lstrip('/').replace('_', ' ')
    audio_utils.say(text)


def main():
    loop = asyncio.get_event_loop()
    dispatcher = Dispatcher()
    dispatcher.map("/*", say_handler)
    osc_server = AsyncIOOSCUDPServer(('127.0.0.1', 12000), dispatcher, loop)
    osc_server.serve()
    loop.run_forever()


if __name__ == "__main__":
    main()
