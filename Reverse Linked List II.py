# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        ans = head 
        dem = 1
        pev = []
        while ans:
            if dem >= left and dem <= right:
                pev.append(ans.val)
                ans = ans.next
            else:
                ans = ans.next
            dem += 1  
        ans = head 
        dem = 1 
        n = len(pev)
        while ans:
            if dem >= left and dem <= right:
                ans.val = pev[n-1]
                n-=1
            ans = ans.next
            dem += 1 
        return head 
        