# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        s = e = None
        p = None
        while list1 and list2:
            if list1.val < list2.val:
                temp = list1
                list1 = list1.next
                temp.next = None
                if s == None:
                    s = e = temp
                else:
                    e.next = temp
                    e = temp
            else:
                temp = list2
                list2 = list2.next
                temp.next = None
                if s == None:
                    s = e = temp
                else:
                    e.next = temp
                    e = temp

        if list1:
            if s == None:
                s = list1
            else:
                e.next = list1
        elif list2:
            if s == None:
                s = list2
            else:
                e.next = list2
        return s
