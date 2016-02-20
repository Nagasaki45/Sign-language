import re
import asyncio
import json

from aiohttp import web, MsgType
from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import AsyncIOOSCUDPServer

import audio_utils

osc_msg_pattern = re.compile(r'^/output_(\d+)$')
with open('index.html') as f:
    index_html = f.read().encode('ascii')

sentences = {
    1: 'hello',
    2: 'My name is Tom',
    3: 'What is your name?',
}


def say_handler(msg):
    sentence_number = int(osc_msg_pattern.match(msg).groups()[0])
    audio_utils.say(sentences[sentence_number])


def init_osc(loop):
    dispatcher = Dispatcher()
    dispatcher.map("/output_*", say_handler)
    osc_server = AsyncIOOSCUDPServer(('127.0.0.1', 12000), dispatcher, loop)
    osc_server.serve()  # Calls 'run_until_complete' internally


async def init_web(loop):
    app = web.Application()
    websocket_handler = WebSocketHandler()
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/ws', websocket_handler.handle)
    app.router.add_static('/static', 'static')
    await loop.create_server(app.make_handler(), '0.0.0.0', 8080)


async def index(request):
    return web.Response(body=index_html)


class WebSocketHandler:
    async def handle(self, request):
        ws = web.WebSocketResponse()
        await ws.prepare(request)

        async for msg in ws:
            if msg.tp == MsgType.text:
                msg_dict = json.loads(msg.data)
                msg_type = msg_dict.pop('type')
                handler = getattr(self, 'handle_' + msg_type)
                await handler(ws, msg_dict)

    async def handle_get_sentences(self, ws, msg_dict):
        js_sentences = [{'id': k, 'text': v} for k, v in sentences.items()]
        response = {'type': 'sentences', 'content': js_sentences}
        ws.send_str(json.dumps(response))


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
