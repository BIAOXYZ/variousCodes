class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """

        # 先写个肯定超时的

        def number_of_one(num):
            res = 0
            while num > 0:
                if num % 10 == 1:
                    res += 1
                num /= 10
            return res
        
        res = 0
        for i in range(1, n+1):
            res += number_of_one(i)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/206358352/

34 / 38 个通过测试用例
状态：超出时间限制

最后执行的输入：
3184191
"""
