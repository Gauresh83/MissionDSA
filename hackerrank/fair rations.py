def fairRations(B):
    count=0
    # Write your code here
    def isEvens(arr):
        for i in arr:
            if i%2 != 0:
                return False
        return True
    for j in range(len(B)):
        if B[j] % 2 != 0:
            if j == len(B)-1:
                return 'NO'
            B[j]+=1
            B[j+1]+=1
            count+=2
            if isEvens(B):
                return str(count)
    return '0'