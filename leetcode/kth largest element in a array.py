class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(left, right):            
            pivot = nums[right]
            low = left
            high = right

            while low <= high:
                while low <= high and nums[low] < pivot:
                    low += 1
                while low <= high and nums[high] > pivot:
                    high -= 1
                if low <= high:
                    nums[low], nums[high] = nums[high], nums[low]
                    low += 1
                    high -= 1

            if k <= high:
                return quickSelect(left, high)
            elif k >= low:
                return quickSelect(low, right)
            else:
                return nums[k]

        return quickSelect(0, len(nums) - 1)