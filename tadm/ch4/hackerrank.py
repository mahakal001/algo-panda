# https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem?h_r=profile
def organizingContainers(container):
    a = []
    b = []

    for i in range(0, len(container)):
        total_balls_in_ith_container = sum(container[i])
        total_balls_of_type_i = 0
        for j in range(0, len(container)):
            total_balls_of_type_i += container[j][i]
        a.append(total_balls_in_ith_container)
        b.append(total_balls_of_type_i)

    a.sort()
    b.sort()

    for p, q in zip(a, b):
        if p != q:
            return "Impossible"

    return "Possible"

# https://www.hackerrank.com/challenges/quicksort3/problem?h_r=profile
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


def quick_sort_recursive(arr, p, r):
    if p < r:
        q = partition_procedure(arr, p, r)
        print(*arr)
        quick_sort_recursive(arr, p, q - 1)
        quick_sort_recursive(arr, q + 1, r)

    return arr

#https://www.hackerrank.com/challenges/mark-and-toys/problem?h_r=profile
def max_toy_recursive(p_rem, k_rem):
    if len(p_rem) == 0 or k_rem < p_rem[0]:
        return 0
    return 1 + max_toy_recursive(p_rem[1:], k_rem - p_rem[0])

def maximumToys(prices, k):
    prices.sort()
    # recursive procedure
    # return max_toy_recursive(prices, k)

    # iterative procedure
    k_rem = k
    i = 0
    while i < len(prices) and k_rem >= prices[i]:
        k_rem -= prices[i]
        i += 1