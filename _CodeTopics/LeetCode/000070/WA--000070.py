class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        """
        # 估计最朴素的递归会超时，我来试试。。。
        # 其实不用提交就知道了，testcase自己填个100去试直接就超时了，但是还是提交下。
        # 另外，试出来了最大的n为35，输出为14930352。n=36时试了好几次都超时。。。
        """

        # n等于0时返回1不是我杜撰的，是我填了个输入0试出来的。
        # 所以可见官方就默认了0个台阶也得有一种走法。。。。
        if n == 0 or n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)
            
"""
# https://leetcode-cn.com/submissions/detail/77597080/

16 / 45 个通过测试用例
状态：超出时间限制

最后执行的输入：38
"""
