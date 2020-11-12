from sorting_helpers import merge_procedure

from sorting_helpers import partition_procedure


def selectionSort(arr):
    arrSize = len(arr)
    for i in range(0, arrSize):
        minIndex = i
        for j in range(i + 1, arrSize):
            if arr[j] < arr[minIndex]:
                minIndex = j

        # swap
        tmp = arr[i]
        arr[i] = arr[minIndex]
        arr[minIndex] = tmp

    return arr


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
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp
    return arr


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
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = tmp
    return arr


def countingSort(arr, n, k):
    """

    :param arr: input array
    :param n: Lenght of the array
    :param k: The value of maximum element that can be present in the array
    :return: sorted version of input arr
    """
    # declare a list of size k
    occurenceRecord = [0] * (k + 1)

    # Iterate over the input array to count the occurence of each input value
    for num in arr:
        occurenceRecord[num] += 1

    index = 0
    for i in range(0, k + 1):
        j = occurenceRecord[i]
        while j > 0:
            arr[index] = i
            j -= 1
            index += 1
    return arr

def merge_sort_recursive(arr, p, q):
    """

    :param arr: Array to be sorted
    :param p: Starting index of the sbuarray to be sorted
    :param q:  Last index of the subarray to be sorted
    :return:  sorted subarray arr[p,q)
    """

    if p < q :
        mid = (p+q) // 2

        merge_sort_recursive(arr, p, mid)
        merge_sort_recursive(arr, mid+1 , q)
        print("================= Merging arr[%d, %d] and arr[%d, %d] ===================== "%(p, mid, mid+1, q))
        merge_procedure(arr, p, mid, q)
        print(arr)

    return arr

def quick_sort_recursive(arr, p, r):
    if p < r:
        q = partition_procedure(arr, p, r)
        print(arr,q)
        quick_sort_recursive(arr, p, q-1)
        quick_sort_recursive(arr, q+1, r)

    return arr
