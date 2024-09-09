# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        dic = {}
        temp = head 
        while temp:
            if temp.val in dic:
                dic[temp.val] += 1
            else:
                dic[temp.val] = 1
            temp = temp.next
        ans = ListNode()
        current = ans
        while head:
            if dic[head.val] > 1:
                head = head.next
                continue
            else:
                current.next = new_node = ListNode(head.val)
                current = current.next
            head = head.next
        return ans.next