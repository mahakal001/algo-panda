import random

import sort

min = 0
max = 100
size = 5

# check 1 : len should be greater than 0
# check 2 : check for (max > min)

arr = random.sample(range(min, max), size)
print(*arr, sep=',')

sortedArr = sort.countingSort(arr, len(arr), max-1)
print(*sortedArr, sep=',')
