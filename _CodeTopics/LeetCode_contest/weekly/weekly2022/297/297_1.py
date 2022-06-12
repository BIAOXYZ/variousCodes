class Solution(object):
    def calculateTax(self, brackets, income):
        """
        :type brackets: List[List[int]]
        :type income: int
        :rtype: float
        """
        
        res = 0
        n = len(brackets)
        total = 0
        
        if income <= brackets[0][0]:
            return income * brackets[0][1] / 100.0
        else:
            res += brackets[0][0] * brackets[0][1] / 100.0
        
        i = 1
        while i < n:
            cur_upper, cur_percent = brackets[i][0], brackets[i][1] / 100.0
            pre_upper, pre_percent = brackets[i-1][0], brackets[i-1][1] / 100.0
            real_upper = cur_upper - pre_upper
            if income <= cur_upper:
                res += (income - pre_upper) * cur_percent
                break
            else:
                res += real_upper * cur_percent
            i += 1
        return res
    
"""
https://leetcode.cn/submissions/detail/324324895/

225 / 225 个通过测试用例
状态：通过
执行用时: 8 ms
内存消耗: 13.1 MB
"""
