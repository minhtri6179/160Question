from tree import BST

root = BST(10)
root.left = BST(5)
root.left.left = BST(2)
root.left.left.left = BST(1)
root.left.right = BST(5)
root.right = BST(15)
root.right.left = BST(13)
root.right.left.right = BST(14)
root.right.right = BST(22)


def closestValue(cur, value):
    minValue = cur.value
    while cur != None:
        if abs(cur.value-value) < abs(value-minValue):
            minValue = cur.value
        if cur.value <= value:
            cur = cur.right
        elif cur.value > value:
            cur = cur.left
        else:
            break
    return minValue


print(f'closestValue: {closestValue(root, 12)}')
