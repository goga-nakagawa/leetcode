"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

"""
from itertools import izip

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for curr, next in izip(prices, prices[1:]):
            if curr < next:
                profit += next - curr
        return profit



s = Solution()
print s.maxProfit([7, 1, 5, 3, 6, 4])
print s.maxProfit([7, 6, 4, 3, 1])
