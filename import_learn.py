from findMinimum import minimum
import numpy as np

arr=np.random.random((100))
sortArr=np.empty(arr.shape)
copArr=np.copy(arr)

for i in range(0,copArr.shape[0]):
    minN,minInd=minimum(copArr)
    sortArr[i]=minN
    copArr[minInd]=1000000

print(sortArr)
