
''' A stack class that will provide APIs for inserting, deleting elements in LIFO manner
'''

class Stack(object):
    def __init__(self):
        self.max_size = 10
        self.top = 0
        self.arr = [None]*self.max_size
        
    def __repr__(self):
        return '%s(%r)' %(self.__class__.__name__, self.arr)
        
    ''' push element into stack
        @param element: element that will be pushed into the stack
        @return: 0: success
                 1: error
    '''
    def push(self, element):
        if (self.top >= self.max_size):
            return 'stack is full'
        self.arr[self.top] = element
        self.top += 1
        return 'success'
    
    ''' pop the top element from stack
        @return: the popped element or None for empty stack
    '''
    def pop(self):
        if (self.top == 0):
            return None
        tmp = self.arr[self.top-1]
        self.top -= 1 
        return tmp
    
    
    ''' get the top element in stack
    '''
    def get_top(self):
        if (self.top == 0):
            return None
        return self.arr[self.top-1]
    
    
    ''' check if stack is empty
    '''
    def is_empty(self):
        return self.top == 0
    


if __name__=='__main__':
    my_stack = Stack()
    stack_data = [2,3,5,7,1,8,9,10,21,40,50]
    for data in stack_data:
        print my_stack.push(data)
    
    while not my_stack.is_empty():
        print my_stack.pop()
    
    print my_stack.get_top()