class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """

        # 这题第一反应就是动态规划，因为之前有类似的。但是鉴于目前这个月前面的几天都是滑动窗口，
        # 顺着滑动窗口的思路想了下就想到了：一共拿走k个，那么最后留下 length - k 个，并且肯定是连续的。
        # 所以等价于求和最小的连续 length-k 个数的和。

        total = sum(cardPoints)
        length = len(cardPoints)
        if k == length:
            return total
        
        n = length - k
        minSum = currSum = sum(cardPoints[:n])
        for i in range(1, length - n + 1):
            currSum += cardPoints[i+n-1] - cardPoints[i-1]
            minSum = min(minSum, currSum)
        return total - minSum
        
"""
https://leetcode-cn.com/submissions/detail/144069181/

40 / 40 个通过测试用例
状态：通过
执行用时: 56 ms
内存消耗: 19.8 MB

执行用时：56 ms, 在所有 Python 提交中击败了91.38%的用户
内存消耗：19.8 MB, 在所有 Python 提交中击败了31.04%的用户
"""
