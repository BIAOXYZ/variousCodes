class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        # 用动态规划把所有子串是不是回文先预处理好。

        length = len(s)
        # 注意这里的 dp[i][i] 包含了末尾 j 对应的字符，也就是其实是左闭右闭的。
        dp = [[True for _ in range(length)] for _ in range(length)]
        # 第一重for循环必须倒序遍历！原因可以参见 LC132 的 README。
        for i in range(length-1,-1,-1):
            for j in range(i+1, length):
                # 也就是长度为2的子串（长度为1的就不用额外判断了）
                if j - i == 1:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = dp[i+1][j-1] and (s[i] == s[j])

        if not s:
            return [[]]
        res = []
        for i in range(1, len(s)+1):
            currStr = s[:i]
            if dp[0][i-1]:
                for lis in self.partition(s[i:]):
                    res.append([currStr] + lis)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/152759559/

32 / 32 个通过测试用例
状态：通过
执行用时: 372 ms
内存消耗: 43.1 MB

执行用时：372 ms, 在所有 Python 提交中击败了5.05%的用户
内存消耗：43.1 MB, 在所有 Python 提交中击败了94.47%的用户
"""
