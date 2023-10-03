#!/usr/bin/python3
"""Unlock Boxes"""


def canUnlockAll(boxes):
    """Can boxes be unlocked"""

    if not isinstance(boxes, list) or not all(isinstance(box, list) for box in boxes):
        return False

    keys = [0]
    for key in keys:
        for box in boxes[key]:
            if box not in keys and box < len(boxes):
                keys.append(box)

    return len(keys) == len(boxes)
