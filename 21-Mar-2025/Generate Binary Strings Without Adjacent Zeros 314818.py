# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = set()
        a = []
        def generator(can):
            if len(a) == n:
                ans.add("".join(a))
                return
            if can:
                a.append("0")
                generator(False)
                a.pop()
                a.append("1")
                generator(True)
                a.pop()
            else:
                a.append("1")
                generator(True)
                a.pop()
        generator(True)
        return list(ans)