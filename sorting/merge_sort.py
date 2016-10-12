#! /usr/bin/env python
from itertools import cycle
from sys import argv

def do_merge(side, turn_th):
    new_merge = []
    while side:
        if turn_th < side[0]:   return new_merge
        new_merge.append(side.pop(0))
    return new_merge

def merge(left, right):
    # if not left:    return right
    # if not right:   return left
    sides = cycle([left, right])
    merged = []
    turn_threshold = right[0]
    for side in sides:
        merged += do_merge(side, turn_threshold)
        if not side:
            merged += next(sides)
            return merged
        turn_threshold = side[0]
    assert False    # Above loop should not end before return

def merge_sort(Arr):
    l = len(Arr)
    if l <= 1:  return Arr
    left = merge_sort(Arr[:l/2])
    right = merge_sort(Arr[l/2:])
    return merge(left, right)

if __name__ == '__main__':
    a = [3,7,3,8,3,9,5,8,5,4,2,234,654,4,92,23,346,545,2,12]
    print merge_sort(a)
