class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        
        res = 0
        for op in operations:
            if op[1] == '+':
                res += 1
            else:
                res -= 1
        return res
    
"""
https://leetcode-cn.com/submissions/detail/220955803/

259 / 259 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 13.1 MB
"""
