import itertools

from .leap_python3.Leap import Finger, Hand
from . import leap_hand_monkey_patch


HAND_FINGERS = [Finger.TYPE_THUMB, Finger.TYPE_INDEX, Finger.TYPE_MIDDLE,
                Finger.TYPE_RING, Finger.TYPE_PINKY]
FINGERS = [(h, f) for h in [Hand.LEFT, Hand.RIGHT] for f in HAND_FINGERS]



def populate_hands_dict_from_fingers(hands_dict, fingers):
    for finger in fingers:
        hands_dict[finger.hand.type, finger.type] = finger.tip_position.to_tuple()


def get_raw_tip_positioning_data(frame):
    hands_dict = {f: (0, 0, 0) for f in FINGERS}
    populate_hands_dict_from_fingers(hands_dict, frame.fingers)
    return itertools.chain.from_iterable(hands_dict[f] for f in FINGERS)
