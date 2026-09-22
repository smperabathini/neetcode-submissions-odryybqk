# Definition for singly-linked list.
# class ListNode:
from os import terminal_size
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        one = list1 if list1.val <= list2.val else list2
        two = list2 if list2.val >= list1.val else list1
        head = one

        while two:
            if not one.next:
                one.next = two
                return head
            if two.val <= one.next.val:
                temp = two.next
                two.next = one.next
                one.next = two
                two = temp
            one = one.next
        return head
            
