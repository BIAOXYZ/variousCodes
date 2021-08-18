class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """

        # 参考官方动态规划实现

        MOD = 10**9 + 7
        dp = [[[0 for n_recent_Late in range(3)] for n_Absent in range(2)] for day in range(n+1)]
        dp[0][0][0] = 1

        for day in range(1, n+1):
            # case P
            for n_Absent in range(2):
                for n_recent_Late in range(3):
                    dp[day][n_Absent][0] = (dp[day][n_Absent][0] + dp[day-1][n_Absent][n_recent_Late]) % MOD

            # case A
            for n_recent_Late in range(3):
                dp[day][1][0] = (dp[day][1][0] + dp[day-1][0][n_recent_Late]) % MOD

            # case L
            for n_Absent in range(2):
                for n_recent_Late in range(1, 3):
                    dp[day][n_Absent][n_recent_Late] = (dp[day][n_Absent][n_recent_Late] + dp[day-1][n_Absent][n_recent_Late-1]) % MOD
        
        res = 0
        for n_Absent in range(2):
            for n_recent_Late in range(3):
                res += dp[n][n_Absent][n_recent_Late]
        return res % MOD
        
"""
https://leetcode-cn.com/submissions/detail/208561124/

59 / 59 个通过测试用例
状态：通过
执行用时: 6628 ms
内存消耗: 67.8 MB

执行用时：6628 ms, 在所有 Python 提交中击败了7.69%的用户
内存消耗：67.8 MB, 在所有 Python 提交中击败了7.69%的用户
"""
