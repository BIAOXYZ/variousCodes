class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        """
        思路：动态规划。主要的难点就是递推公式略有些绕，相通了也就还好。
        """

        if not s:
            return 0
        
        length = len(s)
        if length == 1:
            return 0

        dp = [0] * length
        dp[1] = 2 if s[0] == '(' and s[1] == ')' else 0
        
        for i in range(2,length):
            if s[i] == '(':
                dp[i] = 0
            else:   # 此时 s[i] 等于 ')'
                if s[i-1] == '(':
                    dp[i] = dp[i-2] + 2
                else:   # 此时 s[i-1] 等于 ')'，也就是这个题里最复杂的部分
                    if s[i-dp[i-1]-1] == '(':
                        # 这里需要判断下不能超出边界，否则输入 "(()))())(" 就会返回8。
                        # 而正确答案应该是4。
                        if i-dp[i-1]-1 >= 0: dp[i] = (dp[i-1] + 2) + dp[i-dp[i-1]-2]
                        else: dp[i] = 0   # 这个else当然不写也行，我是刻意写一下，使对比更鲜明。
                    else:
                        dp[i] = 0
        return max(dp)
        
"""
https://leetcode-cn.com/submissions/detail/85706674/

230 / 230 个通过测试用例
状态：通过
执行用时：36 ms
内存消耗：13.2 MB
"""
"""
执行用时：36 ms, 在所有 Python 提交中击败了89.60%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了16.67%的用户
"""
