"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for _ in xrange(m)] for _ in xrange(n)]

        for p in xrange(m):
            for q in xrange(n):
                if p == 0 or q == 0:
                    dp[q][p] = 1
                else:
                    dp[q][p] = dp[q-1][p] + dp[q][p-1]

        return dp[n-1][m-1]

s = Solution()
print s.uniquePaths(4, 5)