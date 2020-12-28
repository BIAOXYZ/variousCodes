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
        
        return (summation - biggest - smallest) / (length - 2)
    
"""
https://leetcode-cn.com/contest/biweekly-contest-29/submissions/detail/82507994/

20 / 43 个通过测试用例
	状态：解答错误

输入： [48000,59000,99000,13000,78000,45000,31000,17000,39000,37000,93000,77000,33000,28000,4000,54000,67000,6000,1000,11000]
输出： 41111.00000
预期： 41111.11111
"""
