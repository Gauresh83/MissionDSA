class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        cnt = Counter(costs); ans = 0
        for c in range(1, max(cnt) + 1):
            buy = min(cnt[c], coins // c)
            ans += buy
            coins -= buy * c
        return ans
