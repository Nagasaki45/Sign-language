import Leap
import frame_handler

class SampleListener(Leap.Listener):

    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        frame = controller.frame()
        frame_handler.handle(frame)


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
    print "Press Enter to quit..."
    ans = raw_input()

    # Remove the sample listener when done
    controller.remove_listener(listener)


if __name__ == "__main__":
    main()
