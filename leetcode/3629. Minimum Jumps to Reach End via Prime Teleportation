class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0

        mx = max(nums)

        spf = list(range(mx + 1))

        for i in range(2, int(mx ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, mx + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        mp = defaultdict(list)

        for i, x in enumerate(nums):
            temp = x

            while temp > 1:
                p = spf[temp]

                mp[p].append(i)

                while temp % p == 0:
                    temp //= p

        q = deque([0])
        vis = [False] * n
        vis[0] = True

        used_prime = set()

        steps = 0

        while q:

            for _ in range(len(q)):

                i = q.popleft()

                if i == n - 1:
                    return steps

                if i - 1 >= 0 and not vis[i - 1]:
                    vis[i - 1] = True
                    q.append(i - 1)

                if i + 1 < n and not vis[i + 1]:
                    vis[i + 1] = True
                    q.append(i + 1)

                val = nums[i]

                if val > 1 and spf[val] == val and val not in used_prime:

                    used_prime.add(val)

                    for idx in mp[val]:
                        if not vis[idx]:
                            vis[idx] = True
                            q.append(idx)

                    mp[val].clear()

            steps += 1

        return -1       
