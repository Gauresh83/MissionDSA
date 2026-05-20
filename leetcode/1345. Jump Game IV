class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n=len(arr)
        vis=[False]*n
        mp=defaultdict(list)
        for i, x in enumerate(arr):
            mp[x].append(i)
        q=deque([0])
        step=0
        while q:
            s=len(q)
            for _ in range(s):
                cur=q.popleft()
                if cur==n-1: return step
                if cur>=1 and not vis[cur-1]:
                    q.append(cur-1)
                    vis[cur-1]=True
                if cur<=n and not vis[cur+1]:
                    q.append(cur+1)
                    vis[cur+1]=True
                x=arr[cur]
                for idx in mp[x]:
                    if not vis[idx]:
                        q.append(idx)
                        vis[idx]=True
                mp[x].clear()
            step+=1
        return -1
