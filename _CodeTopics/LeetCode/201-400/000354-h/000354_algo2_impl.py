class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """

        # 和上一个提交（`000354_algo2.py`）唯一的不同点就是求第二个元素的最长递增子序列时用的另一种动态规划。
        # 详情见`000300_impl.py`。

        if not envelopes:
            return 0

        envelopes.sort(key = lambda x : (x[0], -x[1]))
        heightList = [envelope[1] for envelope in envelopes]
        length = len(envelopes)
        dp = [1 for _ in range(length)]

        for i in range(1, length):
            for j in range(i):
                if heightList[j] < heightList[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
        
"""
https://leetcode-cn.com/submissions/detail/150799853/

85 / 85 个通过测试用例
状态：通过
执行用时: 5196 ms
内存消耗: 15.6 MB

执行用时：5196 ms, 在所有 Python 提交中击败了67.10%的用户
内存消耗：15.6 MB, 在所有 Python 提交中击败了5.80%的用户
"""
