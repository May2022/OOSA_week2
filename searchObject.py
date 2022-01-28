import numpy as np
from sys import exit


class dataSorter(object):
    '''A class to hold data and provide examples of search algorithms'''

    def __init__(self, numb):
        '''Class initialiser'''
        self.numb = numb
        self.arr = np.random.random((numb))
        self.sortArr = 0

    def sortArray(self):
        '''Sort an array, using a simple sort method'''
        # preserve original array by copying
        copArr = np.copy(self.arr)
        # create workspace
        self.sortArr = np.empty(self.arr.shape)
        # sort the array
        for i in range(0, copArr.shape[0]):
            minN, minInd = self.findMin(copArr)
            self.sortArr[i] = minN
            copArr[minInd] = 1000000
        return self.sortArr

    def findMin(self, arr):
        '''Find a minimum, needed for soret'''
        minN = 10000  # a big number
        minInd = 0
        for i in range(0, arr.shape[0]):
            if (arr[i] < minN):
                minN = arr[i]
                minInd = i
        return (minN, minInd)
        print("Could not complete function. Needs finishing.")
        print(" Exiting program now")
        exit()

    def binary_sort(self, threshold_vale, left, right):
        if left >= right:
            return -1
        mid = (left + right) // 2
        midpoint_value = self.sortArr[mid]
        if midpoint_value < threshold_vale:
            return self.binary_sort(threshold_vale, mid + 1, right)
        elif midpoint_value > threshold_vale:
            return self.binary_sort(threshold_vale, left, mid)
        else:
            return mid


if __name__ == '__main__':
    aa = dataSorter(100)
    aa.sortArray()
    print(aa.sortArr)
    print(aa.binary_sort(0.9, ))
