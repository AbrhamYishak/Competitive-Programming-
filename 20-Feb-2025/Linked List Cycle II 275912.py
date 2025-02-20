# Problem: Linked List Cycle II - https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rabbit = head
        tor = head
        if not rabbit or not rabbit.next:
            return None
        while rabbit and rabbit.next:
            rabbit = rabbit.next.next
            tor = tor.next
            if rabbit and rabbit == tor:
                break
        tor = head
        while rabbit:
            if rabbit == tor:
                return tor
            rabbit = rabbit.next
            tor = tor.next
        return None