class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
               1 > 2 > 3 > None
        None < 1 < 2 < 3
        """

        prev = None
        curr = head

        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
