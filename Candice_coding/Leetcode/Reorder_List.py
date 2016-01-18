# Given a singly linked list L: L0->L1->...->Ln-1->Ln,
# reorder it to: L0->Ln->L1->Ln-1->L2->Ln-2->...
# 
# You must do this in-place without altering the nodes' values.
# 
# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __repr__(self):
        return '({})'.format(self.val)

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head: return
        # Find the mid point
        # Reverse the right part
        # Integrate the two parts
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow is the dummy head of the right part
        rightHead = slow.next
        if not rightHead:
            return head
        right = rightHead.next
        while right:
            rightHead.next = right.next
            right.next = slow.next
            slow.next = right
            right = rightHead.next
        h = head
        while slow.next:
            tmp = slow.next
            slow.next = slow.next.next
            tmp.next = h.next
            h.next = tmp
            h = tmp.next
        return head


if __name__ == '__main__':
    valueList = [1,2,3,4,5,6,7]
    nodeList = []
    for value in valueList:
        nodeList.append(ListNode(value))
    for i in xrange(len(nodeList)-1):
        nodeList[i].next = nodeList[i+1]
    head = nodeList[0]
    newHead = Solution().reorderList(head)
    while newHead:
        print '{} ->'.format(newHead),
        newHead = newHead.next