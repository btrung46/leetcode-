# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        temp = ListNode()
        temp = head
        while (temp):
            if temp.next and temp.next.val == val: 
                temp.next = temp.next.next
                continue
            temp = temp.next
        if head and head.val == val:
            head = head.next
        return head


            
        