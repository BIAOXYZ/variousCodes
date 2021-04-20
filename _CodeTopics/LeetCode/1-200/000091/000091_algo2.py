class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        # 用回溯算法是不行了，看来必须动态规划了。
        # dp数组中的 dp[i] 表示以 s[i] 结尾的编码（或者说字符串）能合法的解码的总数。

        def is_legal_encode(s):
            if s[0] == "0" or int(s) > 26:
                return 0
            else:
                return 1

        length = len(s)
        dp = [0 for _ in range(length)]

        for i in range(length):
            if i == 0:
                dp[i] = is_legal_encode(s[i])
            elif i == 1:
                dp[i] = dp[i-1]*is_legal_encode(s[i]) + is_legal_encode(s[i-1:i+1])
            else:
                dp[i] = dp[i-1]*is_legal_encode(s[i]) + dp[i-2]*is_legal_encode(s[i-1:i+1])
        
        return dp[length-1]
        
"""
https://leetcode-cn.com/submissions/detail/170241695/

269 / 269 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 13 MB

执行用时：24 ms, 在所有 Python 提交中击败了58.76%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了69.44%的用户
"""
