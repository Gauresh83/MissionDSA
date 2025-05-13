class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        path = []
        ans = []

        def func(root):
            if not root:
                return
            path.append(str(root.val))
            if not root.left and not root.right:
                ans.append("->".join(path))
            else:
                func(root.left)
                func(root.right)
            path.pop()

        func(root)
        return ans