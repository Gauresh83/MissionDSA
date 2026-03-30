class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        freq=[0]*52
        n=len(s1)
        for i in range(n):
            iOdd=i&1
            freq[iOdd*26+ord(s1[i])-97]+=1
            freq[iOdd*26+ord(s2[i])-97]-=1
        return all(x==0 for x in freq)
        
