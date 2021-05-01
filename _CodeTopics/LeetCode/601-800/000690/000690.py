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
    res = 0
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """

        dic = {employee.id:employee for employee in employees}

        def dfs_for_importance(employee):
            self.res += employee.importance
            if not employee.subordinates:
                return
            for subord in employee.subordinates:
                dfs_for_importance(dic[subord])

        dfs_for_importance(dic[id])
        return self.res
        
"""
https://leetcode-cn.com/submissions/detail/173748175/

108 / 108 个通过测试用例
状态：通过
执行用时: 148 ms
内存消耗: 14.7 MB

执行用时：148 ms, 在所有 Python 提交中击败了57.14%的用户
内存消耗：14.7 MB, 在所有 Python 提交中击败了5.36%的用户
"""
