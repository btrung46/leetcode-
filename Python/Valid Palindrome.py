class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        start = 0
        end = len(s)-1
        for i in range(0,len(s)):
            if s[start].isalnum() == False:
                start+=1
                continue
            if s[end].isalnum() == False:
                end-=1
                continue
            if s[start] != s[end]:
                return False
            else:
                start += 1
                end  -= 1
        return True

                
    
        
        
