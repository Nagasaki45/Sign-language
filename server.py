import re
import asyncio
from itertools import count

from aiohttp import web
from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import AsyncIOOSCUDPServer
from pythonosc import udp_client
from pythonosc.osc_message_builder import OscMessageBuilder

import audio_utils

osc_msg_pattern = re.compile(r'^/output_(\d+)$')
with open('index.html') as f:
    index_html = f.read().encode('ascii')

sentences = {
    1: 'Hello',
    2: 'My name is Tom',
    3: 'What is your name?',
}


def allocate_id(existing_ids):
    """Find the smallest non reserved id."""
    for i in count(start=1):
        if not i in existing_ids:
            return i


def say_handler(msg):
    sentence_number = int(osc_msg_pattern.match(msg).groups()[0])
    audio_utils.say(sentences[sentence_number])


def init_osc(loop):
    dispatcher = Dispatcher()
    dispatcher.map("/output_*", say_handler)
    osc_server = AsyncIOOSCUDPServer(('127.0.0.1', 12000), dispatcher, loop)
    osc_server.serve()  # Calls 'run_until_complete' internally


def control_wekinator(endpoint, arg=None):
    builder = OscMessageBuilder('/wekinator/control/{}'.format(endpoint))
    if arg is not None:
        builder.add_arg(arg)
    msg = builder.build()
    udp_client.UDPClient('127.0.0.1', 6448).send(msg)


async def init_web(loop):
    app = web.Application()
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/ajax/sentences', get_sentences)
    app.router.add_route('GET', '/ajax/record_start', record_start)
    app.router.add_route('GET', '/ajax/record_stop', record_stop)
    app.router.add_route('GET', '/ajax/delete', delete)
    app.router.add_route('GET', '/ajax/add_new_sentence', add_new_sentence)
    app.router.add_static('/static', 'static')
    await loop.create_server(app.make_handler(), '127.0.0.1', 8080)


async def index(request):
    return web.Response(body=index_html)


async def get_sentences(request):
    js_sentences = [{'id': k, 'text': v} for k, v in sentences.items()]
    return web.json_response(js_sentences)


async def record_start(request):
    control_wekinator('startDtwRecording', int(request.GET['id']))
    control_wekinator('startRunning')
    return web.json_response({})


async def record_stop(request):
    control_wekinator('stopDtwRecording', int(request.GET['id']))
    return web.json_response({})


async def delete(request):
    sentences.pop(int(request.GET['id']))
    return web.json_response({})


async def add_new_sentence(request):
    text = request.GET['text']
    id_ = allocate_id(sentences.keys())
    sentences[id_] = text
    return web.json_response({'text': text, 'id': id_})


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
