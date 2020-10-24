class Solution(object):
    def videoStitching(self, clips, T):
        """
        :type clips: List[List[int]]
        :type T: int
        :rtype: int
        """
        
        # 动态规划

        inf = float("inf")
        dp = [0] + [inf for i in range(T)]

        for i in range(1, T+1):
            for clip in clips:
                if clip[0] < i and clip[1] >= i:
                    dp[i] = min(dp[i], dp[clip[0]] + 1)
        
        return -1 if dp[T] == inf else dp[T]
        
"""
https://leetcode-cn.com/submissions/detail/118351517/

52 / 52 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 12.8 MB

执行用时：24 ms, 在所有 Python 提交中击败了43.37%的用户
内存消耗：12.8 MB, 在所有 Python 提交中击败了5.26%的用户
"""
