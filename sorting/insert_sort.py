#! /usr/bin/env python
from sys import argv

def insert(Arr, i):
    for j in reversed(range(1, i+1)):
        if Arr[j-1] < Arr[j]:   return
        Arr[j-1], Arr[j] = Arr[j], Arr[j-1]

def insert_sort(Arr):
    for i in range(len(Arr)):
        insert(Arr, i)

# a = [6,3,7,3,8,1,9]
# insert_sort(a)
if __name__ == '__main__':
    b = argv[1:]
    insert_sort(b)
    print b
