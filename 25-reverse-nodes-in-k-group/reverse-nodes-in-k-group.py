# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        curr = head
        for i in range(k):
            if curr == None:
                return head
            curr = curr.next

        cnt = 0
        pre = None
        curr = head
        
        while cnt < k:
            temp = curr.next
            curr.next = pre
            pre = curr
            curr = temp
            cnt += 1
        
        head.next = self.reverseKGroup(curr, k)
        return pre

        