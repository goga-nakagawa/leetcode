"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for num in nums[len(nums)-k:][::-1]:
            nums.pop(-1)
            nums.insert(0, num)

    def rotate1(self, nums, k):
        for num in nums[:len(nums)-k]:
            nums.pop(0)
            nums.append(num)


    def rotate2(self, nums, k):
        p = 0
        q = len(nums) - k
        while p < len(nums) - k:
            if q < len(nums):
                nums[p] , nums[q] = nums[q], nums[p]
            else:
                tmp = nums.pop(p)
                nums.append(tmp)
            p, q = p + 1, q + 1


    def rotate3(self, nums, k):
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1


arr = [1,2,3,4,5,6,7]
Solution().rotate(arr, 3)
print arr

arr1 = [1,2,3,4,5,6,7]
Solution().rotate1(arr1, 3)
print arr1

arr2 = [1,2,3,4,5,6,7]
Solution().rotate2(arr2, 3)
print arr2

arr3 = [1,2,3,4,5,6,7]
Solution().rotate3(arr3, 3)
print arr3