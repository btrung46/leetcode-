# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head==None or head.next==None or k==0:
            return head
        p = head
        length = 1
        while p.next!=None:
            p = p.next
            length += 1
        k = k % length
        if k==0:
            return head
        count = length - k
        q = head
        while count > 1:
            q = q.next
            count -= 1
        r = q.next
        q.next = None
        p.next = head
        return r