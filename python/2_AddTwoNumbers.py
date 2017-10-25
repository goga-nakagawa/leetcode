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
        head = ListNode(0)
        p = l1
        q = l2
        curr = head
        carry = 0

        while p is not None or q is not None:
            x = p.val if p is not None else 0
            y = q.val if q is not None else 0
            digit = x + y + carry
            carry = digit / 10
            curr.next = ListNode(digit % 10)
            curr = curr.next
            if p is not None:
                p = p.next
            if q is not None:
                q = q.next
        if carry > 0:
            curr.next = ListNode(carry)
        return head.next


l1 = ListNode(5)
l2 = ListNode(5)

s = Solution()
print s.addTwoNumbers(l1, l2).val
print s.addTwoNumbers(l1, l2).next.val
# print s.addTwoNumbers(l1, l2).next.next.val
# print s.addTwoNumbers(l1, l2).next.next.next.val
# print s.addTwoNumbers(l1, l2).next.next.next.next.val
