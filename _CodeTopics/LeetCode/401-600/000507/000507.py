class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """

        if num == 1:
            return False

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
https://leetcode-cn.com/submissions/detail/253660316/

执行用时：24 ms, 在所有 Python 提交中击败了58.67%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了78.67%的用户
通过测试用例：
98 / 98
"""
