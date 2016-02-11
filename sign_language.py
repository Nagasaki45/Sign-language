import threading
import time

from leap_python3 import Leap
from pythonosc.udp_client import UDPClient
from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import ThreadingOSCUDPServer

import leap_utils
import osc_utils
import audio_utils


class LeapListener(Leap.Listener):
    def on_init(self, controller):
        self.osc_client = UDPClient('127.0.0.1', 6448)

    def on_frame(self, controller):
        frame = controller.frame()
        positioning_values = leap_utils.get_raw_tip_positioning_data(frame)
        msg = osc_utils.build_osc_message(positioning_values)
        self.osc_client.send(msg)
        time.sleep(0.05)


def say_handler(*args):
    if len(args) > 1:
        return
    msg = args[0]
    text = msg.lstrip('/').replace('_', ' ')
    audio_utils.say(text)


def main():
    controller = Leap.Controller()
    listener = LeapListener()
    controller.add_listener(listener)

    dispatcher = Dispatcher()
    dispatcher.map("/*", say_handler)
    osc_server = ThreadingOSCUDPServer(('127.0.0.1', 12000), dispatcher)
    threading.Thread(target=osc_server.serve_forever, daemon=True).start()
    input('Press any key to quit...\n')


if __name__ == "__main__":
    main()
