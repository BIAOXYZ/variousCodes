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
            for subd in dic[currId]:
                stk.append(subd)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/173751452/

1 / 108 个通过测试用例
状态：执行出错

执行出错信息：
TypeError: 'Employee' object is not iterable
    for subd in dic[currId]:
Line 30 in getImportance (Solution.py)
    ret = Solution().getImportance(param_1, param_2)
Line 128 in __helper__ (Solution.py)
    param_1, param_2, num_repeat
Line 159 in _driver (Solution.py)
    _driver()
Line 169 in <module> (Solution.py)
最后执行的输入：
[[1,5,[2,3]],[2,3,[]],[3,3,[]]]
1
"""
