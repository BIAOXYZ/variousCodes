class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        """
        # 类似于最经典的`LC70 爬楼梯`、`LC322 零钱兑换`等。
        # 这里准备先写一个（可能）超时的：也就是先试试“自顶向下”的记忆化搜索。
        # 但其实就此题本身来说，第一反应还是“自底向上”的动态规划更直观些。
        """

        """
        # 本来是按(0,0)开始的，但是发现不好写，还是按(1,1)开始最简单直观。
        # 另外我不明白为啥起点处不是需要0步，而是需要1步，本来我的代码还有下面这个if分支。
        # 但是输入 1 1 时，答案返回的是1，我觉得不对。。。
        if m == 1 and n == 1:
            return 0
        
        我非得提交下试试不可。。。看看输入 1 1 时会WA，还是跟前一个（deliberate-TLE--000062.py）
        一样TLE。。。
        """
        if m == 1 and n == 1:
            return 0
        elif m == 1 or n == 1:
            return 1
        else:          
            return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
        
"""
https://leetcode-cn.com/submissions/detail/129738807/

36 / 62 个通过测试用例
状态：解答错误

输入：
1
1
输出：
0
预期：
1
"""
"""
补：还真是跟我预期的一样：1 1 这个输入和答案不对。但是我依然认为输入 1 1 时结果应该是0，因为机器人就在起点啊。
    除非是为了DP算法实现的一致性（毕竟我这里用的是记忆化搜索）？不过等会写了DP的就知道了。
"""
