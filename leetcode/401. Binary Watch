class Solution:
    def readBinaryWatch(self, k: int) -> List[str]:
        if k == 0:
            return ['0:00']
        mask = (1 << 6) - 1
        q = (1 << k) - 1
        limit = q << (10 - k)
        res = []
        while q <= limit:
            min = q & mask
            hour = q >> 6
            if hour < 12 and min < 60:
                res.append(f'{hour}:{min:0>2}')
            r = q & -q
            n = q + r 
            q = (((q ^ n) // r) >> 2) | n
        return res
