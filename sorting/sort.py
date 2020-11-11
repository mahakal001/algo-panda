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
                arr[j] = arr[j+1]
                arr[j+1] = tmp
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
            arr[j+1] = arr[j]
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