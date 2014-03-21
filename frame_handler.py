import Leap


class Handler:

    BACK_STACK_MAX_LEN = 30
    NO_GESTURE_COUNTER_MAX_LEN = 2

    def __init__(self):
        self.init_data_structures()

    def init_data_structures(self):
        self.back_stack = []
        self.counter = dict(frames=0,
                            hands=0,
                            fingers_a=0,
                            fingers_b=0,
                            gesture_circles=0,
                            gesture_swipes=0,
                            gesture_key_taps=0,
                            gesture_screen_taps=0)
        self.no_gesture_counter = 0

    def handle(self, frame):

        # print(frame.hands[0].palm_position)

        if frame.gestures():
            self.back_stack.append(frame)
            if len(self.back_stack) > self.BACK_STACK_MAX_LEN:
                self.back_stack.pop(self.BACK_STACK_MAX_LEN / 2)
            # add stuff to counter
            self.counter['frames'] += 1
            self.counter['hands'] += len(frame.hands)
            self.counter['fingers_a'] += len(frame.hands[0].fingers)
            self.counter['fingers_b'] += len(frame.hands[1].fingers)
            for gesture in frame.gestures():
                if gesture.type == Leap.Gesture.TYPE_CIRCLE:
                    self.counter['gesture_circles'] += 1
                    return None
                if gesture.type == Leap.Gesture.TYPE_SWIPE:
                    self.counter['gesture_swipes'] += 1
                    return None
                if gesture.type == Leap.Gesture.TYPE_KEY_TAP:
                    self.counter['gesture_key_taps'] += 1
                    return None
                if gesture.type == Leap.Gesture.TYPE_SCREEN_TAP:
                    self.counter['gesture_screen_taps'] += 1
                    return None

        if not frame.gestures() and self.back_stack:

            if self.no_gesture_counter < self.NO_GESTURE_COUNTER_MAX_LEN:
                self.no_gesture_counter += 1
                return None

            gestures = {key: value for key, value in self.counter.items()
                        if key.startswith('gesture')}
            gesture = max(gestures, key=lambda x: gestures[x])

            if not len(self.back_stack) >= self.BACK_STACK_MAX_LEN:
                self.init_data_structures()
                if gesture == 'gesture_key_taps':
                    print('TAP')
                    return 'TAP'
                if gesture == 'gesture_screen_taps':
                    print('SCREEN TAP')
                    return 'SCREEN_TAP'
                else:
                    print('back_stack too short and not a tap', gesture)
                    return None

            # calculate back_stack and counter means
            frames = self.counter['frames']
            hands = round(float(self.counter['hands']) / frames)
            fingers_a = round(float(self.counter['fingers_a']) / frames)
            fingers_b = round(float(self.counter['fingers_b']) / frames)

            vec = {'start':
                   {'l': [x.hands[0].palm_position for x in
                          self.back_stack[:(self.BACK_STACK_MAX_LEN / 2)]]},

                   'stop':
                   {'l': [x.hands[0].palm_position for x in
                          self.back_stack[(self.BACK_STACK_MAX_LEN / 2):]]}
                   }

            for name in ['start', 'stop']:
                vec_len = len(vec[name]['l'])
                vec[name]['x'] = sum([x[0] for x in vec[name]['l']]) / vec_len
                vec[name]['y'] = sum([x[1] for x in vec[name]['l']]) / vec_len
                vec[name]['z'] = sum([x[2] for x in vec[name]['l']]) / vec_len

            diff = {axis: (vec['stop'][axis] - vec['start'][axis])
                    for axis in ['x', 'y', 'z']}
            max_diff = max(diff, key=lambda x: abs(diff[x]))
            diff_direction = ('+' if diff[max_diff] > 0 else '-') + max_diff

            # return solution
            sol = (hands, fingers_a, fingers_b, gesture, diff_direction)
            print(sol)

            # empty back_stack and counter
            self.init_data_structures()
            return sol
