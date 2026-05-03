class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        if n != len(goal):
            return False

        dfa = [[0] * 26 for _ in range(n)]
        dfa[0][ord(s[0]) - 97] = 1

        x = 0
        for i in range(1, n):
            for j in range(26):
                dfa[i][j] = dfa[x][j]
            c = ord(s[i]) - 97
            dfa[i][c] = i + 1
            x = dfa[x][c]

        st = 0
        for i in range(n << 1):
            st = dfa[st][ord(goal[i % n]) - 97]
            if st == n:
                return True

        return False
