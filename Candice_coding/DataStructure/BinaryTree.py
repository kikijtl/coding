''' Implement a binary tree class
'''

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
    root=t.create_tree(pre_order, in_order)
    
    
    t.pre_order_traversal_recur(root)
    print
    print t.get_height(root)