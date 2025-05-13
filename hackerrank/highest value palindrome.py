def highestValuePalindrome(s, n, k):
    s = list(s)  
    left = 0
    right = n - 1
    mismatches = set()
    while left < right:
        if s[left] != s[right]:
            s[left] = s[right] = max(s[left], s[right])
            mismatches.add(left)
            k -= 1
        if k < 0: 
            return '-1'
        left += 1
        right -= 1
        
    left = 0
    right = n - 1
    while left <= right:
        if left == right: 
            if k > 0:
                s[left] = '9'
        elif s[left] != '9':  
            if left in mismatches: 
                if k >= 1:
                    s[left] = s[right] = '9'
                    k -= 1
            elif k >= 2:  
                s[left] = s[right] = '9'
                k -= 2
        left += 1
        right -= 1

    return ''.join(s)