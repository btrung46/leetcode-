
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        # """
        if not head:
            return None
        sorted_head = ListNode()
        current = sorted_head
        current.val = head.val
        while head:
            if current.val == head.val:
                head = head.next 
                current.next = head
            else: 
                current = current.next
        print(head)
        print(sorted_head)
        return sorted_head