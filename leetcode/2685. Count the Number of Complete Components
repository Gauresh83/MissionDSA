class UnionFind:
    def __init__(self, N):
        self.root = list(range(N))
        self.Size = [1]*N

    def Find(self, x):
        if self.root[x] != x:
            self.root[x] = self.Find(self.root[x])  # path compression
        return self.root[x]

    def Union(self, x, y):
        x = self.Find(x)
        y = self.Find(y)
        if x==y: return False

        if self.Size[x] > self.Size[y]:
            self.Size[x] += self.Size[y]
            self.root[y]=x
        else:
            self.Size[y] += self.Size[x]
            self.root[x]=y
        return True
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        m=len(edges)
        if m==n*(n-1)//2: 
            return 1

        G=UnionFind(n)
        eN=[0]*n
        for v, w in edges:
            a=eN[G.Find(v)]
            b=eN[G.Find(w)]
            if G.Union(v, w):
                eN[G.Find(v)]=a+b+1
            else:
                eN[G.Find(v)]=a+1
        ans=0
        for i, v in enumerate(G.Size):
            if G.Find(i)==i and eN[i]==v*(v-1)//2:
                ans+=1
        return ans
         
