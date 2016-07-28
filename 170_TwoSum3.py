"""
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.
"""

# add: O(1) runtime
# find: O(n) runtime, O(n) space

from collections import Counter

class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.cnt = Counter()
        

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        self.cnt[number] += 1
        

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for k, v in self.cnt.items():
            dif = value - k
            if dif == k:
                if self.cnt.get(k) >= 2:
                    return True
            else:
                if self.cnt.get(dif):
                    return True
        else:
            return False

# Your TwoSum object will be instantiated and called as such:
twoSum = TwoSum()
twoSum.add(1)
twoSum.add(3)
twoSum.add(5)
twoSum.add(1)


print twoSum.find(4)
print twoSum.find(7)
print twoSum.find(2)
