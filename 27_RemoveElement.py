"""
Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        p = 0
        q = len(nums) - 1
        while p < q and nums[q] == val:
            nums.pop()
            q -= 1

        while p <= q:
            if nums[p] == val:
                nums[-1], nums[p] = nums[p], nums[-1]
                nums.pop()
                q -= 1
            else:
                p += 1
        return len(nums)

s = Solution()
print s.removeElement([1,3,4,2,3,3,2,3], 3)