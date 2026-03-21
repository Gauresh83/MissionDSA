class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        t, b=x, x+k-1
        while t<b:
            grid[t][y:y+k], grid[b][y:y+k]=grid[b][y:y+k],grid[t][y:y+k]
            t+=1
            b-=1
        return grid
