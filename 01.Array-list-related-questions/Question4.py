#Question - how to find maximum produxt of two integers in the array where all elements are positive

import numpy as np

myArray = np.array([47, 12, 89, 63, 25, 8, 71, 99, 34, 56, 15, 78, 42, 3, 68, 91, 20, 54, 6, 37])

def findMaxPro(array):
    maxProduct = 0
    for i in range(len(array)):
        for j in range(i+1 , len(array)):
            if array[i] * array[j] > maxProduct:
                maxProduct = array[i] * array[j]
                pairs = str(array[i]) +  "," + str(array[j])
    print(maxProduct)
    print(pairs)
            
findMaxPro(myArray)