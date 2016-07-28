"""
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.
"""

# add: O(n) runtime
# find: O(n) runtime, O(1) space

from itertools import izip

class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.numbers = []
        

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        if self.numbers:
            if number <= self.numbers[0]:
                self.numbers.insert(0, number)
            elif number > self.numbers[-1]:
                self.numbers.append(number)
            else:
                for curr, next in izip(self.numbers, self.numbers[1:]):
                    if curr <= number and number < next:
                        self.numbers.insert(curr, number)
                        break
        else:
            self.numbers.append(number)
        

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        head = 0
        tail = len(self.numbers) - 1
        while head < tail:
            if self.numbers[head] + self.numbers[tail] == value:
                return True
            elif self.numbers[head] + self.numbers[tail] < value:
                head += 1
            else:
                tail -= 1
        return False

# Your TwoSum object will be instantiated and called as such:
twoSum = TwoSum()
twoSum.add(0)
twoSum.add(0)
print twoSum.numbers
print twoSum.find(0)

