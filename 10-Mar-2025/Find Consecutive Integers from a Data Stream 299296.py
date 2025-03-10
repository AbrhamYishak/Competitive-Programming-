# Problem: Find Consecutive Integers from a Data Stream - https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream:

    def __init__(self, value: int, k: int):
        self.que = deque()        
        self.val = value
        self.k = k
        self.counter = defaultdict(int)
    def consec(self, num: int) -> bool:
        self.que.append(num)
        self.counter[num]+=1
        if len(self.que) > self.k:
            a = self.que.popleft()
            self.counter[a]-=1
            if not self.counter[a]:
                del self.counter[a]
        if len(self.que) == self.k:
            if len(self.counter) == 1 and self.val in self.counter:
                return True
        return False


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)