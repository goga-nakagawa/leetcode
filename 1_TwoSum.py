class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = dict() # val:index
        for i, num in enumerate(nums):
            if (target - num) in m.keys():
                return [m.get(target - num) + 1, i + 1]
            m[num] = i
        return []