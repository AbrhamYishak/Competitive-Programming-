# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 =l1
        curr2 = l2
        len_l1 = 0
        len_l2 = 0
        while curr1:
            len_l1+=1
            curr1 = curr1.next
        while curr2:
            len_l2+=1
            curr2 = curr2.next
        curr = l1
        curr2 = l2
        if len_l1 > len_l2:
            curr = l1
            curr2 = l2
        else:
            curr = l2
            curr2 = l1
        final = curr
        carry = 0
        while curr:
            if curr and curr2:
                ans = curr.val+curr2.val+carry
                if ans>9:
                    curr.val = ans-10
                    carry = 1
                else:
                    curr.val = ans
                    carry = 0
                curr = curr.next
                curr2 = curr2.next
            else:
                while curr and carry:
                    ans = curr.val+carry
                    if ans>9:
                        curr.val = ans-10
                        carry = 1
                    else:
                        curr.val = ans
                        carry = 0
                    curr = curr.next
                break
        a = final
        if carry:
            while a.next:
                a = a.next
            a.next = ListNode(carry,None)
        return final



