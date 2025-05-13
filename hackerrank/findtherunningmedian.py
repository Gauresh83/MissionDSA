def get_median(arr):
    
    # Must pass sorted array
    n = len(arr)
    
    if n == 1: return arr[0]

    if n % 2 == 0:
        return round((arr[n // 2] + arr[n // 2 - 1]) / 2, 1)
    
    return round(arr[n // 2], 1)


def get_min_index(arr, x):
    """
    Fetch Min Index
    """
    
    # index = 0
    n = len(arr)
    
    # Optimisation
    
    # Base Checks
    if n == 0: return 0
    if x <= arr[0]: return 0
    if x >= arr[n-1]: return n
    
    l = 0
    r = n - 1
    
    while l < r:
        
        mid = (l + r) >> 1
        
        if arr[mid] < x: l = mid + 1
        else: r = mid
    
    return l

    
def sorted_insert(arr, x):
    min_index = get_min_index(arr, x)
    
    # Insert element
    arr.insert(min_index, x)

def runningMedian(a):
    # Write your code here
    
    sorted_arr = []
    running_median = []
    
    for ele in a: # O(n) * log n time 
        sorted_insert(sorted_arr, ele) # O(log n) time avg~
        running_median.append(get_median(sorted_arr))
        
    return running_median