# LeetCode provides ListNode and TreeNode.
class Solution:
    def sortedListToBST(self, head):
        values = []
        while head:
            values.append(head.val)
            head = head.next

        def build(left, right):
            if left > right:
                return None
            middle = (left + right) // 2
            node = TreeNode(values[middle])
            node.left = build(left, middle - 1)
            node.right = build(middle + 1, right)
            return node
        return build(0, len(values) - 1)
