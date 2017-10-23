class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maxSofar, maxEndingHere = nums[0], nums[0]
        for n in nums:
            maxEndingHere = max(maxEndingHere + n, n)
            maxSofar = max(maxEndingHere, maxSofar)
        return maxSofar


s = Solution()
print s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])