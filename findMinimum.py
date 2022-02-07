import numpy as np


def minimum(arr):
    '''A minimum funding function'''
    minN = 10000  # a big number
    minInd = 0
    for i in range(0, arr.shape[0]):
        if (arr[i] < minN):
            minN = arr[i]
            minInd = i
    return (minN, minInd)


if __name__ == '__main__':
    arr = np.random.random((100))
    print(minimum(arr))
