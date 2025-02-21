# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy2 = ListNode()
        ans = dummy
        ans2 = dummy2
        start2 = copy.deepcopy(head)
        start = head
        while start: 
            if start.val < x:
                dummy.next = start
                if dummy.next:
                    dummy = dummy.next
            start = start.next
        while start2: 
            if start2.val >= x:
                dummy2.next = start2
                dummy2 = dummy2.next
            start2 = start2.next
        while dummy2:
            if dummy2.next and dummy2.next.val < x:
                dummy2.next = None
            dummy2 = dummy2.next
        dummy.next = ans2.next
        return ans.next
        