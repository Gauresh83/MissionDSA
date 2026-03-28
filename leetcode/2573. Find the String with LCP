class Solution:
    def findTheString(self, lcp):
        n = len(lcp)
        word = [''] * n
        current = ord('a')

        # construct the string
        for i in range(n):
            if word[i] == '':
                if current > ord('z'):
                    return ""
                word[i] = chr(current)
                for j in range(i + 1, n):
                    if lcp[i][j] > 0:
                        word[j] = word[i]
                current += 1

        # verify LCP matrix
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word[i] != word[j]:
                    if lcp[i][j] != 0:
                        return ""
                else:
                    if i == n - 1 or j == n - 1:
                        if lcp[i][j] != 1:
                            return ""
                    else:
                        if lcp[i][j] != lcp[i + 1][j + 1] + 1:
                            return ""

        return "".join(word)
