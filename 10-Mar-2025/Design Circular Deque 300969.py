# Problem: Design Circular Deque - https://leetcode.com/problems/design-circular-deque/

class Node():
    def __init__(self,val,prev = None,next = None):
        self.val = val
        self.next = next
        self.prev = prev
class MyCircularDeque:

    def __init__(self, k: int):
        self.head = Node(-1)
        self.tail = Node(-2)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.limit = k
        self.len = 0
    def insertFront(self, value: int) -> bool:
        if self.len < self.limit:
            new_node = Node(value,self.head,self.head.next)
            self.head.next.prev = new_node
            self.head.next = new_node
            self.len+=1
            return True
        return False
    def insertLast(self, value: int) -> bool:
        if self.len < self.limit:
            new_node = Node(value,self.tail.prev,self.tail)
            self.tail.prev.next = new_node
            self.tail.prev = new_node
            self.len+=1
            return True
        return False
    def deleteFront(self) -> bool:
        if self.head.next.next:
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
            self.len-=1
            return True
        return False
    def deleteLast(self) -> bool:
        if self.tail.prev.prev:
            self.tail.prev.prev.next = self.tail
            self.tail.prev = self.tail.prev.prev
            self.len-=1
            return True
        return False
    def getFront(self) -> int:
        if self.len >= 1:
            return self.head.next.val
        return -1
    def getRear(self) -> int:
        if self.len >= 1:
            return self.tail.prev.val
        return -1
    def isEmpty(self) -> bool:
        if self.len:
            return False
        return True
    def isFull(self) -> bool:
        return self.len == self.limit


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()