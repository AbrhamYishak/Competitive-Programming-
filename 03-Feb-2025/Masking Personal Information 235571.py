# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        ans = ""
        isPhone = False
        for i in s:
            if i.isnumeric():
                isPhone = True
        if isPhone:
            num = ""
            for i in s:
                if i.isnumeric():
                    num+=i
            print(num)
            if(len(num)>10):
                ans+='+'
                ans+="*"*(len(num)-10)
                ans+='-'
            num = num[len(num)-10:]
            for i in range(0,len(num)-4):
                if i>0 and i%3 == 0:
                    ans+='-'
                ans+='*'
            ans+='-'
            ans+=num[len(num)-4:]
            return ans
        else:
            a,b = s.split('@')
            ans+=a[0].lower()+'*'*5+a[-1].lower()
            ans+='@'
            ans+=b.lower()
            return ans
                
                

        