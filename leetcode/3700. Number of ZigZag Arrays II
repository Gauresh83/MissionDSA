class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        up = list(range(m))

        T = [[0]*m for _ in range(m)]
        for i in range(1, m):
            for k in range(m - i, m):
                T[i][k] = 1

        def matmul(A, B):
            sz = len(A)
            C = [[0]*sz for _ in range(sz)]
            for i in range(sz):
                for k in range(sz):
                    if not A[i][k]: continue
                    for j in range(sz):
                        C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
            return C

        def matpow(M, p):
            sz = len(M)
            res = [[int(i == j) for j in range(sz)] for i in range(sz)]
            while p:
                if p & 1: res = matmul(res, M)
                M = matmul(M, M)
                p >>= 1
            return res

        Tn = matpow(T, n - 2)

        ans = 0
        for i in range(m):
            for j in range(m):
                ans = (ans + Tn[i][j] * up[j]) % MOD

        return ans * 2 % MOD
