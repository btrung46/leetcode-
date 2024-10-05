
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        if head is None:
            return None
        curr = head
        while curr:
            newNode = Node(curr.val,curr.next)
            curr.next = newNode
            curr = newNode.next
            
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        curr = head 
        new_head = head.next
        new_curr = new_head 
        while curr:
            curr.next = new_curr.next
            curr = curr.next
            if curr:
                new_curr.next = curr.next
                new_curr = new_curr.next
        return new_head
