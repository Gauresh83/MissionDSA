from collections import deque


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        container = deque()

        iterNode = head

        while iterNode is not None:
            container.append(iterNode.val)
            iterNode = iterNode.next

        result = 0

        while container:
            front = container.popleft()
            back = container.pop()
            result = max(result, front + back)

        return result
