# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        pev = None
        while head:
            temp = head.next
            head.next = pev
            pev = head
            head = temp
        return pev
# head = 1->2->3
# lần 1:
# temp = 2->3
# head = 1->None
# pev  = 1->None
# head = 2->3
# lần 2:
# temp = 3
# head = 2->1
# pev = 2->1
# head = 3
# lần 2 
# temp = None
# head = 3->2->1
# pev = 3->2->1
# head = None 