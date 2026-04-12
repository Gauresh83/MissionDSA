# dp[i][j]=min cost after typing word[i], with the OTHER finger at j
# 26 denotes hovering
class Solution:
    def minimumDistance(self, word: str) -> int:
        def dist(x, y):
            if x==26 or y==26: return 0
            return abs(x//6-y//6)+abs(x%6-y%6)
        # setting for dp
        n=len(word)
        INF=1<<30
        dp=[[INF]*27 for _ in range(n)]
        dp[0][26]=0
        prev=ord(word[0])-65
        for i, c in enumerate(word[1:], start=1):
            x=ord(c)-65
            for j in range(27):
                dp[i][j]=min(dp[i][j], dp[i-1][j]+dist(prev, x))
                dp[i][prev]=min(dp[i][prev], dp[i-1][j]+dist(j, x))
            prev=x
        return min(dp[-1])
        
        
