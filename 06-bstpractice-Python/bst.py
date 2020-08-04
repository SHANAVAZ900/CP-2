class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.new_insert(self.root, new_val)

    def new_insert(self, root, new_val):
        # recursive helper function for inserting
        if root:
            if root.value > new_val:
                if root.left is not None:
                    self.new_insert(root.left, new_val)
                else:
                    root.left = Node(new_val)
            elif root.value < new_val:
                if root.right is not None:
                    self.new_insert(root.right, new_val)
                else:
                    root.right = Node(new_val)
        else:
            root = Node(new_val)

    def printSelf(self):
        self.new_peint(self.root)

    def new_peint(self, root):
        # recursive iterative dunction for print
        if root is None:
            return
        print(" ", root.value)
        self.new_peint(root.left)
        self.new_peint(root.right)

    def search(self, find_val):
        if self.root and isinstance(find_val, int):
            root = self.new_search(self.root, find_val)
            f = True if root else False
            print(f)
            return True if root else False
        return False

    def new_search(self, root, find_val):
        # recursive iterative function for searching
        if root is None or root.value == find_val:
            print("in middle")
            return root
        if root.value > find_val:
            print("in left")
            return self.new_search(root.left, find_val)
        if root.value < find_val:
            print("in right")
            return self.new_search(root.right, find_val)
