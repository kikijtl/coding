'''Implement a queue using two stacks.'''

class Queue:
    def __init__(self):
        self.max_size = 10
        self.front = 0
        self.end = 0
        self.arr = [None]*self.max_size
        self.tmp = []
        
    def __repr__(self):
        return '%s(%r)' %(self.__class__.__name__, self.arr)
    
    def enqueue(self, element):
        if (self.end - self.front) >= self.max_size:
            print 'queue is full'
            return 1
        self.arr[self.end] = element
        self.end += 1
        return 0
                
    def dequeue(self):
        if self.end == self.front:
            print 'queue is empty'
            return None
        if not self.tmp:
            while self.arr:
                self.tmp.append(self.arr.pop())
        self.front += 1
        return self.tmp.pop()
    
    def is_empty(self):
        return self.end == self.front
    
if __name__ == '__main__':
    my_queue = Queue()
    queue_data = [1,2,3,4,5,6,7,8,9,10,11]
    
    for data in queue_data:
        my_queue.enqueue(data)
    while not my_queue.is_empty():
        print my_queue.dequeue()
    
    print my_queue
    
     
    from collections import deque
    
    
    
    q = deque([40,50,60])
    for data in queue_data:
        q.append(data)
    while q:
        q.popleft()
        print q
        