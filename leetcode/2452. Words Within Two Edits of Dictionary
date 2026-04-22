import numpy as np

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        # All words have the same length N
        N = len(queries[0])
        
        # Convert to integer matrices: Shape (Q, N) and (D, N)
        q_vec = np.array([[ord(c) for c in w] for w in queries], dtype=np.int8)
        d_vec = np.array([[ord(c) for c in w] for w in dictionary], dtype=np.int8)
        
        results = []
        
        # We broadcast each query vector against the entire dictionary field
        # q_vec[i, None] has shape (1, N)
        # d_vec has shape (D, N)
        # Difference has shape (D, N)
        for i in range(len(queries)):
            # Displacement vectors from query[i] to all dictionary words
            diff = q_vec[i] != d_vec
            
            # Count the '1's (edits) across the word length (axis 1)
            edit_counts = np.sum(diff, axis=1)
            
            # If any dictionary word is within 2 edits
            if np.any(edit_counts <= 2):
                results.append(queries[i])
                
        return results        
