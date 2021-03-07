class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """

        # 跟官方答案类似，双重dp，区别就是第一重dp写法不一样。我的两个for循环range更正常些。
        # 此外，if分支其实我也可以像答案一样省略掉（因为dp初始化时候都是True），但是为了逻辑更清晰，还是分开。

        length = len(s)
        # 注意这里的 dp[i][i] 包含了末尾 j 对应的字符，也就是其实是左闭右闭的。
        dp = [[True for _ in range(length)] for _ in range(length)]
        for i in range(length):
            for j in range(i+1, length):
                # 也就是长度为2的子串（长度为1的就不用额外判断了）
                if j - i == 1:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = dp[i+1][j-1] and (s[i] == s[j])
        
        dp2 = [float("inf")] * length
        for i in range(length):
            if dp[0][i]:
                dp2[i] = 0
            else:
                for j in range(i):
                    if dp[j+1][i]:
                        dp2[i] = min(dp2[i], dp2[j] + 1)     
        return dp2[length-1]
        
"""
https://leetcode-cn.com/submissions/detail/152335567/

17 / 29 个通过测试用例
状态：解答错误

输入：
"cabababcbc"
输出：
0
预期：
3
"""
