class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        
        length = len(salary)
        biggest, smallest = max(salary), min(salary)
        
        summation = 0
        for i in range(length):
            summation += salary[i]
        
        return (summation - biggest - smallest) / float(length - 2)
    
"""
https://leetcode-cn.com/contest/biweekly-contest-29/submissions/detail/82512107/

43 / 43 个通过测试用例
	状态：通过
执行用时：8 ms
内存消耗：12.5 MB
"""
