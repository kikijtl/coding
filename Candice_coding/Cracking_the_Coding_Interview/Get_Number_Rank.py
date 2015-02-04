'''Imagine you are reading in a stream of integers. Periodically, you wish to be able to 
look up the rank of a number x(the number of values less than or equal to x). Implement 
the data structures and algorithms to support these operations. That is, implement 
the method track(int x), which is called when each number is generated, 
and the method getRankOfNumber(int x), which returns the umber of values 
less than or equal to x(not including x itself).'''

class rankNode():
    def __init__(self, x):
        self.left_sz = 0
        self.left = None
        self.right = None
        self.val = x
        
class rank():
    def __init__(self):
        self.root = None
    
    def track(self, x):
        if not self.root:
            self.root = rankNode(x)
        else:
            self.insert(self.root, x)
    
    def insert(self, root, x):
        if x <= root.val:
            if not root.left:
                root.left = rankNode(x)
            else:
                self.insert(root.left, x)
            root.left_sz += 1
        else:
            if not root.right:
                root.right = rankNode(x)
            else:
                self.insert(root.right, x)
    
    def getRoot(self):
        return self.root
    
    def getRank(self, root, x):
        if x == root.val:
            return root.left_sz
        if x < root.val:
            if not root.left:
                return -1
            else:
                return self.getRank(root.left, x)
        else:
            if not root.right:
                return -1
            else:
                right_rank = self.getRank(root.right, x)
                if right_rank == -1:
                    return -1
                return root.left_sz+1+right_rank


if __name__ == '__main__':
    A = [2,3,1,5,6,7,9,5]
    myRank = rank()
    for num in A:
        myRank.track(num)
    myRoot = myRank.getRoot()
    x = 5
    print myRank.getRank(myRoot, x)
    