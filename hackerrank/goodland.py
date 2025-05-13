def pylons(k, arr):
    n = len(arr)
    plants = 0
    i = 0
    while i < n:
        plant_pos = -1
        for j in range(min(n - 1, i + k - 1), max(-1, i - k), -1):
            if arr[j] == 1:
                plant_pos = j
                break
                
        if plant_pos == -1:
            return -1  
        plants += 1
        i = plant_pos + k
    return plants