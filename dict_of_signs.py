# gesture structure
# sol = (hands, fingers_a, fingers_b, gesture, direction)

DICT = {
    # swipes
    (1, 3, 0, 'gesture_swipes', '+x'): 'hello', # 5 fingers
    (1, 4, 0, 'gesture_swipes', '+x'): 'hello',
    (1, 5, 0, 'gesture_swipes', '+x'): 'hello',

    (1, 1, 0, 'gesture_swipes', '+x'): 'Was it Hard', # 1 finger
    (1, 2, 0, 'gesture_swipes', '+x'): 'Was it Hard',

    (1, 1, 0, 'gesture_swipes', '+y'): 'beep',
    (1, 2, 0, 'gesture_swipes', '+y'): 'beep',

    (1, 3, 0, 'gesture_swipes', '+y'): 'How are you feeling', # 5 fingers
    (1, 4, 0, 'gesture_swipes', '+y'): 'How are you feeling',
    (1, 5, 0, 'gesture_swipes', '+y'): 'How are you feeling',

    (1, 1, 0, 'gesture_swipes', '-y'): 'OK',
    (1, 2, 0, 'gesture_swipes', '-y'): 'OK',

    (1, 3, 0, 'gesture_swipes', '-x'): 'Have a great week', # 5 fingers
    (1, 4, 0, 'gesture_swipes', '-x'): 'Have a great week',
    (1, 5, 0, 'gesture_swipes', '-x'): 'Have a great week',

    # circles
    (2, 1, 1, 'gesture_circles', 'clockwise'): 'So so',
    (2, 2, 1, 'gesture_circles', 'clockwise'): 'So so',
    (2, 3, 1, 'gesture_circles', 'clockwise'): 'So so',
    (2, 4, 1, 'gesture_circles', 'clockwise'): 'So so',
    (2, 5, 1, 'gesture_circles', 'clockwise'): 'So so',
    (2, 1, 2, 'gesture_circles', 'clockwise'): 'So so',
    (2, 2, 2, 'gesture_circles', 'clockwise'): 'So so',
    (2, 3, 2, 'gesture_circles', 'clockwise'): 'So so',
    (2, 4, 2, 'gesture_circles', 'clockwise'): 'So so',
    (2, 5, 2, 'gesture_circles', 'clockwise'): 'So so',
    (2, 1, 3, 'gesture_circles', 'clockwise'): 'So so',
    (2, 2, 3, 'gesture_circles', 'clockwise'): 'So so',
    (2, 3, 3, 'gesture_circles', 'clockwise'): 'So so',
    (2, 4, 3, 'gesture_circles', 'clockwise'): 'So so',
    (2, 5, 3, 'gesture_circles', 'clockwise'): 'So so',
    (2, 1, 4, 'gesture_circles', 'clockwise'): 'So so',
    (2, 2, 4, 'gesture_circles', 'clockwise'): 'So so',
    (2, 3, 4, 'gesture_circles', 'clockwise'): 'So so',
    (2, 4, 4, 'gesture_circles', 'clockwise'): 'So so',
    (2, 5, 4, 'gesture_circles', 'clockwise'): 'So so',
    (2, 1, 5, 'gesture_circles', 'clockwise'): 'So so',
    (2, 2, 5, 'gesture_circles', 'clockwise'): 'So so',
    (2, 3, 5, 'gesture_circles', 'clockwise'): 'So so',
    (2, 4, 5, 'gesture_circles', 'clockwise'): 'So so',
    (2, 5, 5, 'gesture_circles', 'clockwise'): 'So so',

    (1, 1, 0, 'gesture_circles', 'clockwise'): 'thank you',
    (1, 2, 0, 'gesture_circles', 'clockwise'): 'thank you',
    (1, 3, 0, 'gesture_circles', 'clockwise'): 'thank you',
    (1, 4, 0, 'gesture_circles', 'clockwise'): 'thank you',
    (1, 5, 0, 'gesture_circles', 'clockwise'): 'thank you',

    (1, 1, 0, 'gesture_circles', 'counterclockwise'): 'We should do it again',
    (1, 2, 0, 'gesture_circles', 'counterclockwise'): 'We should do it again',
    (1, 3, 0, 'gesture_circles', 'counterclockwise'): 'We should do it again',
    (1, 4, 0, 'gesture_circles', 'counterclockwise'): 'We should do it again',
    (1, 5, 0, 'gesture_circles', 'counterclockwise'): 'We should do it again',

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
