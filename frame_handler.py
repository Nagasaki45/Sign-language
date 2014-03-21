import Leap

def handle(frame_data, callback):

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
