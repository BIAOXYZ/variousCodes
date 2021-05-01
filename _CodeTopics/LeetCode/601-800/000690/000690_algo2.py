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
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """

        dic = {employee.id:employee for employee in employees}

        res = dic[id].importance
        stk = collections.deque([subd for subd in dic[id].subordinates])
        while stk:
            currId = stk.popleft()
            res += dic[currId].importance
            for subd in dic[currId].subordinates:
                stk.append(subd)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/173755500/

108 / 108 个通过测试用例
状态：通过
执行用时: 140 ms
内存消耗: 14 MB

执行用时：140 ms, 在所有 Python 提交中击败了83.93%的用户
内存消耗：14 MB, 在所有 Python 提交中击败了98.21%的用户
"""
