

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def topView(root):
    #Write your code here
    top_view = {}
    
    queue = [(root,0)]

    while queue:
        
        node, hd = queue.pop(0)
        if hd not in top_view:
            top_view[hd] = node.info
        if node.left:
            queue.append((node.left, hd - 1))   
        if node.right:
            queue.append((node.right, hd + 1))
            
    for key in sorted(top_view.keys()):
        print(top_view[key], end=' ')

