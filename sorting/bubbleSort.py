import random


def bubbleSort(arr, n):
    '''
    Loop Invariant :  At the end of ith iteration where i belongs to [0,n), the subarray [n - i, n) is already sorted
    :param arr:
    :param n:
    :return:
    '''

    for i in range(0, n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
    return arr


min = 0
max = 100
size = 20

# check 1 : len should be greater than 0
# check 2 : check for (max > min)

arr = random.sample(range(min, max), size)
print(*arr, sep=',')

sortedArr = bubbleSort(arr, len(arr))
print(*sortedArr, sep=',')
