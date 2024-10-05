class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp = []
        dic = {
            "{":"}",
            "[":"]",
            "(":")"
        }
        for i in s:
            if i in "{[(":
                temp.append(i)
            else:
                if len(temp) == 0 or dic[temp.pop()] != i:
                    return False
        return len(temp) == 0



        