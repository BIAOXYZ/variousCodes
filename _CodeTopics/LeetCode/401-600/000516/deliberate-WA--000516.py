class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """

        length = len(s)
        """
        # dp[i][j] 的含义是：恰好以 s[i] 开头，以 s[j] 结尾的最回文长子序列的长度。在这种情况下，递推公式为：
        ## 如果首尾字符不相等，那么肯定是0；如果相等，那么要么是2，要么是 2 + dp[i+1][j-1]。
        
        # 可惜，这样做还是有问题，以输入 "bbbab" 为例：最长回文子序列是四个b，但是如果按这种dp方式，
        ## 第一个b和最后一个b算长度2，它们中间的 "bba" 是0！！！
        
        # 所以应该是要令 dp[i][j] 表示 s[i] 和 s[j] 之间的最长回文子序列的长度，但是不是必须严格让这俩做开头和结尾。
        """
        dp = [[0 for _ in range(length)] for _ in range(length)]
        for i in range(length):
            dp[i][i] = 1
        
        res = 1
        for start in range(length-1):
            for end in range(start+1, length):
                if s[end] != s[start]:
                    continue
                else:
                    if start == end - 1:
                        dp[start][end] = 2
                    else:
                        dp[start][end] = 2 + dp[start+1][end-1]
                res = max(res, dp[start][end])
        return res
        
"""
https://leetcode-cn.com/submissions/detail/205973106/

26 / 86 个通过测试用例
状态：解答错误

最后执行的输入：
"bbbab"
输出：
3
预期结果：
4
"""
