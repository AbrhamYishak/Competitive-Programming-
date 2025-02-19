# Problem: Reverse Linked List - https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        final = ListNode(-1,None)
        ans = final
        while head:
            a = head
            while a.next and a.next.next:
                a = a.next
            if a.next:
                final.next = a.next
                final = final.next
            if a == head:
                a.next = None
                final.next = a
                break
            a.next = None
        return ans.next
        