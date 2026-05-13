class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        dp = [0] * (2 * limit + 2)
        for i in range(n // 2):
            mini = min(nums[i], nums[-1 - i])
            maxi = max(nums[i], nums[-1 - i])
            dp[2] += 2
            dp[mini + 1] -= 1
            dp[mini + maxi] -= 1
            dp[mini + maxi + 1] += 1
            dp[maxi + limit + 1] += 1
        res = n
        moves = 0
        for c in range(2, 2 * limit + 1):
            moves += dp[c]
            res = min(res, moves)
        return res
