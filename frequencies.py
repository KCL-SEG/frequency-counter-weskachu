"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for item in items:
        key = str(item)
        if not key in frequencies:
            frequencies[key] = 1
        elif key in frequencies:
            frequencies[key] += 1

    return frequencies
