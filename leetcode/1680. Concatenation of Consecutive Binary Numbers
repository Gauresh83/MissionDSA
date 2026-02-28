class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD=10**9+7
        ans=0
        for x in range(1, n+1):
            bw=x.bit_length()
            ans=(ans<<bw)+x
            if ans>=MOD: ans%=MOD
        return ans
