# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional [TreeNode]:
        ptr = root
        if ptr==None:
            ptr = TreeNode(val = val)
            return ptr
            
        while True:
                if ptr.val>val: 
                    if ptr.left==None:
                        ptr.left = TreeNode(val=val)
                        break
                    ptr = ptr.left
            
        
                elif ptr.val<val:
                    if ptr.right == None:
                        ptr.right = TreeNode(val=val)
                        break
                    ptr = ptr.right
            
        return root
    

            

        