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
        """
        if m == 1 or n == 1:
            return 1
        else:          
            return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
        
"""
https://leetcode-cn.com/submissions/detail/129737774/

37 / 62 个通过测试用例
状态：超出时间限制

最后执行的输入：
23
12
"""
