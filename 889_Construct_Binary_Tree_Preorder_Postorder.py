# LeetCode provides TreeNode.
class Solution:
    def constructFromPrePost(self, preorder: list[int], postorder: list[int]):
        post_positions = {value: i for i, value in enumerate(postorder)}

        def build(pre_left, pre_right, post_left, post_right):
            if pre_left > pre_right:
                return None
            root = TreeNode(preorder[pre_left])
            if pre_left == pre_right:
                return root
            left_root = preorder[pre_left + 1]
            left_size = post_positions[left_root] - post_left + 1
            root.left = build(pre_left + 1, pre_left + left_size,
                              post_left, post_left + left_size - 1)
            root.right = build(pre_left + left_size + 1, pre_right,
                               post_left + left_size, post_right - 1)
            return root

        return build(0, len(preorder) - 1, 0, len(postorder) - 1)
