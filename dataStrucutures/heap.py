
class Heap(object):
    def __init__(self):
        return

    """ 
       The below three functions are based on the observation that a heap is an almost complete binary tree, that is, l
        1. Leaves are either present at the last level or the second last level only,
        2. Before starting filling the nth level,(n-1)th level should be filled completely
        3. Insert from Left to Right
    """
    def parent(self, index):
        return index >> 1

    def left_child(self, index):
        return index << 1

    def right_child(self, index):
        return (index << 1) + 1

    def max_heapify(self, arr, index, heap_size):

        if index not in range(0, len(arr)):
            return

        left = self.left_child(index)
        right = self.right_child(index)

        largest = index
        if left < heap_size and arr[left] > arr[largest]:
            largest = left

        if right < heap_size and arr[right] > arr[largest]:
            largest = right

        if largest != index:
            # swap
            arr[index], arr[largest] = arr[largest], arr[index]
            self.max_heapify(arr, largest, heap_size)

        return

    def build_max_heap(self, arr):

        heap_size = len(arr)
        maxNonLeafIndex = len(arr) >> 1 # len(arr) // 2

        index = maxNonLeafIndex
        while index >= 0:
            self.max_heapify(arr, index, heap_size)
            index -= 1

    def heap_sort(self, arr):

        if len(arr) < 2:
            return arr

        self.build_max_heap(arr)
        heap_size = len(arr)
        arr[0], arr[heap_size-1] = arr[heap_size-1], arr[0]
        heap_size -= 1

        while heap_size > 0:
            self.max_heapify(arr, 0, heap_size)
            arr[0], arr[heap_size - 1] = arr[heap_size - 1], arr[0]
            heap_size -= 1

        return arr

    def extract_max(self, heap):

        if len(heap) == 0:
            return None

        if len(heap) == 1:
            return heap[0]

        max_value = heap[0]
        heap[0] = heap[len(heap) - 1]
        del heap[len(heap) - 1 :]

        self.max_heapify(heap, 0, len(heap))
        return max_value

    def increase_key(self, heap, index, key):

        if key < heap[index] :
            return -1

        heap[index] = key

        while index > 0 and heap[index] > heap[self.parent(index)]:
            heap[index], heap[self.parent(index)] = heap[self.parent(index)], heap[index]
            index = self.parent(index)

        return heap

    def heap_insert(self, heap, key):
        tmp = key - 1
        heap.append(tmp)
        self.increase_key(heap, len(heap)-1, key )







