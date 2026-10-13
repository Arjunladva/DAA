# LeetCode provides TreeNode.
class Solution:
    def sortedArrayToBST(self, nums: list[int]):
        def build(left, right):
            if left > right:
                return None
            middle = (left + right) // 2
            node = TreeNode(nums[middle])
            node.left = build(left, middle - 1)
            node.right = build(middle + 1, right)
            return node
        return build(0, len(nums) - 1)
