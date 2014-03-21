import Leap

# DON'T USE THIS HANDLER
def old_handle(frame_data):

    def state_string(state):
        if state == Leap.Gesture.STATE_START:
            return "STATE_START"

        if state == Leap.Gesture.STATE_UPDATE:
            return "STATE_UPDATE"

        if state == Leap.Gesture.STATE_STOP:
            return "STATE_STOP"

        if state == Leap.Gesture.STATE_INVALID:
            return "STATE_INVALID"

    print "Frame id: %d, timestamp: %d, hands: %d, fingers: %d, tools: %d, gestures: %d" % (
              frame.id, frame.timestamp, len(frame.hands), len(frame.fingers), len(frame.tools), len(frame.gestures()))

    if not frame.hands.is_empty:
        # Get the first hand
        hand = frame.hands[0]

        # Check if the hand has any fingers
        fingers = hand.fingers
        if not fingers.is_empty:
            # Calculate the hand's average finger tip position
            avg_pos = Leap.Vector()
            for finger in fingers:
                avg_pos += finger.tip_position
            avg_pos /= len(fingers)
            print "Hand has %d fingers, average finger tip position: %s" % (
                  len(fingers), avg_pos)

        # Get the hand's sphere radius and palm position
        print "Hand sphere radius: %f mm, palm position: %s" % (
              hand.sphere_radius, hand.palm_position)

        # Get the hand's normal vector and direction
        normal = hand.palm_normal
        direction = hand.direction

        # Calculate the hand's pitch, roll, and yaw angles
        print "Hand pitch: %f degrees, roll: %f degrees, yaw: %f degrees" % (
            direction.pitch * Leap.RAD_TO_DEG,
            normal.roll * Leap.RAD_TO_DEG,
            direction.yaw * Leap.RAD_TO_DEG)

        # Gestures
        for gesture in frame.gestures():
            if gesture.type == Leap.Gesture.TYPE_CIRCLE:
                circle = Leap.CircleGesture(gesture)

                # Determine clock direction using the angle between the pointable and the circle normal
                if circle.pointable.direction.angle_to(circle.normal) <= Leap.PI/4:
                    clockwiseness = "clockwise"
                else:
                    clockwiseness = "counterclockwise"

                # Calculate the angle swept since the last frame
                swept_angle = 0
                if circle.state != Leap.Gesture.STATE_START:
                    previous_update = CircleGesture(controller.frame(1).gesture(circle.id))
                    swept_angle =  (circle.progress - previous_update.progress) * 2 * Leap.PI

                print "Circle id: %d, %s, progress: %f, radius: %f, angle: %f degrees, %s" % (
                        gesture.id, state_string(gesture.state),
                        circle.progress, circle.radius, swept_angle * Leap.RAD_TO_DEG, clockwiseness)

            if gesture.type == Leap.Gesture.TYPE_SWIPE:
                swipe = Leap.SwipeGesture(gesture)
                print "Swipe id: %d, state: %s, position: %s, direction: %s, speed: %f" % (
                        gesture.id, state_string(gesture.state),
                        swipe.position, swipe.direction, swipe.speed)

            if gesture.type == Leap.Gesture.TYPE_KEY_TAP:
                keytap = Leap.KeyTapGesture(gesture)
                print "Key Tap id: %d, %s, position: %s, direction: %s" % (
                        gesture.id, state_string(gesture.state),
                        keytap.position, keytap.direction )

            if gesture.type == Leap.Gesture.TYPE_SCREEN_TAP:
                screentap = Leap.ScreenTapGesture(gesture)
                print "Screen Tap id: %d, %s, position: %s, direction: %s" % (
                        gesture.id, state_string(gesture.state),
                        screentap.position, screentap.direction )

    if not (frame.hands.is_empty and frame.gestures().is_empty):
        print ""


BACK_STACK_MAX_LEN = 50
back_stack = []
counter = dict(frames=0,
               hands=0,
               fingers_l=0,
               fingers_r=0)


def handle(frame):

    if frame.gestures():
        back_stack.append(frame)
        if len(back_stack) >= 2 * BACK_STACK_MAX_LEN:
            back_stack.pop(BACK_STACK_MAX_LEN)
        # add stuff to counter



    elif not frame.gestures() and back_stack:
        # calculate back_stack and counter means
        frames = counter['frames'] or 1
        hands = round(float(counter['hands']) / frames)
        fingers_l = round(float(counter['fingers_l']) / frames)
        fingers_r = round(float(counter['fingers_r']) / frames)
        gestures = {key: value for key, value in counter.items()
            if key.startswith('gesture')}
        print(gestures)

        # empty back_stack and counter
        back_stack = []
        counter = {}

        # TODO remove this
        gesture = "SWIPE"
        direction = "UP"

        # return solution
        return (hands, fingers_l, fingers_r, gesture, direction)
