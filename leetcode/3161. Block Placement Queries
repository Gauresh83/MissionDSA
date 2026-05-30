class Solution:

    MAXX = 50000

    def __init__(self):
        self.seg = [0] * (4 * (self.MAXX + 1))

    def update(self, node, l, r, idx, val):
        if l == r:
            self.seg[node] = val
            return

        mid = (l + r) // 2

        if idx <= mid:
            self.update(2 * node, l, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, r, idx, val)

        self.seg[node] = max(
            self.seg[2 * node],
            self.seg[2 * node + 1]
        )

    def query(self, node, l, r, ql, qr):
        if ql > r or qr < l:
            return 0

        if ql <= l and r <= qr:
            return self.seg[node]

        mid = (l + r) // 2

        return max(
            self.query(2 * node, l, mid, ql, qr),
            self.query(2 * node + 1, mid + 1, r, ql, qr)
        )

    def getResults(self, queries: List[List[int]]) -> List[bool]:
        
        obstacles = SortedSet([0])

        # Build final obstacle configuration
        for q in queries:
            if q[0] == 1:
                obstacles.add(q[1])

        pos = list(obstacles)

        # gap[pos[i]] = pos[i] - pos[i-1]
        for i in range(1, len(pos)):
            self.update(1,0,self.MAXX,pos[i],pos[i] - pos[i - 1])

        ans = []

        for i in range(len(queries) - 1, -1, -1):

            if queries[i][0] == 2:

                x = queries[i][1]
                sz = queries[i][2]

                idx = obstacles.bisect_right(x) - 1
                prev_obstacle = obstacles[idx]

                best = self.query(1,0,self.MAXX,0,prev_obstacle)
                best = max(best, x - prev_obstacle)

                ans.append(best >= sz)

            else:

                x = queries[i][1]

                idx = obstacles.index(x)
                left_pos = obstacles[idx - 1]

                # remove gap ending at x
                self.update(1,0,self.MAXX,x,0)

                if idx + 1 < len(obstacles):
                    right_pos = obstacles[idx + 1]
                    # merge gaps
                    self.update(1,0,self.MAXX,right_pos,right_pos - left_pos)

                obstacles.remove(x)

        return ans[::-1]
        
