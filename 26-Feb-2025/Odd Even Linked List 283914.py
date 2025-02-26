# Problem: Odd Even Linked List - https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy2 = ListNode()
        ans = dummy
        ans2 = dummy2
        start2 = copy.deepcopy(head)
        counter = copy.deepcopy(head)
        start = head
        i = 1
        count = 0
        while counter:
            count+=1
            counter = counter.next
        while start: 
            if i%2 == 1 and i <= count:
                dummy.next = start
                if dummy.next:
                    dummy = dummy.next
            if (i%2 == 1 and i+2 <= count) or i%2 == 0:
                start = start.next
            else:
                start.next = None
            i+=1
        i = 1
        while start2: 
            if i%2 == 0 and i <= count:
                dummy2.next = start2
                dummy2 = dummy2.next
            if (i%2 == 0 and i+2 <= count) or i%2 == 1:
                start2 = start2.next
            else:
                start2.next = None
            i+=1
        dummy.next = ans2.next
        return ans.next
        