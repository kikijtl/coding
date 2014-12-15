''' Implement a binary tree class
'''
from collections import deque
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    #use pre_order and in_order sequence to recursively create the binary tree
    def create_tree(self,seq1, seq2, indicator='pre_in'):
        if indicator == 'pre_in':
            return self.create_tree_pre_in(seq1,seq2)
        elif indicator == 'post_in':
            return self.create_tree_post_in(seq1,seq2)
        else:
            print 'Invalid indicator'
            return 
        
    def create_tree_pre_in(self, pre_order, in_order):
        if len(pre_order)==0:
            return None
        n=TreeNode(pre_order[0])
        pos=in_order.index(pre_order[0])
        n.left=self.create_tree_pre_in(pre_order[1:pos+1],in_order[:pos])
        if n.left!=None:
            n.left.parent=n
        n.right=self.create_tree_pre_in(pre_order[pos+1:], in_order[pos+1:])
        if n.right!=None:
            n.right.parent=n
        self.root=n
        return n
    
    def create_tree_post_in(self, post_order, in_order):
        if len(post_order)==0:
            return None
        l=len(post_order)-1
        n=TreeNode(post_order[l])
        pos=in_order.index(post_order[l])
        n.left=self.create_tree_post_in(post_order[:pos], in_order[:pos])
        if n.left != None:
            n.left.parent = n
        n.right=self.create_tree_post_in(post_order[pos:l], in_order[pos+1:])
        if n.right != None:
            n.right.parent = n
        self.root = n
        return n
    
    def pre_order_traversal_recur(self, r):
        if r:
            print r.data,
            self.pre_order_traversal_recur(r.left)
            self.pre_order_traversal_recur(r.right)
            
    def in_order_traversal_recur(self, r):
        if r:
            self.in_order_traversal_recur(r.left)
            print r.data,
            self.in_order_traversal_recur(r.right)
     
    def post_order_traversal_recur(self, r):
        if r:
            self.post_order_traversal_recur(r.left)
            self.post_order_traversal_recur(r.right)
            print r.data,

    def get_height(self,r):
        if not r:
            return 0
        return max(self.get_height(r.left), self.get_height(r.right))+1
    
    def preorder_traversal_iter(self, r):
        stack = []
        stack.append(r)

        while stack:
            current = stack.pop()
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
            print current.data,
        print

    

    def level_order_traversal(self,r):

        q = deque([])
        q.append(r)
        current_level = 1
        next_level = 0

        while q:
            current = q.popleft()
            current_level -= 1
            if current.left:
                q.append(current.left)
                next_level += 1
            if current.right:
                q.append(current.right)
                next_level += 1
            print current.data,
            if current_level == 0:
                print
                current_level = next_level
                next_level = 0
        print

if __name__=='__main__':
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
    
    t.pre_order_traversal_recur(root)
    print
    t.in_order_traversal_recur(root)
    print
    t.level_order_traversal(root)
    print
    print t.get_height(root)