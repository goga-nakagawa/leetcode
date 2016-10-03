"""
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dup = set()
        for num in nums:
            if num in dup:
                return True
            else:
                dup.add(num)
        return False

s = Solution()
print s.containsDuplicate([1,2,3,4,5,6,7,1])
