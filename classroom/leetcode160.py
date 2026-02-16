# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        d = {}
        ha = headA
        hb = headB
        while ha:
            d[ha] = True
            ha = ha.next
        while hb:
            if hb in d:
                return hb
            hb = hb.next
        return None