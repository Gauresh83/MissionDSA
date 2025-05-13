class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        d = dict(sorted(d.items(), key=lambda item: item[1],reverse=True))
        res=[]
        for i in d:
            if k>0:
                res.append(i)
                k-=1
        
        return res