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
        if len(nums) < 2:
            return len(nums)
        ret = 2
        cnt = 2
        flg = nums[0] < nums[1]

        for curr, next in izip(nums[1:], nums[2:]):
            dif = next - curr if flg else curr - next
            if dif == 0:
                continue
            elif dif < 0 ^ flg:
                cnt += 1
                flg = not flg
                ret = max([cnt, ret])
            else:
                cnt = 2
                flg = curr < next
        return ret


s = Solution()
print s.wiggleMaxLength([1,7,4,9,2,5])
print s.wiggleMaxLength([1,4,7,2,5])
print s.wiggleMaxLength([1,7,4,5,5])
print s.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8])
print s.wiggleMaxLength([1,2,3,4,5,6,7,8,9])
