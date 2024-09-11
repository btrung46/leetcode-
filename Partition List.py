# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        ans = ListNode()
        a = ans
        temp = head 
        while temp:
            if temp.val < x:
                a.next = new_node = ListNode(temp.val)
                a = a.next
            temp = temp.next
        temp = head
        while temp:
            if temp.val >= x:
                a.next = new_node = ListNode(temp.val)
                a = a.next
            temp = temp.next
        return ans.next
                

        
    
        