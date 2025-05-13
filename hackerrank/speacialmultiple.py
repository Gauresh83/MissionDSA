def solve(n):
    i = 0
    while True:
        i += 1
        x = int(bin(i)[2:]) * 9
        if x % n == 0:
            return str(x)