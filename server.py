import asyncio

from aiohttp import web
from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import AsyncIOOSCUDPServer

import audio_utils

with open('index.html') as f:
    index_html = f.read().encode('ascii')


def say_handler(*args):
    if len(args) > 1:
        return
    msg = args[0]
    text = msg.lstrip('/').replace('_', ' ')
    audio_utils.say(text)


def init_osc(loop):
    dispatcher = Dispatcher()
    dispatcher.map("/*", say_handler)
    osc_server = AsyncIOOSCUDPServer(('127.0.0.1', 12000), dispatcher, loop)
    osc_server.serve()  # Calls 'run_until_complete' internally


async def init_web(loop):
    app = web.Application()
    app.router.add_route('GET', '/', index)
    app.router.add_static('/static', 'static')
    await loop.create_server(app.make_handler(), '0.0.0.0', 8080)


async def index(request):
    return web.Response(body=index_html)


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init_web(loop))
    init_osc(loop)  # Calls 'run_until_complete' internally
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
