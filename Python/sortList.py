
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        sort_list =[]
        while(head):
            sort_list.append(head.val)
            head = head.next
        sort_list.sort()
        ans = ListNode(sort_list[0])
        current = ans
        for i in sort_list[1:]:
            current.next = new_node = ListNode(i)
            current = current.next
            print(current)
        return ans