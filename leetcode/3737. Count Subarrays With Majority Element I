class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0

        for l in range(n):
            target_count = 0

            for r in range(l, n):
                if nums[r] == target:
                    target_count += 1

                length = r - l + 1

                if target_count > length // 2:
                    ans += 1

        return ans
