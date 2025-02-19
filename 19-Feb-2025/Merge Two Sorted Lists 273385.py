# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        final = ListNode(-1,None)
        head = final
        while list1 and list2:
            if list1.val < list2.val:
                final.next = list1
                list1 = list1.next
            else:
                final.next = list2
                list2 = list2.next
            final = final.next
        while list1:
            final.next = list1
            break
        while list2:
            final.next = list2
            break
        return head.next