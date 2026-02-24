class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        count = 0
        l1 = l2 = t = head
        while t.next:
            count += 1
            t = t.next
        for _ in range(count // 2):
            l2 = l2.next
        temp = head
        tl = l2
        while l2.next:
            temp = temp.next
            l2 = l2.next
        if not new:
            new.val = tl.val
            new.next = None
            t = t.next
        while t:
            nl = ListNode()
            nl.val = t.val
            nl.next = new
            new = nl
            t = t.next
        l1.next = new
        start = head
        while new:
            start.next = new
            start = start.next.next
            new = new.next
