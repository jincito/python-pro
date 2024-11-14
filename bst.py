class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# Helper to print a binary tree.
def printBinaryTree(node, level=0):
    if node is not None:
        printBinaryTree(node.right, level + 1)
        print(' ' * 4 * level + '-> ' + str(node.val))
        printBinaryTree(node.left, level + 1)


root = TreeNode(50)
root.left = TreeNode(30)
root.right = TreeNode(70)
root.left.left = TreeNode(20)
root.left.right = TreeNode(40)
root.right.left = TreeNode(60)
root.right.right = TreeNode(80)
print("Printing binary tree:")
printBinaryTree(root)
print("\n")


# Traversing Binary Trees

def preorder(root):
    if not root:
        print("\t\tfound None")
        return
    print(f"\tAt node {root.val}...")
    print(root.val)
    print(f"\tGoing left from {root.val}...")
    preorder(root.left)
    print(f"\tGoing right from {root.val}...")
    preorder(root.right)
    print(f"\tDone with node {root.val}")


print("preorder traversal")
preorder(root)
print("\n")


def postorder(root):
    if not root:
        print("\t\tfound None")
        return
    print(f"\tAt node {root.val}...")
    print(f"\tGoing left from {root.val}...")
    preorder(root.left)
    print(f"\tGoing right from {root.val}...")
    preorder(root.right)
    print(root.val)
    print(f"\tDone with node {root.val}")


print("postorder traversal")
preorder(root)
print("\n")


def inorder(root):
    if not root:
        print("\t\tfound None")
        return
    print(f"\tAt node {root.val}...")
    print(f"\tGoing left from {root.val}...")
    inorder(root.left)
    print(root.val)
    print(f"\tGoing right from {root.val}...")
    inorder(root.right)
    print(f"\tDone with node {root.val}")


print("inorder traversal")
inorder(root)
print("\n")


def isUniValue(root, value):
    if not root:  # base case
        return True
    if root.val != value:
        return False
    left = isUniValue(root.left, value)
    if not left:
        return False
    return isUniValue(root.right, value)


# # Helper to create a BST
# def createBst():
#     root = TreeNode(13)
#     root.left = TreeNode(6)
#     root.right = TreeNode(21)
#     root.left.left = TreeNode(4)
#     root.left.right = TreeNode(8)
#     root.right.left = TreeNode(15)
#     root.right.right = TreeNode(24)
#     root.right.right.right = TreeNode(26)
#     return root


# def insertIntoBst(node, value):
#     if not node:
#         return TreeNode(value)
#     if node.value < value:
#         node.right = insertIntoBst(node.right, value)
#     else:  # node.value > value
#         node.left = insertIntoBst(node.left, value)
#     return node


# def deleteFromBst(root, value):
#     def getSmallestValue(root):
#         if not root.left:
#             return root.value
#         return getSmallestValue(root.left)
#     if not root:
#         return root
#     if root.value < value:
#         root.right = deleteFromBst(root.right, value)
#     elif root.value > value:
#         root.left = deleteFromBst(root.left, value)
#     else:
#         if not root.left:
#             return root.right
#         elif not root.right:
#             return root.left
#         new_root_value = getSmallestValue(root.right)
#         root.value = new_root_value
#         return deleteFromBst(root.right, new_root_value)
#     return root


# # Searching in a BST
# # Input:
# #  - root: current TreeNode or None
# #  - key: target value to be searched for
# # Output: the TreeNode with the target value or None if the node doesn't exist
# def search(root, key):
#     if not root:
#         print(f"Node is empty - did not find target: {key}. Returning None.")
#         return None
#     print(f"At node with value: {root.val}")
#     if root.val == key:
#         print(f"\t...found node with target: {key}. Returning node.")
#         return root
#     elif root.val > key:
#         print(f"\t... {root.val} > target {key}. Moving left...")
#         return search(root.left, key)
#     else:
#         print(f"\t... {root.val} < target {key}. Moving right...")
#         return search(root.right, key)


# # Example search
# target = 40
# print(f"Searching for target: {target}")
# found_node = search(root, target)
# if found_node:
#     print(f"Target {target} found in the tree.\n")
# else:
#     print(f"Target {target} not found in the tree.\n")
