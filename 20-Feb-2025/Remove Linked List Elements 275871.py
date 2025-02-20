# Problem: Remove Linked List Elements - https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        ans = ListNode()
        modified = head
        a = modified
        while modified and modified.next:
            while modified.next and modified.next.val == val:
                if modified.next.next:
                    modified.next = modified.next.next
                else:
                    modified.next = None
            modified = modified.next
        if a and a.val == val:
            ans.next = a.next
        elif a and a.val != val:
            ans.next = a
        return ans.next

        