class Node:
    """A node in a binary tree."""
    def __init__(self, value,left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    """A binary tree data structure."""
    def __init__(self, root_value=None):
        self.root = Node(root_value) if root_value is not None else None

    def insert_left(self, current_node, value):
        """Insert a node as the left child of the current node."""
        if current_node.left is None:
            current_node.left = Node(value)
        else:
            new_node = Node(value)
            new_node.left = current_node.left
            current_node.left = new_node

    def insert_right(self, current_node, value):
        """Insert a node as the right child of the current node."""
        if current_node.right is None:
            current_node.right = Node(value)
        else:
            new_node = Node(value)
            new_node.right = current_node.right
            current_node.right = new_node

    def preorder_traversal(self, start,traversal):
        """Traverse the tree in preorder (root, left, right)."""
        if start:
            traversal += (str(start.value) + " ")
            traversal = self.preorder_traversal(start.left,traversal)
            traversal = self.preorder_traversal(start.right,traversal)
        return traversal    

    def inorder_traversal(self, start,traversal):
        """Traverse the tree in inorder (left, root, right)."""
        if start:
            traversal = self.inorder_traversal(start.left,traversal)
            traversal += (str(start.value) + " ")
            traversal = self.inorder_traversal(start.right,traversal)
        return traversal    

    def postorder_traversal(self, start,traversal):
        """Traverse the tree in postorder (left, right, root)."""
        if start:
            traversal = self.postorder_traversal(start.left,traversal)
            traversal = self.postorder_traversal(start.right,traversal)
            traversal += (str(start.value) + " ")
        return traversal       


    def search(self, root, key):
        if root is None:
            return None

        if root.value == key:
            return root

        result = self.search(root.left, key)

        if result is not None:
            return result

        return self.search(root.right, key)
    
    def delete_node(self, root, key):
        if root is None:
            return None

        queue = [root]
        target = None
        deepest = None
        deepest_parent = None

        while queue:
            current = queue.pop(0)

            if current.value == key and target is None:
                target = current

            if current.left:
                deepest_parent = current
                queue.append(current.left)

            if current.right:
                deepest_parent = current
                queue.append(current.right)

            deepest = current

        if target is None:
            return root

        if deepest is root:
            return None

        target.value = deepest.value

        if deepest_parent.right is deepest:
            deepest_parent.right = None
        else:
            deepest_parent.left = None

        return root

    def get_tree_data(self, root):
        if root is None:
            return None

        return {
            'value': root.value,
            'left': self.get_tree_data(root.left),
            'right': self.get_tree_data(root.right)
        }