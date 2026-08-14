class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq=[0]*26
        l, n, Len=0, len(s), 0
        for r, x in enumerate(s):
            x=ord(s[r])-97
            freq[x]+=1
            while l<r and freq[x]>2:
                freq[ord(s[l])-97]-=1
                l+=1
            Len=max(Len, r-l+1)
        return Len
        
