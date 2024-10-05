class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic={}
        for s in strs:
            sorted_word = ''.join(sorted(s))
            if sorted_word in dic:
                dic[sorted_word].append(s)
            else:
                dic[sorted_word]=[s]
        return list(dic.values())
        