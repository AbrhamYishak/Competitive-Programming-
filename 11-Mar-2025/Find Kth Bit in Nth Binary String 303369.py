# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def generator(s):
            if s == 1:
                return '0'
            else:
                a = generator(s-1)
                b = []
                for i in range(len(a)-1,-1,-1):
                    if a[i] == '0':
                        b.append('1')
                    else:
                        b.append('0')
                return a+"1"+"".join(b)
        return generator(n)[k-1]