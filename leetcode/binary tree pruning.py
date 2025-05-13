def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
	if root:
		root.left = self.pruneTree(root.left)
		root.right = self.pruneTree(root.right)
		if not root.left and not root.right and root.val == 0:
			return None
	return root