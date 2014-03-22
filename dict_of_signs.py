# gesture structure
# sol = (hands, fingers_a, fingers_b, gesture, direction)

DICT = {
    # swipes
    (1, 1, 0, 'gesture_swipes', '+x'): 'hello',
    (1, 2, 0, 'gesture_swipes', '+x'): 'hello',
    (1, 2, 0, 'gesture_swipes', '+y'): 'How are you feeling',
    (1, 4, 0, 'gesture_swipes', '+x'): 'Was it Hard',
    (1, 1, 0, 'gesture_swipes', '+y'): 'beep',
    (1, 1, 0, 'gesture_swipes', '-y'): 'OK',
    (1, 1, 0, 'gesture_swipes', '-x'): 'Have a great week',
    (1, 2, 0, 'gesture_swipes', '-x'): 'Have a great week',
    (1, 3, 0, 'gesture_swipes', '-x'): 'Have a great week',
    # circles
    (2, 1, 1, 'gesture_circles', 'clockwise'): 'Tired',
    (1, 1, 0, 'gesture_circles', 'clockwise'): 'thank you',
    (1, 1, 0, 'gesture_circles', 'counterclockwise'): 'We should do it again',
    # taps
    'TAP': 'I',
    'SCREEN_TAP': 'you'
}

OLD_DICT = {'+x110.0': 'hello',
            '+x120.0': 'hello',
            '+y120.0': 'How are you feeling',
            'CR2': 'Tired',
            "+x140.0": 'Was it Hard',
            "+x130.0": 'Was it Hard',
            '+y110.0': 'beep',
            'CL1': 'We should do it again',
            '-y110.0': 'OK',
            '-x110.0': 'Have a great week',
            '-x120.0': 'Have a great week',
            '-x130.0': 'Have a great week',
            'TAP': 'I',
            'SCREEN_TAP': 'you',
            'CR1': 'thank you'
            }
