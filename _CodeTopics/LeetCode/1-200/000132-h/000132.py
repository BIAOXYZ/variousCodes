class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """

        # 跟官方答案类似，双重dp。
        # <del> 区别就是第一重dp写法不一样。我的两个for循环range更正常些。</del> --> 改成官方的写法了。。。
        # 此外，if分支其实我也可以像答案一样省略掉（因为dp初始化时候都是True），但是为了逻辑更清晰，还是分开。

        length = len(s)
        # 注意这里的 dp[i][i] 包含了末尾 j 对应的字符，也就是其实是左闭右闭的。
        dp = [[True for _ in range(length)] for _ in range(length)]
        # 结果事实证明这第一重for循环里还必须倒着来，暂时没想明白为啥。。。
        for i in range(length-1,-1,-1):
            for j in range(i+1, length):
                # 也就是长度为2的子串（长度为1的就不用额外判断了）
                if j - i == 1:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = dp[i+1][j-1] and (s[i] == s[j])
        print dp
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
https://leetcode-cn.com/submissions/detail/152336620/

29 / 29 个通过测试用例
状态：通过
执行用时: 1552 ms
内存消耗: 31.2 MB

执行用时：1552 ms, 在所有 Python 提交中击败了5.48%的用户
内存消耗：31.2 MB, 在所有 Python 提交中击败了6.85%的用户
"""
