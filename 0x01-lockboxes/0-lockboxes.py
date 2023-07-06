#!/usr/bin/python3
"""
Module: Unlock Boxes

This module provides a function to determine
if all boxes can be unlocked.
"""


def canUnlockAll(boxes):
    """
    Check if all boxes can be unlocked.
    Args:
        boxes (list): A list of lists representing the boxes
        and their corresponding keys.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    num_boxes = len(boxes)
    unlocked = [False] * num_boxes  # Keep track of the unlocked boxes
    unlocked[0] = True  # The first box is unlocked by default
    keys = [0]  # Start with the keys in the first box

    while keys:
        box = keys.pop()
        for key in boxes[box]:
            if key >= 0 and key < num_boxes and not unlocked[key]:
                unlocked[key] = True
                keys.append(key)

    return all(unlocked)
