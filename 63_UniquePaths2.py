"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n = len(obstacleGrid)
        if not n:
            return 0
        m = len(obstacleGrid[0])

        for p in xrange(m):
            for q in xrange(n):
                if obstacleGrid[q][p] == 1:
                    continue
                elif p == 0 or q == 0:
                    obstacleGrid[q][p] = -1
                else:
                    s = 0 if obstacleGrid[q-1][p] == 1 else obstacleGrid[q-1][p]
                    t = 0 if obstacleGrid[q][p-1] == 1 else obstacleGrid[q][p-1]
                    obstacleGrid[q][p] = s + t

        return abs(obstacleGrid[n-1][m-1]) if obstacleGrid[n-1][m-1] < 0 else 0


grid = [
          [0,0,0,0],
          [0,0,1,0],
          [0,0,0,0],
          [0,0,0,0]
        ]
grid1 = [
          [0,0]
        ]
grid2 = [
          [1]
        ]
s = Solution()
print s.uniquePathsWithObstacles(grid)
print s.uniquePathsWithObstacles(grid1)
print s.uniquePathsWithObstacles(grid2)