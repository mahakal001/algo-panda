MAX = 9999


def merge_procedure(arr, p, mid, q):
    """
    Merge two sorted subarray into each other

    :param arr: arr which contains subarray to be merged
    :param p:  arr[p:mid+1] -> first sorted subarray
    :param mid:
    :param q: arr[mid+1:q) -> second sorted subarray
    :return:  arr[p,q) sorted
    """
    arr1 = arr[p:mid + 1]
    arr2 = arr[mid + 1:q + 1]

    arr1.append(MAX)
    arr2.append(MAX)

    i = 0
    j = 0

    for k in range(p, q + 1):
        if arr1[i] <= arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1

    return arr


def partition_procedure(arr, p, r):
    """

    :param arr: Array of numbers
    :param p: starting index
    :param r: Last Index
    :return: index of the location where pivot has been placed
    After run of this function, one element called pivot is at its right position
    according to sorted sequence
    """
    i = p - 1
    pivot = arr[r]

    for j in range(p, r + 1):
        if arr[j] <= pivot:
            i += 1
            # swap
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp

    return i
