# LeetCode provides ListNode.
class Solution:
    def sortList(self, head):
        values = []
        while head:
            values.append(head.val)
            head = head.next
        values.sort()

        dummy = ListNode(0)
        tail = dummy
        for value in values:
            tail.next = ListNode(value)
            tail = tail.next
        return dummy.next
