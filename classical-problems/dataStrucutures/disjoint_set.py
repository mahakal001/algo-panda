class Node(object):

    def __init__(self, label):
        self.label = label
        self.parent = self

    def is_root(self):
        if self.parent == self:
            return True
        return False

    def set_parent(self, parent):
        self.parent = parent
        return


def make_set(label):
    return Node(label)


def find_set(node):
    while node.parent != node:
        node = node.parent
    return node


def union(u, v):
    root1 = find_set(u)
    root2 = find_set(v)

    if root1 == root2:
        return
    root2.parent = root1

    return