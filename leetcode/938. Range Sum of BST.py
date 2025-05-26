class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def dfs(root):
            if not root:
                return 0
            current = 0
            if low <= root.val <= high:
                current = root.val
            left = dfs(root.left)
            right = dfs(root.right)
            return current + left + right

        return dfs(root)
