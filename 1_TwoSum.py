

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = {}
        for i, n in enumerate(nums):

            if (target - n) not in m.keys():
                m[n] = i
            else:
                return [m[target - n], i]
        return []

s = Solution()
print s.twoSum([2,7,11,15], 9)