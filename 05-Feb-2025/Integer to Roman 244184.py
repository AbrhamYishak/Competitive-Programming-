# Problem: Integer to Roman - https://leetcode.com/problems/integer-to-roman/description/

class Solution:
    def intToRoman(self, num: int) -> str:
        ans = []
        list1 = ['I','X','C','M']
        list2 = ['V','L','D']
        num = str(num)
        for i in range(len(num)):
            if int(num[i]) < 4:
                ans.append(list1[len(num)-i-1]*int(num[i]))
            elif int(num[i]) == 4:
                ans.append(list1[len(num)-i-1])
                ans.append(list2[len(num)-i-1])
            elif 9 > int(num[i]) >= 5:
                ans.append(list2[len(num)-i-1])
                ans.append(list1[len(num)-i-1]*(int(num[i])-5))
            else:
                ans.append(list1[len(num)-i-1])
                ans.append(list1[len(num)-i])
        return "".join(ans)