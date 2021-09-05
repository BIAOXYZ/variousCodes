# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """

        while True:
            row = rand7()
            col = rand7()
            idx = (row - 1) * 7 + col
            if idx <= 40:
                return 1 + (idx - 1) % 10
        
"""
https://leetcode-cn.com/submissions/detail/215596859/

12 / 12 个通过测试用例
状态：通过
执行用时: 368 ms
内存消耗: 17.6 MB

执行用时：368 ms, 在所有 Python 提交中击败了30.17%的用户
内存消耗：17.6 MB, 在所有 Python 提交中击败了92.24%的用户
"""
