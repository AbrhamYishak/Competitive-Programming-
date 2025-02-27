# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        a = []
        while head:
            a.append(head.val)
            head = head.next
        i = 0
        j = len(a)-1
        max_sum = float("-inf")
        while i < j:
            max_sum = max(max_sum,a[i]+a[j])
            i+=1
            j-=1
        return max_sum
