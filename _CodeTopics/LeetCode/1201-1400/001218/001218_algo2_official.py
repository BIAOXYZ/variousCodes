class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """

        # 官方答案这个dp还是挺巧的，只需要线性复杂度。

        dp = defaultdict(int)
        for num in arr:
            dp[num] = dp[num - difference] + 1
        return max(dp.values())
        
"""
https://leetcode-cn.com/submissions/detail/235621504/

执行用时：80 ms, 在所有 Python 提交中击败了93.33%的用户
内存消耗：21.7 MB, 在所有 Python 提交中击败了33.33%的用户
通过测试用例：
39 / 39
"""
