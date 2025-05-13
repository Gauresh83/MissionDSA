class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # Initialize the outDegree (children) - inDegree (parent) to 1
        degree = 1
        
        # Iterate through the nodes in the preorder traversal
        for node in preorder.split(','):
            degree -= 1 # Decrement the degree by 1 for each node
            
            if degree < 0: # If the degree is negative, return False
                return False
            
            if node != '#': # If the node is not a leaf node
                degree += 2 # Increment the degree by 2 for each non-leaf node
            
        # If the final degree is 0, the tree is valid, else invalid
        return degree == 0