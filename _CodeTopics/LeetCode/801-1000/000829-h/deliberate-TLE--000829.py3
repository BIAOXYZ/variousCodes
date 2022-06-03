class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:

        # trivial 的做法当然是按一个数字和为n，两个数字和为n，... 一直到 m 个数字和为 n 来计算。
        # 假设开头的数字是 a，于是有 (a + a + m - 1) * m // 2 == n，只要算算这样的 a 是否存在即可。
        # 但是这种肯定会超时，不过打算先写一下。

        res = 1
        m = 2
        while m < n:
            if 2 * n % m == 0:
                quotient = 2 * n // m
                if (quotient + 1 - m) % 2 == 0 and (quotient + 1 - m) // 2 >= 1:
                    res += 1
            m += 1
        return res
        
"""
https://leetcode.cn/submissions/detail/321367267/

131 / 170 个通过测试用例
状态：超出时间限制

最后执行的输入：
72316829
"""
