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
        
    def reverse(self):
        dummy = ListNode(-1)
        dummy.next = None
        p = self.head
        while p:
            q = p.next
            p.next = dummy.next
            dummy.next = p
            p = q
        self.head = dummy.next
        
    def check_circle(self):
        p = self.head
        q = self.head
        while q and q.next:
            q = q.next.next
            p = p.next
            if p == q:
                p = self.head
                while p != q:
                    q = q.next
                    p = p.next
                return True, p
        return False
    
    def add_circle(self, pos):
        p = self.head
        for i in range(pos):
            p = p.next
        q = self.head
        while q.next:
            q = q.next
        q.next = p
        
 
    
if __name__=='__main__':
    #node = ListNode(3)
    #print node.val, node.next
    my_list = LinkList()
    list_data = [3,7,5,1,4,6]
    for i, data in enumerate(list_data):
        my_list.add_node(data, i)
    my_list.print_list()
    my_list.add_circle(2)
    print my_list.check_circle()
    '''
    my_list.reverse()
    my_list.print_list()
    '''
    '''
    print len(my_list)
    
    my_list.del_node(2)
    my_list.print_list()
    print len(my_list)

    '''
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
    
    
    
    