def sansaXor(arr):
    ln = len(arr)
    x = 0
    i = 0
    
    if (ln % 2 != 0):
        while (i < ln):
            x ^= arr[i]
            i += 2
        return x
    
    return 0