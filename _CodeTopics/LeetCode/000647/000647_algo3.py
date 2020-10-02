class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if not s:
            return 0
        
        length = len(s)

        # 动态规划法和中心扩散法在中间推理的时候是类似的，奇数从长度为1的子串出发，
        # 偶数从长度为2的字串出发，不断填充dp二维数组的相应的格子。
        # 下面首先把长度为1的字串和2的字串对于的dp格子填好。
        dp = [[0 for i in range(length+1)] for j in range(length+1)]
        for i in range(length):
            if i + 1 <= length:
                dp[i][i+1] = 1
            if i + 2 <= length and s[i] == s[i+1]:
                dp[i][i+2] = 1
        
        # 从长度为3的字串开始接着填dp的格子。
        for subStrLen in range(3, length+1):
            for i in range(length-subStrLen+1):
                if dp[i+1][i+subStrLen-1] == 1 and s[i] == s[i+subStrLen-1]:
                    dp[i][i+subStrLen] = 1
        return sum(dp[i][j] for i in range(length+1) for j in range(length+1))
        
"""
https://leetcode-cn.com/submissions/detail/112866223/

130 / 130 个通过测试用例
状态：通过
执行用时: 344 ms
内存消耗: 21 MB

执行用时：344 ms, 在所有 Python 提交中击败了19.82%的用户
内存消耗：21 MB, 在所有 Python 提交中击败了8.44%的用户
"""
