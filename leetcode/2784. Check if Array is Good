class Solution:
    def isGood(self, nums: List[int]) -> bool:
        mx = max(nums)

        # size must be mx + 1
        if len(nums) != mx + 1:
            return False

        freq = [0] * (mx + 1)

        for x in nums:
            # invalid number
            if x < 1 or x > mx:
                return False

            freq[x] += 1

        # 1 to mx-1 should appear once
        for i in range(1, mx):
            if freq[i] != 1:
                return False

        # mx should appear twice
        return freq[mx] == 2
