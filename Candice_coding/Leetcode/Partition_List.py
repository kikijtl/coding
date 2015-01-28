'''Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
def partition(head, x):
    if head == None:
        return
    d = ListNode(-1)
    d.next = head
    p = d
    q = p.next
    while q and q.val < x:
        p = p.next
        q = q.next
    i = q
    # the existence of i
    while i and i.next:
        j = i.next
        if j.val >= x:
            i = i.next
            continue
        i.next = j.next
        j.next = q
        p.next = j
        p = j
    return d.next

