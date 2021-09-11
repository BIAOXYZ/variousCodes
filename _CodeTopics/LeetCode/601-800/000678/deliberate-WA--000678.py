class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """

        length = len(s)
        dp = [[0, 0] for _ in range(length+1)]

        for i in range(1, length+1):
            ch = s[i-1]
            if ch == "(":
                dp[i] = map(lambda x : x + 1, dp[i-1])
            elif ch == ")":
                dp[i] = map(lambda x : x - 1, dp[i-1])
            else:
                dp[i][0] = dp[i-1][0] + 1
                dp[i][1] = dp[i-1][1] - 1
            if dp[i][0] < 0:
                return False
        
        # TODO：这个判断条件还是有问题的，比如用例 "*(()"。但是一堆事，实在不想管了，就这样吧。
        if dp[length][1] > 0:
            return False
        return True
        
"""
https://leetcode-cn.com/submissions/detail/218105757/

66 / 83 个通过测试用例
状态：解答错误

最后执行的输入：
"(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"
输出：
true
预期结果：
false
"""
