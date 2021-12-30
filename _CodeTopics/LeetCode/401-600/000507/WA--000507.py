class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """

        summation = 1
        i = 2
        while i**2 <= num:
            if num % i == 0:
                summation += i
                if i != num / i:
                    summation += num / i
            i += 1
        return summation == num
        
"""
https://leetcode-cn.com/submissions/detail/253659676/

97 / 98 个通过测试用例
状态：解答错误

输入：
1
输出：
true
预期结果：
false
"""
