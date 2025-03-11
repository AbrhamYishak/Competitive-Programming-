# Problem: Design browser history  - https://leetcode.com/problems/design-browser-history/

class Node():
    def __init__(self,val = "",next = None,prev = None):
        self.prev = prev
        self.val = val
        self.next = next
class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.pos = 1
    def visit(self, url: str) -> None:
        i = 1
        curr = self.head
        while curr and i < self.pos:
            curr = curr.next
            i+=1
        node = Node(url,self.tail,curr)
        curr.next = node
        self.pos +=1
    def back(self, steps: int) -> str:
        i = 1
        curr = self.head
        while curr and i < self.pos:
            curr = curr.next
            i+=1
        while curr.prev and steps > 0:
            curr = curr.prev
            steps-=1
            self.pos-=1
        return curr.val
    def forward(self, steps: int) -> str:
        i = 1
        curr = self.head
        while curr.next and i < self.pos:
            curr = curr.next
            i+=1
        while curr.next.next and steps > 0:
            curr = curr.next
            steps-=1
            self.pos+=1
        return curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)