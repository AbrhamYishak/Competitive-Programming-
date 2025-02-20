# Problem: Product of the Last K Numbers - https://leetcode.com/problems/product-of-the-last-k-numbers/description/

class ProductOfNumbers:

    def __init__(self):
        self.stream = [1]
        self.zero_position = set()
        self.len = 1
    def add(self, num: int) -> None:
        if num == 0:
            self.zero_position.add(self.len-1)
            self.stream.append(self.stream[-1])
        else:
            self.stream.append(self.stream[-1]*num)
        self.len+=1
    def getProduct(self, k: int) -> int:
        last = self.len-1
        start = last-k
        for i in self.zero_position:
            if start <= i <= last:
                return 0
        return self.stream[last]//self.stream[start]        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)