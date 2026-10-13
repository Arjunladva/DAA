# LeetCode provides TreeNode.
class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]):
        if not nums:
            return None
        middle = nums.index(max(nums))
        node = TreeNode(nums[middle])
        node.left = self.constructMaximumBinaryTree(nums[:middle])
        node.right = self.constructMaximumBinaryTree(nums[middle + 1:])
        return node
