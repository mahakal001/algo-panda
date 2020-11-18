import random
from dataStrucutures import heap

min = 0
max = 100
size = 10

# check 1 : len should be greater than 0
# check 2 : check for (max > min)

arr = random.sample(range(min, max), size)

print("Input array : ", arr)
maxHeap = heap.Heap()
sortedArr = maxHeap.heap_sort(arr)
print("Sorted array: ", sortedArr)