class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Helper to print a binary tree
def printTree(node, level=0):
    if node is not None:
        printTree(node.right, level + 1)
        print(' ' * 4 * level + '->' + str(node.value))
        printTree(node.left, level + 1)


# Helper to create a BST
def createBst():
    root = TreeNode(13)
    root.left = TreeNode(6)
    root.right = TreeNode(21)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(8)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(24)
    root.right.right.right = TreeNode(26)
    return root


def insertIntoBst(node, value):
    if not node:
        return TreeNode(value)
    if node.value < value:
        node.right = insertIntoBst(node.right, value)
    else:  # node.value > value
        node.left = insertIntoBst(node.left, value)
    return node


def deleteFromBst(root, value):
    def getSmallestValue(root):
        if not root.left:
            return root.value
        return getSmallestValue(root.left)
    if not root:
        return root
    if root.value < value:
        root.right = deleteFromBst(root.right, value)
    elif root.value > value:
        root.left = deleteFromBst(root.left, value)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        new_root_value = getSmallestValue(root.right)
        root.value = new_root_value
        return deleteFromBst(root.right, new_root_value)
    return root


bst = createBst()
printTree(bst, 0)
print('-----------')
insertIntoBst(bst, 22)
printTree(bst, 0)
