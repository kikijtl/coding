class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        
class HashTable:
    def __init__(self, size):
        self.table = [None]*size
        self.size = size
    
    def _hash_function(self, s):
        hash_val = 0
        for ch in s:
            hash_val  = abs(ord(ch) + (hash_val <<5) - hash_val)
        return hash_val % self.size
    
    def insert(self, key, value):
        mynode = HashNode(key, value)
        idx = self._hash_function(key)
        head = self.table[idx]
        while head:
            if head.key == mynode.key:
                return -1
            head = head.next
        mynode.next = self.table[idx]
        self.table[idx] = mynode
        
    def find(self, key): 
        idx = self._hash_function(key)
        head = self.table[idx]
        while head:
            if head.key == key:
                return head.val
            head = head.next
        return None
    

if __name__ == '__main__':
    mytable = HashTable(10)
    mytable.insert('yifei','vmware')
    #print mytable.insert('yifei','cisco')
    mytable.insert('yuqi','scu')
    mytable.insert('','')
    print mytable.find('yifei')
    print mytable.find('yuqi')
    print mytable.find('')
    
        