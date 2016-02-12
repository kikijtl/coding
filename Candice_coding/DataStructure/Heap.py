from copy import deepcopy

class Heap:
    def __init__(self):
        self.heap = []
        
    def heapify(self, i):
        n = len(self.heap)
        if 2*i+1 > n-1:
            return
        if self.heap[i] < self.heap[2*i+1]:
            if 2*i+2 > n-1 or self.heap[i] < self.heap[2*i+2]:
                return
            self.heap[i],self.heap[2*i+2] = self.heap[2*i+2],self.heap[i]
            self.heapify(2*i+2)
        else:
            if 2*i+2 < n and self.heap[2*i+2] < self.heap[2*i+1]:
                self.heap[i],self.heap[2*i+2] = self.heap[2*i+2],self.heap[i]
                self.heapify(2*i+2) 
            else:
                self.heap[i],self.heap[2*i+1] = self.heap[2*i+1],self.heap[i]
                self.heapify(2*i+1)
        
    def build_heap(self, seq):
        self.heap = deepcopy(seq)
        n = len(self.heap)
        m = n/2 - 1
        for i in range(m, -1, -1):
            self.heapify(i)
            
    def print_heap(self):
        print self.heap
        
    def extract_node(self):
        if not self.heap:
            return
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        ret = self.heap.pop()
        self.heapify(0)
        return ret
        
    def add_node(self, x):
        self.heap.append(x)
        #self.sift_up(len(self.heap)-1)
        p = len(self.heap)-1
        while p-1 >= 0 and self.heap[(p-1)/2] > x:
            self.heap[(p-1)/2], self.heap[p] = self.heap[p], self.heap[(p-1)/2]
            p = (p-1)/2
        
        
    def sift_up(self, j):
        p = (j-1)/2
        if p < 0 or self.heap[p] <= self.heap[j]:
            return
        self.heap[p], self.heap[j] = self.heap[j], self.heap[p]
        self.sift_up(p)
        
    def get_n_largest(self, n, seq):
        for i in range(n):
            self.add_node(seq[i])
        for i in range(n, len(seq)):
            if seq[i] > self.heap[0]:
                self.heap[0] = seq[i]
                self.heapify(0)
        return self.heap[:n]   
    
    def heap_sort(self):
        ret = []
        while self.heap:
            ret.append(self.extract_node())
        return ret
        
        
if __name__ == '__main__':
    seq = [37,50,21,34,15,16,10000,32,43,6,7,345,14]
    hp = Heap()
    '''
    hp.build_heap(seq)
    
    hp.print_heap()
    print hp.heap_sort()
    
    for num in seq:
        hp.add_node(num)
        hp.print_heap()
    '''
    print hp.get_n_largest(3, seq)