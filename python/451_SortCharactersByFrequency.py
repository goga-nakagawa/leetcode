
from collections import Counter



class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        cnt = Counter(s)
        res = ""
        for w in sorted(cnt, key=cnt.get, reverse=True):
            res += w*cnt.get(w)
        return res

s = Solution()
print s.frequencySort('cccaaa')