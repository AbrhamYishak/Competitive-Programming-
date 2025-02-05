# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

import random
class RandomizedSet:
    def __init__(self):
        self.set = []
        self.dict = {}
        self.ind = 0
    def insert(self, val: int) -> bool:
        if val not in self.set:
            self.set.append(val)
            self.dict[val] = self.ind
            self.ind+=1
            return True
        else:
            return False
    def remove(self, val: int) -> bool:
        if val in self.set:
            ind = self.dict[val]
            self.set[ind],self.set[-1] = self.set[-1],self.set[ind]
            self.dict[self.set[ind]] = ind
            del self.dict[self.set[-1]]
            self.set.pop()
            self.ind-=1
            return True
        else:
            return False
    def getRandom(self) -> int:
        num = random.random()
        a = self.set[int(len(self.set)*num)]
        return a


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()