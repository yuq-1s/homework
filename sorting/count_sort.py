#! /usr/bin/env python
from pdb import set_trace

def count_sort(Arr):
    min_value = min(Arr)
    max_value = max(Arr)

    # HACK: zeros(max.....)
    B = ([0]*(max_value - min_value + 1))[:]
    for num in Arr:
        B[num-min_value]+=1

    last_num = 0
    for i in range(len(B)):
        B[i] += last_num
        last_num = B[i]
    del last_num

    C = ([0]*len(Arr))[:]
    for num in reversed(Arr):
        C[B[num-min_value]-1] = num
        B[num-min_value] -= 1

    return C

if __name__ == '__main__':
    a = [3,2,6,3,6,4,8,4,2,5,7,3]
    print a
    print count_sort(a)
