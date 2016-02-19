from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import ThreadingOSCUDPServer

import osc_utils
import audio_utils


def say_handler(*args):
    if len(args) > 1:
        return
    msg = args[0]
    text = msg.lstrip('/').replace('_', ' ')
    audio_utils.say(text)


def main():
    dispatcher = Dispatcher()
    dispatcher.map("/*", say_handler)
    osc_server = ThreadingOSCUDPServer(('127.0.0.1', 12000), dispatcher)
    osc_server.serve_forever()


if __name__ == "__main__":
    main()
