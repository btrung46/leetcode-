# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
       
        dummy = ListNode(0,head)
        left = dummy
        right = head
        while(n>0):
            right = right.next
            n-=1
       
        while right:
            left=left.next
            right=right.next
        
        left.next=left.next.next
        return dummy.next
    
"""
head = 1->2->3->4->5->6
n = 2 

dummy = 0->1->2->3->4->5->6
left = 0->1->2->3->4->5->6
right = 1->2->3->4->5->6

lần 1:
right = 2->3->4->5->6
n = 1
lần 2:
right = 3->4->5->6
n = 0


lần 1:
left = 1->2->3->4->5->6
right = 4->5->6
lần 2: 
left = 2->3->4->5->6
right = 5->6
lần 3:
left = 3->4->5->6
right = 6
lần 4:
left = 4->5->6
right = None

left = 4->6

dummy.next  = 1->2->3->4->6

"""