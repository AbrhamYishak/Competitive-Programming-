# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = defaultdict(int)
        for i in cpdomains:
            a,b = i.split()
            a = int(a)
            d[b] += a
            for i in range(len(b)):
                if b[i] == '.':
                    d[b[i+1:]]+=a
        ans = []
        for i in d:
            ans.append(str(d[i])+" "+i)
        return ans

        
        