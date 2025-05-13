def candies(n, arr):
    # Write your code here
    total_candy = [1] * n
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            total_candy[i] = total_candy[i - 1] + 1
    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            total_candy[i] = max(total_candy[i], total_candy[i + 1] + 1)
    
    # The result is the sum of all total_candy
    return sum(total_candy)