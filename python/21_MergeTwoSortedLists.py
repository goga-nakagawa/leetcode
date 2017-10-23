"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyhead = ListNode(0)
        p = dummyhead
        while (l1 is not None and l2 is not None):
            if (l1.val < l2.val):
                p.next = l1
                l1.next = l1
            else:
                p.next = l2
                l2.next = l2
            p = p.next
        if (l1 is not None):
            p.next = l1
        if (l2 is not None):
            p.next = l2

        return dummyhead.next
