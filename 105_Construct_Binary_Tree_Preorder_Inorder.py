# LeetCode provides TreeNode.
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]):
        positions = {value: i for i, value in enumerate(inorder)}
        self.index = 0

        def build(left, right):
            if left > right:
                return None
            value = preorder[self.index]
            self.index += 1
            node = TreeNode(value)
            middle = positions[value]
            node.left = build(left, middle - 1)
            node.right = build(middle + 1, right)
            return node

        return build(0, len(inorder) - 1)
