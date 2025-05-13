class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = float('-inf')
        def inorder(node):
            nonlocal prev
            if not node:
                return True
            if not (inorder(node.left) and prev < node.val):
                return False
            prev = node.val
            return inorder(node.right)
        return inorder(root)