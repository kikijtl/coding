class MinStack:
    def __init__(self):
        self.st1 = []
        '''st1 is the original stack'''
        self.st2 = []
        '''st2 is used to store the minimum value'''
    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.st1.append(x)
        if not self.st2 or x <= self.st2[-1]:
            self.st2.append(x)
        '''if x > st2[-1], then x cannot be the minimum,
            because it pops first.'''
        return x
        
    # @return nothing
    def pop(self):
        if self.st1:
            tmp = self.st1.pop()
            if tmp == self.st2[-1]:
                self.st2.pop()

    # @return an integer
    def top(self):
        if self.st1:
            return self.st1[-1]

    # @return an integer
    def getMin(self):
        if self.st2:
            return self.st2[-1]
        
if __name__ == '__main__':
    stack = [2,7,9,3,4,6,5,1,8,9,0]
    mystack = MinStack()
    for each in stack:
        mystack.push(each)
        print 'get min', mystack.getMin()
    print 'push is done'
    while mystack.st1:
        print 'top',mystack.top()
        mystack.pop()
        print 'get min', mystack.getMin()