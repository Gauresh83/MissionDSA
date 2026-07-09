class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        qz, prev, cid=len(queries), -1, 0
        comp=[-1]*n
        for i, curr in enumerate(nums):
            cid+=(prev+maxDiff<curr)
            comp[i]=cid
            prev=curr
        return [ comp[x]==comp[y] for x, y in queries]

        
