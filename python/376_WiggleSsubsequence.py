"""
A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and negative. In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.
"""


from itertools import izip

class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        wiggle_l = 0
        max_l = 0
        flg = None
        start = 0
        for curr, next in izip(nums, nums[1:]):
            dif = curr - next
            start += 1
            if dif == 0:
                continue
            else:
                flg = dif > 0
                wiggle_l = 2
                max_l = 2
                break

        for curr, next in izip(nums[start:], nums[start+1:]):
            dif = curr - next
            if dif == 0:
                continue
            elif (dif > 0) ^ flg:
                wiggle_l += 1
                max_l = max([wiggle_l, max_l])
                flg = not flg
            else:
                wiggle_l = 2

        return max_l


s = Solution()
print s.wiggleMaxLength([1,7,4,9,2,5])
print s.wiggleMaxLength([1,7,4,5,5])
print s.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8])
print s.wiggleMaxLength([1,2,3,4,5,6,7,8,9])
