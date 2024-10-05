
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum_list = ListNode()
        temp = sum_list
        total = temp1 = 0 

        while l1 or l2 or temp1:
            total = temp1
            if l1:
                total+=l1.val
                l1 = l1.next
            if l2:
                total+=l2.val
                l2 = l2.next
            num = total % 10 
            temp1 = total // 10
            temp.next = ListNode(num)
            temp = temp.next
        return sum_list.next
