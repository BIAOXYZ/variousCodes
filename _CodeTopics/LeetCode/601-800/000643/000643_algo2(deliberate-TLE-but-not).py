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
        res = -float('inf')

        for i in range(n-k+1):
            res = max(res, sum(nums[i:i+k]))
        return res * 1.0 / k
        
"""
https://leetcode-cn.com/submissions/detail/143539629/

123 / 123 个通过测试用例
状态：通过
执行用时: 7872 ms
内存消耗: 15.8 MB

执行用时：7872 ms, 在所有 Python 提交中击败了41.35%的用户
内存消耗：15.8 MB, 在所有 Python 提交中击败了56.39%的用户
"""
"""
滑动窗口写完后不信邪，就用暴力穷举写一下。结果并没有像答案说的那样会超时。
其实不但没超时，时间上还超过了百分之四十多的人，可见暴力的O(kn)相比滑动窗口的O(n)也还好。
"""
