# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        test = head
        while test:
            length+=1
            test = test.next
        i = -1
        target = length-n
        h = ListNode(-1,head)
        ans = h
        while h and i < target-1:
            i+=1
            h = h.next
        if h.next.next:
            h.next = h.next.next
        else:
            h.next = None
        return ans.next
        