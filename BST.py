class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    # Insert a node
    def insert(self, key):
        def _insert(root, key):
            if not root:
                return Node(key)
            if key < root.key:
                root.left = _insert(root.left, key)
            elif key > root.key:
                root.right = _insert(root.right, key)
            return root
        self.root = _insert(self.root, key)

    # Search a node
    def search(self, key):
        def _search(root, key):
            if not root:
                return False
            if root.key == key:
                return True
            elif key < root.key:
                return _search(root.left, key)
            else:
                return _search(root.right, key)
        return _search(self.root, key)

    # Inorder traversal
    def inorder(self):
        result = []
        def _inorder(root):
            if root:
                _inorder(root.left)
                result.append(root.key)
                _inorder(root.right)
        _inorder(self.root)
        return result

    # Display leaf nodes
    def display_leaves(self):
        leaves = []
        def _leaves(root):
            if root:
                if not root.left and not root.right:
                    leaves.append(root.key)
                _leaves(root.left)
                _leaves(root.right)
        _leaves(self.root)
        return leaves

    # Find min node
    def find_min(self):
        current = self.root
        if not current:
            return None
        while current.left:
            current = current.left
        return current.key

    # Find max node
    def find_max(self):
        current = self.root
        if not current:
            return None
        while current.right:
            current = current.right
        return current.key

# Example usage
bst = BST()
for key in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(key)

print("Inorder Traversal:", bst.inorder())
print("Search 40:", bst.search(40))
print("Leaf Nodes:", bst.display_leaves())
print("Min Node:", bst.find_min())
print("Max Node:", bst.find_max())


