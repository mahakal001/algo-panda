import random

def selectionSort(arr):
    arrSize = len(arr)
    for i in range(0, arrSize):
        minIndex = i
        for j in range(i+1, arrSize):
            if arr[j] < arr[minIndex]:
                minIndex = j

        # swap
        tmp = arr[i]
        arr[i] = arr[minIndex]
        arr[minIndex] = tmp

    return arr


min = 0
max = 100
size = 20

# check 1 : len should be greater than 0
# check 2 : check for (max > min)

arr = random.sample(range(min, max), size)
print(*arr, sep=',')

sortedArr = selectionSort(arr)
print(*sortedArr, sep=',')

