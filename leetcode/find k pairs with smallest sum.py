import heapq

class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        if not nums1 or not nums2 or k == 0:
            return []

        result = []
        min_heap = []

        # Start by pairing nums1[i] with nums2[0]
        for i in range(min(len(nums1), k)):
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))

        while k > 0 and min_heap:
            total, i, j = heapq.heappop(min_heap)
            result.append([nums1[i], nums2[j]])

            if j + 1 < len(nums2):
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))

            k -= 1

        return result