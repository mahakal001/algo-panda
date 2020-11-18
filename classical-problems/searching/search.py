def linear_search(arr, n, k):
    """
    :param arr: The array to search
    :param n:  Length of the array
    :param k: The number k to search for
    :return:  -1 if k is not present in the array else index of the location of k
    """
    for index in range(0, n):
        if arr[index] == k:
            return index
    return -1


def binary_search_recursive(arr, min, max, k):
    """
    :param arr: sorted array
    :param n:  Length of the array
    :param k: The number k to search for
    :return:  -1 if k is not present in the array else index of the location of k
    """
    if min > max:
        return -1;

    mid = (min + max) // 2

    if arr[mid] > k:
        return binary_search_recursive(arr, min, mid - 1, k)
    elif arr[mid] < k:
        return binary_search_recursive(arr, mid + 1, max, k)
    else:
        return mid


def binary_search_iterative(arr, n, k):
    """
    :param arr: sorted array
    :param n:  Length of the array
    :param k: The number k to search for
    :return:  -1 if k is not present in the array else index of the location of k
    """
    min = 0
    max = len(arr) - 1

    while min <= max:
        mid = (min + max) // 2
        if arr[mid] < k:
            min = mid + 1
        elif arr[mid] > k:
            max = mid - 1
        else:
            return mid

    return -1
