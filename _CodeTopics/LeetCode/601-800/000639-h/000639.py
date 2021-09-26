class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        # 基本参照官方答案，这题主要是复杂，其他意义不大。两个子函数都是抄的，
        # 但是子函数下面的程序逻辑改成了更标准（空间复杂度也更高）的动态规划形式。

        MOD = 10**9 + 7
        def check1digit(ch):
            if ch == "0":
                return 0
            return 9 if ch == "*" else 1
        def check2digits(c0, c1):
            if c0 == c1 == "*":
                return 15
            if c0 == "*":
                return 2 if c1 <= "6" else 1
            if c1 == "*":
                return 9 if c0 == "1" else (6 if c0 == "2" else 0)
            return int(c0 != "0" and int(c0) * 10 + int(c1) <= 26)

        length = len(s)
        if length == 1:
            return check1digit(s[0])
        
        dp = [-1 for _ in range(length)]
        dp[0] = check1digit(s[0])
        dp[1] = dp[0] * check1digit(s[1]) + check2digits(s[0], s[1])
        for i in range(2, length):
            dp[i] = dp[i-1] * check1digit(s[i]) + dp[i-2] * check2digits(s[i-1], s[i])
            dp[i] %= MOD
        return dp[length-1]
        
"""
https://leetcode-cn.com/submissions/detail/223581695/

217 / 217 个通过测试用例
状态：通过
执行用时: 788 ms
内存消耗: 20.4 MB

执行用时：788 ms, 在所有 Python 提交中击败了28.57%的用户
内存消耗：20.4 MB, 在所有 Python 提交中击败了71.43%的用户
"""
