def first(arr, n, k):
    min = 0
    max = n - 1

    while min <= max:
        mid = (min + max) // 2
        if (mid == 0 or arr[mid-1] < k) and arr[mid] == k:
            return mid
        elif arr[mid] < k:
            min = mid + 1
        else:
            max = mid - 1

    return -1

def last(arr, n, k):
    min = 0
    max = n - 1

    while min <= max:
        mid = (min + max) // 2
        if (mid == n-1 or arr[mid+1] > k) and arr[mid] == k:
            return mid
        elif arr[mid] > k:
            max = mid - 1
        else:
            min = mid + 1

    return -1

# TC : O(log n)
arr = [1, 2, 3, 4, 4, 4, 5, 6]
k = -1
f = first(arr, len(arr), k)
if f == -1:
    print("element does not exist")
else:
    l = last(arr, len(arr), k)
    print(" The occurence of given item is: ", l - f + 1)
