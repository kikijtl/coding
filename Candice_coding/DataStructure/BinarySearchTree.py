'''Implement a binary search tree class'''
from BinaryTree import *
class BinarySearchTree(BinaryTree):
    def create_tree(self, seq):
        self.root = self.sortedArrayToBST(seq)
        return self.root
    
    def sortedArrayToBST(self, num):
        if not num:
            return None
        m = len(num)/2
        r = TreeNode(num[m])
        r.left = self.sortedArrayToBST(num[:m])
        r.right = self.sortedArrayToBST(num[m+1:])
        return r
    
    def find_node(self, root, x):
        if not root:
            return None
        if root.data == x:
            return root
        if x < root.data:
            return self.find_node(root.left, x)
        else:
            return self.find_node(root.right, x)
    
    def add_node(self, root, node):
        if node.data < root.data:
            if not root.left:
                root.left = node
                node.parent = root
                return
            else:
                self.add_node(root.left, node)
        else:
            if not root.right:
                root.right = node
                node.parent = root
                return
            else:
                self.add_node(root.right, node)
                
    def del_node(self, root, val):
        if root.data < val:
            root.right = self.del_node(root.right, val)
            return root
        if root.data > val:
            root.left = self.del_node(root.left, val)
            return root
        if root.data == val:
            if not root.left and not root.right:
                del root
                return
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            target = self.get_sub_min(root.right)
            '''exchange the min value of the right subtree and root.data'''
            '''or we can exchange it with the max value of the left subtree.'''
            root.data = target.data
            root.right = self.del_node(root.right, target.data)
            '''if we del target, python just del the connection between target and the node.'''
            return root
        
    def get_sub_min(self, root):
        if not root:
            return None
        while root.left:
            root = root.left
        return root
        
        
if __name__ == '__main__':
    seq = [20,50,60,70,80,90,100,110]
    bst = BinarySearchTree()
    root = bst.create_tree(seq)
    '''
    print root.data
    bst.in_order_traversal_recur(root)
    print
    bst.level_order_traversal(root)
    '''
    '''
    x = 10
    print bst.find_node(root, x)
    '''
    '''
    node = TreeNode(65)
    bst.add_node(root, node)
    bst.level_order_traversal(root)
    '''
    del_case = [20, 100, 80]
    for val in del_case:
        bst.del_node(root, val)
        bst.level_order_traversal(root)
        print
    
        
    