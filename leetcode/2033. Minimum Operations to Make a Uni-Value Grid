class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        n, m = len(grid), len(grid[0])
        N = n * m
        freq = [0] * 10001
        mn = grid[0][0]
        mx = mn

        for row in grid:
            for c in row:
                if (c - grid[0][0]) % x != 0: return -1
                freq[c] += 1
                mn = min(mn, c)
                mx = max(mx, c)

        target = (N + 1) // 2
        acc = 0
        median = mn

        for i in range(mn, mx + 1, x):
            acc += freq[i]
            if acc >= target:
                median = i
                break

        ops = 0
        for i in range(mn, mx + 1, x):
            ops += abs(i - median) // x * freq[i]

        return ops
