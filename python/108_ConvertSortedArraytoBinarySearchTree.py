# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.helper(nums, 0, len(nums)-1)

    def helper(self, arr, start, end):
        if start > end:
            return None
        mid = (start + end)/2
        node = TreeNode(arr[mid])
        node.left = self.helper(arr, start, mid-1)
        node.right = self.helper(arr, mid+1, end)
        return node

s = Solution()
print s.sortedArrayToBST([9,12,14,17,19,23,50,54,67,72,76])