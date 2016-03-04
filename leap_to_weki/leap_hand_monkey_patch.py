"""
I missed some of the functionality of Leap.Finger in Leap.Hand,
so I'm adding it here
"""
from .leap_python3.Leap import Hand

Hand.LEFT = 0
Hand.RIGHT = 1
def hand_type(hand):
    if hand.is_left:
        return Hand.LEFT
    else:
        return Hand.RIGHT
Hand.type = property(hand_type)
