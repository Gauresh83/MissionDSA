t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    d={0:1}
    ans=0
    sums=0
    for i in range(n):
        sums+=a[i]
        temp=sums%k
        if temp in d:
            ans+=d[temp]
            d[temp]+=1
        else:
            d[temp]=1
    print(ans)