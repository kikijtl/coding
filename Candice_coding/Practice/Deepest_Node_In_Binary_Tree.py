# Write a function to find the deepest node in a binary tree AND its depth.
# How would you test this code?

from BinaryTree import BinaryTree
def findDeepestNode(root):
    if not root:
        return [None, 0]
    if not root.left and not root.right:
        return [root, 1]
    left = findDeepestNode(root.left)
    right = findDeepestNode(root.right)
    left[1] += 1
    right[1] += 1
    if left[1] < right[1]:
        return right
    else:
        return left


if __name__ == '__main__':
#     The tree is:
#                      1
#                    /   \ 
#                  2      3
#                 / \    / \
#                4   5  8   9
#                   / \    / \
#                  6   7  10  11
#                 /
#                12
    t=BinaryTree()
    pre_order=[1,2,4,5,6,12,7,3,8,9,10,11]
    in_order=[4,2,12,6,5,7,1,8,3,10,9,11]
    post_order=[4,12,6,7,5,2,8,10,11,9,3,1]
    root=t.create_tree(post_order, in_order, indicator='post_in')
    print findDeepestNode(root)
