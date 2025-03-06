# Problem: Number of Recent Calls - https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter:

    def __init__(self):
        self.call = deque()
    def ping(self, t: int) -> int:
        self.call.append(t)
        while t - self.call[0] > 3000:   
            self.call.popleft()
        return len(self.call)     


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)