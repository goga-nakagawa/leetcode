"""
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 is not None and l2 is not None:
            a = l1.val + l2.val
            carry, digit = a / 10, a % 10 + carry
            curr.next = ListNode(digit)
            l1, l2 = l1.next, l2.next
            curr = curr.next

        if l1 is None:
            while l2 is not None:
                carry, digit = 0, l2.val + carry
                curr.next = ListNode(digit)
                curr = curr.next
                l2 = l2.next
        if l2 is None:
            while l1 is not None:
                carry, digit = 0, l1.val + carry
                curr.next = ListNode(digit)
                curr = curr.next
                l1 = l1.next

        if carry  == 1:
            curr.next = ListNode(1)
        return dummy.next


l1 = ListNode(5)
l2 = ListNode(5)

s = Solution()
print s.addTwoNumbers(l1, l2).val
print s.addTwoNumbers(l1, l2).next.val
# print s.addTwoNumbers(l1, l2).next.next.val
# print s.addTwoNumbers(l1, l2).next.next.next.val
# print s.addTwoNumbers(l1, l2).next.next.next.next.val
