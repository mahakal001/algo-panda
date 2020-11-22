# https://www.hackerrank.com/challenges/array-left-rotation/
def rotateLeft(d, arr):
    # Write your code here
    if d == len(arr):
        return arr

    # O(1) storage space
    # O(dn) running time, if d is close to n, then O(n^2)
    #
    # for i in range(d):
    #     tmp = arr[0]
    #     for j in range(len(arr)-1):
    #         arr[j] = arr[j+1]
    #     arr[len(arr)-1] = tmp

    # O(n) storage space when d==n
    # O(n) running time because we iterate over the array only twice(constant) in worst case

    tmpArr = arr[:d]
    for i in range(d, n):
        arr[i - d] = arr[i]

    index_from_end = n - d
    for j in range(d):
        arr[index_from_end + j] = tmpArr[j]
    return arr

# https://www.hackerrank.com/challenges/kangaroo/
def kangaroo(x1, v1, x2, v2):
    if x1 == x2 and v1 == v2:
        return "YES"

    if x1 >= x2 and v1 >= v2:
        return "NO"

    if x2 >= x1 and v2 >= v1:
        return "NO"

    if x1 > x2:
        d = (x1 - x2) * (v1 / (v2 - v1))
        jumps = d / v1
    else:
        d = (x2 - x1) * (v2 / (v1 - v2))
        jumps = d / v2

    f, t = math.modf(jumps)

    if t > 0 and f == 0.0:
        return "YES"
    else:
        return "NO"

# https://www.hackerrank.com/challenges/hackerland-radio-transmitters/
def hackerlandRadioTransmitters(x, k):
    # if there  are no house at all, then no need to put and transmitter
    if len(x) == 0:
        return 0

    # if coverage area of transmitter is 0, then we need all the location have the
    # transmitter installed. since we can have mutliple house at the same location
    # so we need to take unique among the given list
    if k == 0:
        return len(set(x))

    # our algorithm need a sorted list
    x.sort()  # O(n*lg(n))

    start_house = x[0]
    cov_area = start_house + k
    n = len(x)

    # a list to store position where towers will be installed
    towers = []

    # In below loop we will make one iteration over the sorted inpput O(n)
    i = 0
    while True:
        while i < n and x[i] <= cov_area:
            i += 1

        towers.append(x[i - 1])
        max_possible_skip = x[i - 1] + k

        while i < n and x[i] <= max_possible_skip:
            i += 1

        if i >= n:
            break

        start_house = x[i]
        cov_area = start_house + k

    return len(towers)