# Added using AI
class Solution:
    def minimumDistance(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 2:
            return -1
        ans = float('inf')
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    for k in range(j+1, n):
                        if nums[j] == nums[k]:
                            ans = min(ans, 2*(k-i))
        return -1 if ans == float('inf') else ans
