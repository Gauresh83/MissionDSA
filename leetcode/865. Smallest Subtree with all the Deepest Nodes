class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return 0, None

            left_height, left_node = dfs(node.left)
            right_height, right_node = dfs(node.right)

            if left_height > right_height:
                return left_height+1, left_node
            
            elif right_height > left_height:
                return right_height+1, right_node
            
            else:
                return left_height+1, node
            
        return dfs(root)[1]
