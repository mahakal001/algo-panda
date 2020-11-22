#https://www.hackerrank.com/challenges/is-binary-search-tree/problem?h_r=profile
""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""


def inorder_traversal(root, arr):
    if root == None:
        return
    inorder_traversal(root.left, arr)
    arr.append(root.data)
    inorder_traversal(root.right, arr)


def check_binary_search_tree_(root):
    arr = []
    inorder_traversal(root, arr)

    for i in range(0, len(arr) - 1):
        if arr[i] >= arr[i + 1]:
            return False
    return True


# https://www.hackerrank.com/challenges/queue-using-two-stacks/problem?h_r=profile
class Queue(object):

    def __init__(self):
        self.stack1 = []
        self.stack1_len = 0
        self.stack2 = []
        self.stack2_len = 0

    def enqueue(self, x):
        self.stack1.append(x)
        self.stack1_len += 1

        return

    def dequeue(self, q_type=2):

        if self.stack2_len == 0:
            while self.stack1_len != 0:
                self.stack2.append(self.stack1.pop())
                self.stack1_len -= 1
                self.stack2_len += 1

        if q_type == 2:
            tmp = self.stack2.pop()
            self.stack2_len -= 1
        else:
            tmp = self.stack2[-1]

        return tmp

    def top(self):
        return self.dequeue(q_type=3)

# https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    if head == None or head.next == None:
        return 0

    p = head
    q = head

    while p and q and q.next:

        p = p.next
        q = q.next.next

        if p == q:
            return 1
    return 0