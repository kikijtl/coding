''' Implement a LinkList class
'''

class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None
    
    def __repr__(self):
        return '%s(%r)' %(self.__class__.__name__, self.val)

class LinkList:
    def __init__(self):
        self.head = None
    
    def __len__(self):
        p = self.head
        cnt = 0
        while p:
            cnt += 1
            p = p.next
        return cnt
        
    
    def add_node(self, x, pos):
        new_node = ListNode(x)
        if pos < 0:
            print 'ERR: pos out of range, check input'
            return
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        p=self.head
        
        for i in range(pos-1):
            p = p.next
            if not p:
                print 'ERR: pos out of range, check input'
                return
        q = p.next
        p.next = new_node
        new_node.next = q
   
    
    def del_node(self, pos):
        if pos < 0:
            print 'ERR: pos out of range, check input'
            return
        if pos == 0:
            tmp = self.head
            self.head = self.head.next
            del tmp
        
        p = self.head
        for i in range(pos-1):
            p = p.next
            if not p.next:
                print 'ERR: pos out of range, check input'
                return
        target_node = p.next
        p.next = target_node.next
        del target_node
    
    def print_list(self):
        p = self.head
        while p:
            print p.val,
            p = p.next
        print

 
    
if __name__=='__main__':
    #node = ListNode(3)
    #print node.val, node.next
    my_list = LinkList()
    list_data = [3,7,5,1]
    for i, data in enumerate(list_data):
        my_list.add_node(data, i)
    my_list.print_list()
    print len(my_list)
    
    my_list.del_node(4)
    my_list.print_list()
    print len(my_list)

    '''
    my_list.add_node(8, 0)
    my_list.print_list()
    
    my_list.add_node(8, 2)
    my_list.print_list()
    
    my_list.add_node(8, 6)
    my_list.print_list()
    
    my_list.add_node(8, 100)
    my_list.print_list()
    
    my_list.add_node(8, -2)
    my_list.print_list()
    '''
    
    
    
    