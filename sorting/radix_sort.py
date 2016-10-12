#! /usr/bin/env python

from merge_sort import merge_sort
from count_sort import count_sort
from insert_sort import insert_sort
from numpy import log

class radix(object):
    def __init__(self, num, r):
        self.__radixies = []
        self.__r = r
        while num:
            self.__radixies.append(num%self.__r)
            num /= self.__r
        self.__it = iter(self.__radixies)
        # private?
        self.cmp_next()

    def cmp_next(self):
        self.to_cmp = self.next()

    def next(self):
        return next(self.__it)

    def __lt__(self, other):
        return self.to_cmp < other.to_cmp

    def __sub__(self, other):
        return self.to_cmp - other.to_cmp

    def number(self):
        ret = 0
        for num in reversed(self.__radixies):
            ret += num
            ret *= self.__r
        return ret / self.__r

    def digit_count(self):
        return len(self.__radixies)

def radix_sort(arr):
    # B = [radix(num, int(log(len(Arr))/log(2))) for num in Arr]
    B = [radix(num, 10) for num in arr]
    try:
        while True:
            # B = insert_sort(B)
            # B = merge_sort(B)
            # B = count_sort(B)
            B = sorted(B)
            print [r.number() for r in B]
            for r in B:
                r.cmp_next()
    except StopIteration:
        return [r.number() for r in B]

if __name__ == '__main__':
    a = [351, 162, 716, 631, 234, 152, 362] 
    print a
    print radix_sort(a)
