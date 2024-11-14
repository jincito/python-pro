# Tree traversals

def pre_order(root):
    if not root:
        return
    print(root.val)
    pre_order(root.left)
    pre_order(root.right)


def post_order(root):
    if not root:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.val)


def in_order(root):
    if not root:
        return
    in_order(root.left)
    print(root.val)
    in_order(root.right)
