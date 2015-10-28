from threading import Lock, Thread, currentThread
from sets import Set
from random import randint
import logging

logging.basicConfig(level=logging.INFO, 
                    format='[%(levelname)s] (%(threadName)s) %(message)s')

class IdManager1(object):
    def __init__(self, n):
        self.avail = Set([])
        for i in xrange(1, n+1):
            self.avail.add(i)
        self.unavail = Set([])
        self.maxid = n
        self.lock = Lock()

    def get_id(self):
        '''Returns available id if succeeds, otherwise returns False.'''
        with self.lock:
            if not self.avail:
                logging.error('No available id in the pool')
                return False
            id = self.avail.pop()
            self.unavail.add(id)
            logging.info('Got id {}'.format(id))
            return id
    
    def free_id(self, id):
        '''Returns True if successful, False otherwise.'''
        if id > self.maxid or id < 1:
            logging.error('Id {} is out of range'.format(id))
            return False
        with self.lock:
            if id not in self.unavail:
                logging.error('Id {} is not in use'.format(id))
                return False
            self.unavail.remove(id)
            self.avail.add(id)
            logging.info('Id {} is available now'.format(id))
            return True
    

class IdManager2(object):
    def __init__(self, n):
        self.freeList = LinkedList()
        self.hashmap = [False] * n
        self.maxid = n
        self._CreateFreeList(n)
        self.lock = Lock()
    
    def get_id(self):
        '''Returns available id if succeeds, otherwise returns False.'''
        with self.lock:
            if not self.freeList.head:
                logging.error('No available id in the pool')
                return False
            id = self.freeList.delHead().val
            assert self.hashmap[id-1] == False
            self.hashmap[id-1] = True
            logging.info('Got id {}'.format(id))
            return id
    
    def free_id(self, id):
        '''Returns True if successful, False otherwise.'''
        if id > self.maxid or id < 1:
            logging.error('Id {} is out of range'.format(id))
            return False
        with self.lock:
            if self.hashmap[id-1] == False:
                logging.error('Id {} is not in use'.format(id))
                return False
            self.freeList.addHead(ListNode(id))
            self.hashmap[id-1] = False
            logging.info('Id {} is available now'.format(id))
            return True
            
    def _CreateFreeList(self, n):
        for i in xrange(n, 0, -1):
            self.freeList.addHead(ListNode(i))
        

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
    def __repr__(self):
        return '%s(%r)' %(self.__class__.__name__, self.val)


class LinkedList(object):
    def __init__(self):
        self.head = None
    
    def __repr__(self):
        return '%s(%r)' %(self.__class__.__name__, self.head)
    
    def addHead(self, newHead):
        newHead.next = self.head
        self.head = newHead
        logging.debug('newHead: {}'.format(self.head))
        
    def delHead(self):
        oldHead = self.head
        self.head = self.head.next
        logging.debug('oldHead: {}, newHead: {}'.format(oldHead, self.head))
        return oldHead
    


if __name__ == '__main__':
    n = 10
#     manager = IdManager1(n)
    manager = IdManager2(n)
    threads = []
    thread_num = 30
    result = []
    for i in xrange(thread_num):
        choice = randint(0, 1)
        # The thread will randomly choose to get_id or free_id
        if choice:
            thread = Thread(target=manager.get_id)
            threads.append(thread)
            print '{}: get_id'.format(thread.name)
        else:
            input = randint(0, n*4/3)
            thread = Thread(target=manager.free_id, args=(input,))
            threads.append(thread)
            print '{}: free_id {}'.format(thread.name, input)
    for thread in threads:
        thread.start()
