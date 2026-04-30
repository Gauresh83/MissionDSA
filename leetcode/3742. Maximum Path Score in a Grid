class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        
        t = [[[-1] * (k + 1) for _ in range(n)] for _ in range(m)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                is_pos = 1 if grid[i][j] > 0 else 0
                for cost in range(k + 1):
                    new_cost = cost + is_pos
                    if new_cost > k:
                        continue
                    if i == m - 1 and j == n - 1:
                        t[i][j][cost] = grid[i][j]
                        continue
                    else:
                        down = t[i + 1][j][new_cost] if i + 1 < m else -1
                        right = t[i][j + 1][new_cost] if j + 1 < n else -1
                        best_next = max(down, right)

                        if best_next != -1:
                            t[i][j][cost] = grid[i][j] + best_next
        
        return t[0][0][0]
