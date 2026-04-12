class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n, M=len(nums), max(nums)
        pos=[(-1, -1) for _ in range(M+1)]
        ans=1<<32
        for k, x in enumerate(nums):
            if pos[x][1]!=-1:
                ans=min(ans, (k-pos[x][1])<<1)
            pos[x]=k, pos[x][0]
        return -1 if ans==1<<32 else ans      
