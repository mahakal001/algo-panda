import random
import sort

min = 0
max = 100
size = 10

# check 1 : len should be greater than 0
# check 2 : check for (max > min)

arr = random.sample(range(min, max), size)

print("Input array : ", arr)
sortedArr = sort.quick_sort_recursive(arr, 0, len(arr)-1)
print("Sorted array: ", sortedArr)
