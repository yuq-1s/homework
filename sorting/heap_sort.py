#! /usr/bin/env python

def parent(i):
    return (i/2) if i%2 else i/2-1

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

class max_heap:

    def __init__(self, Arr):
        self.__size = len(Arr)
        self.__arr = Arr
        for pos in reversed(range(self.__size/2)):
            self.max_heapify(pos)

    def max_heapify(self, pos):
        if left(pos) >= self.__size:    return
        if right(pos) == self.__size:
            largest = self.get_index_of_max(pos, left(pos))
        else:
            largest = self.get_index_of_max(pos, left(pos), right(pos))

        if largest != pos:
            self.__arr[largest], self.__arr[pos] = self.__arr[pos], self.__arr[largest]
            self.max_heapify(largest)

    def get_max(self):
        return self.__arr[0]

    def get_index_of_max(self, *pos):
        max_value = max([self.__arr[i] for i in pos])
        for i in pos:
            if self.__arr[i] == max_value:
                return i

    def pop_max(self):
        self.__size -= 1
        return self.__arr.pop(0)

    def sort(self):
        for i in reversed(range(len(self.__arr))):
            tmp = self.__arr[i]
            self.__arr[i] = self.__arr[0]
            self.__arr[0] = tmp
            self.__size -= 1
            self.max_heapify(0)
        print self.__arr

def heap_sort(Arr):
    max_heap(Arr).sort()

heap_sort([2,6,3,4,7,5,2,1])
