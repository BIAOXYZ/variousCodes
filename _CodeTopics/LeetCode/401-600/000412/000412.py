class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        res = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 != 0:
                res.append("Fizz")
            elif i % 3 != 0 and i % 5 == 0:
                res.append("Buzz")
            elif i % 15 == 0:
                res.append("FizzBuzz")
            else:
                res.append(str(i))
        return res
        
"""
https://leetcode-cn.com/submissions/detail/228327110/

8 / 8 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 14.1 MB

执行用时：16 ms, 在所有 Python 提交中击败了87.83%的用户
内存消耗：14.1 MB, 在所有 Python 提交中击败了5.27%的用户
"""
