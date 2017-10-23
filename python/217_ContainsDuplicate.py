"""
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dup = {}
        for n in nums:
            if n not in dup.keys():
                dup[n] = True
            else:
                return True
        return False

s = Solution()
print s.containsDuplicate([1,2,3,4,5,6,7,1])
