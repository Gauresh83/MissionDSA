class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        a=[]
        if not  lists:
            return None
        for i in lists:
            k=i
            while k:
                a.append(k.val)
                k=k.next
        a.sort()
        m=ListNode(-1)
        head=m

        for i in range(len(a)):
            k=ListNode(a[i])
            m.next=k
            m=m.next
        return head.next 


