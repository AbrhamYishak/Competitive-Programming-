# Problem: Goal Parser Interpretation - https://leetcode.com/problems/goal-parser-interpretation/description/

class Solution(object):
    def interpret(self, command):
        ans = ""
        for i in range(len(command)):
            if command[i] == "G":
                ans+="G"
            elif command[i] == "(":
                if command[i+1] == ")":
                    ans+="o"
                else:
                    ans+="al"
            else:
                continue
        return ans


        """
        :type command: str
        :rtype: str
        """
        