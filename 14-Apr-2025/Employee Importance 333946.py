# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        ans = 0
        def search(id):
            found = False
            for i in employees:
                if i.id == id:
                    return(i.importance,i.subordinates)
                    found = True
            if not found:
                return (0,[])
        def dfs(id):
            x,y = search(id)
            ans = x
            for j in y:
                ans+=dfs(j)
            return ans
        for i in employees:
            if i.id == id:
                return dfs(id)
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        