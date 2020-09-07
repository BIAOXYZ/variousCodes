class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # 手动狗头题
        # from： https://leetcode-cn.com/problems/top-k-frequent-elements/solution/qian-k-ge-gao-pin-yuan-su-by-leetcode-solution/580209
        return [num for num, _ in Counter(nums).most_common(k)]
"""
https://leetcode-cn.com/submissions/detail/105784935/

21 / 21 个通过测试用例
状态：通过
执行用时: 44 ms
内存消耗: 14.8 MB
"""
"""
执行用时：44 ms, 在所有 Python 提交中击败了32.18%的用户
内存消耗：14.8 MB, 在所有 Python 提交中击败了38.03%的用户
"""
