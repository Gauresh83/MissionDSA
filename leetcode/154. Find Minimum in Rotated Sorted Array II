class Solution:
    def findMin(self, nums):

        s = 0
        e = len(nums) - 1

        while s < e:

            # Find middle index
            mid = s + (e - s) // 2

            # Minimum lies in right half
            if nums[mid] > nums[e]:
                s = mid + 1

            # Minimum lies in left half including mid
            elif nums[mid] < nums[e]:
                e = mid

            # Duplicate case
            # Cannot determine correct side
            else:
                e -= 1

        # s points to minimum element
        return nums[s]
