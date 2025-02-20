# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.tail = ListNode(-1,None)
        self.head = ListNode(-1,self.tail)
        self.len = 0
    def get(self, index: int) -> int:
        if index >= self.len:
            return -1 
        i = -1
        curr = self.head
        while i < index:
            curr = curr.next
            i+=1
        return curr.val
    def addAtHead(self, val: int) -> None:
        self.len+=1
        node = ListNode(val,self.head.next)
        self.head.next = node
    def addAtTail(self, val: int) -> None:
        self.len+=1
        node = ListNode(val,self.tail)
        curr = self.head
        while curr.next.next:
            curr = curr.next
        curr.next = node
    def addAtIndex(self, index: int, val: int) -> None:  
        i = -1
        if index <= self.len:
            curr = self.head
            while i < index-1:
                curr = curr.next
                i+=1
            node = ListNode(val,curr.next)
            curr.next = node
            self.len+=1
    def deleteAtIndex(self, index: int) -> None:
        i = -1
        if index < self.len:
            curr = self.head
            while i < index-1:
                curr = curr.next
                i+=1
            curr.next = curr.next.next
            self.len-=1
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)