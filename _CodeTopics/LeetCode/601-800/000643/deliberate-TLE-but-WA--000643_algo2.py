class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        # 滑动窗口做完后，发现答案里说普通的穷举会超时。滑动窗口复杂度可以认为是O(n)，
        # 普通穷举也就O(kn)，我感觉不一定会超时吧？决定试试。

        n = len(nums)
        res = 0

        for i in range(n-k+1):
            res = max(res, sum(nums[i:i+k]))
        return res * 1.0 / k
        
"""
https://leetcode-cn.com/submissions/detail/143539330/

116 / 123 个通过测试用例
状态：解答错误

输入：
[-1]
1
输出：
0.00000
预期：
-1.00000
"""
