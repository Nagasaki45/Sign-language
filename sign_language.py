from leap_python3 import Leap
from frame_handler import Handler
from dict_of_signs import DICT
import audio


class SampleListener(Leap.Listener):

    def on_init(self, controller):
        self.handler = Handler()

    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        frame = controller.frame()
        sol = self.handler.handle(frame)
        try:
            audio.say(DICT[sol])
        except KeyError:
            pass


def main():
    # Create a sample listener and controller
    controller = Leap.Controller()
    listener = SampleListener()

    # Enable gestures
    controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
    controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
    controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
    controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    ans = input("Press Enter to quit...\n")

    # Remove the sample listener when done
    controller.remove_listener(listener)


if __name__ == "__main__":
    main()
