# Problem: Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(-101)
        final = ans
        while head:
            if head.next == None:
                ans.next = None
            if ans.val!=head.val:
                ans.next = head
                ans = ans.next
            head = head.next
        return final.next