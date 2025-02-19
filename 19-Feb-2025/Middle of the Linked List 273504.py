# Problem: Middle of the Linked List - https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        counter_head = head
        point = 0
        while counter_head:
            point+=1
            counter_head = counter_head.next
        point //= 2
        while head:
            if point == 0:
                ans.next = head
            head = head.next
            point-=1
        return ans.next