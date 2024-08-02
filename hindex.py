class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse = True)
        print(citations)
        if citations[0] == 0:
            return 0
        dem = 0
        for i in range(0,len(citations)):
            if citations[i] == i+1:
                return i+1
            if citations[i] > i+1:
                dem += 1
        return dem
        
                    