#! /usr/bin/env python
from random import randint

def rand_partition(Arr, beg, end):
    pivot_pos = randint(beg, end-1)
    Arr[pivot_pos], Arr[end-1] = Arr[end-1], Arr[pivot_pos]
    return partition(Arr, beg, end)

def partition(Arr, beg, end):
    last_small = beg - 1
    off_big = beg
    while off_big < end - 1:
        if Arr[off_big] < Arr[end-1]:
            last_small += 1
            Arr[off_big], Arr[last_small] = Arr[last_small], Arr[off_big]
        off_big += 1

    Arr[last_small+1], Arr[end-1] = Arr[end-1], Arr[last_small+1]
    return last_small + 1

def quicksort(Arr, beg, end):
    if beg < end:
        pos = rand_partition(Arr, beg, end)
        quicksort(Arr, beg, pos)
        quicksort(Arr, pos + 1, end)

if __name__ == '__main__':
    a = [2,5,2,5,6,1,4,7]
    print a
    quicksort(a, 0, len(a))
    print a
