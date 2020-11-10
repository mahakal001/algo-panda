import random


def insertionSort(arr, n):
    '''
    Loop Invariant :  The subarray [0,i) is always sorted.
    :param arr:
    :param n:
    :return:
    '''
    for i in range(1, n):
        j = i - 1
        tmp = arr[i]
        while j > -1 and arr[j] > tmp:
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = tmp
    return arr


min = 0
max = 100
size = 20

# check 1 : len should be greater than 0
# check 2 : check for (max > min)

arr = random.sample(range(min, max), size)
print(*arr, sep=',')

sortedArr = insertionSort(arr, len(arr))
print(*sortedArr, sep=',')
