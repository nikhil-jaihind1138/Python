class Solution(object):
    def deleteDuplicates(self, head):
        
    # Method 1
    
        p = head
        while p:
            temp = head
            if p.next != None and p.value == p.next.value:
                temp = p.next
                p.next = temp.next
                temp.next = None
            else:
                    p = p.next
                
        return head
    
    
    # Method 2
    
        current  = head
        while current and current.next:
            if current.val == caurrent.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head