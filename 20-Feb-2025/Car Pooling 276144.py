# Problem: Car Pooling - https://leetcode.com/problems/car-pooling/description/

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        bus = [0]*(1001)
        for i in trips:
            n,f,t = i
            bus[f]+=n
            bus[t]-=n
        for i in range(1,1001):
            bus[i] = bus[i]+bus[i-1]
        if max(bus) > capacity:
            return False
        return True
        