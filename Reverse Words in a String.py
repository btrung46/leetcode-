class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        b = s.split(" ")
        i = 0
        while(i<len(b)):
            if b[i] == '':
                b.remove(b[i])
                i-=1
            i+=1
        ans = ""
        for i in range(len(b)-1,-1,-1):
            ans += b[i]
            print(i)
            if i == 0:
                break
            ans += ' '
        return ans