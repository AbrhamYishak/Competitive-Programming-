# Problem: Implement Queue using Stacks - https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.stack = []
        self.pointer= 0
    def push(self, x: int) -> None:
        self.stack.append(x)        
    def pop(self) -> int:
        self.pointer+=1
        return self.stack[self.pointer-1]
    def peek(self) -> int:
        return self.stack[self.pointer]
    def empty(self) -> bool:
        if self.pointer == len(self.stack):
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()