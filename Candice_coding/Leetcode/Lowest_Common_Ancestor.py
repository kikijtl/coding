'''Given two tree nodes, find the lowest common ancestor.
Every tree node has a parent.
Very similar to Intersection Linked list in Leetcode.'''

from BinaryTree import *
def lowestAncestor(node1, node2):
    h1 = 0
    h2 = 0
    p = node1
    q = node2
    while p:
        h1 += 1
        p = p.parent
    while q:
        h2 += 1
        q = q.parent
    p = node1
    q = node2
    if h1 >= h2:
        for i in range(h1-h2):
            p = p.parent
    else:
        for i in range(h2-h1):
            q = q.parent
    while p != q:
        p = p.parent
        q = q.parent
    return p

'''if tree node doesn't have the attribute of parent, we can do as follows'''
def LCA(root, node1, node2):
    if not root:
        return None
    if root == node1 or root == node2:
        return root
    left = LCA(root.left, node1, node2)
    right = LCA(root.right, node1, node2)
    if left and right:
        return root
    if not left:
        return right
    if not right:
        return left

'''if the tree is a binary search tree.'''
def LCA_BST(root, node1, node2):
    if node1.data < root.data < node2.data or node2.data < root.data < node1.data:
        return root
    if node1.data < root.data and node2.data < root.data:
        return LCA_BST(root.left, node1, node2)
    else:
        return LCA_BST(root.right, node1, node2)

if __name__ == '__main__':
    ''' The tree is:
                     1
                   /   \ 
                 2      3
                / \    / \
               4   5  8   9
                  / \    / \
                 6   7  10  11
                /
               12
    '''
    t=BinaryTree()
    pre_order=[1,2,4,5,6,12,7,3,8,9,10,11]
    in_order=[4,2,12,6,5,7,1,8,3,10,9,11]
    post_order=[4,12,6,7,5,2,8,10,11,9,3,1]
    root=t.create_tree(post_order, in_order, indicator='post_in')
    test_cases = [(root.left.left,root.left.right.right), 
                  (root.left.right,root.left.right.left.left),
                  (root.left.left, root.right.right.left)]
    '''test cases are (4,7), (5,12), (4,8)'''
    for test in test_cases:
        node1 = test[0]
        node2 = test[1]
        print lowestAncestor(node1, node2).data, LCA(root, node1, node2).data
    bst = BinaryTree()
    pre_bst = [90,50,20,70,60,80,100,110]
    in_bst = [20,50,60,70,80,90,100,110]
    root_bst = bst.create_tree_pre_in(pre_bst, in_bst)
    test_bst = [(root_bst.left.left, root_bst.left.right.right),
                (root_bst.left.right.left, root_bst.right),
                (root_bst.left.right.right, root_bst.left.right.left)]
    for test in test_bst:
        node1 = test[0]
        node2 = test[1]
        print LCA_BST(root_bst, node1, node2).data