class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(i):
            if i==0: return 0
            ans=-inf
            for j in range(i):
                if abs(nums[j]-nums[i])<=target:
                    ans=max(ans, 1+dfs(j))
            return ans
        ans=dfs(len(nums)-1)
        return -1 if ans<0 else ans

        
