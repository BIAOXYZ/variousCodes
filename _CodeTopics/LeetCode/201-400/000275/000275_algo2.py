class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        length = len(citations)
        left, right = 0, length - 1
        res = 0
        while left <= right:
            mid = left + (right - left) / 2
            if citations[mid] >= length - mid:
                res = length - mid
                right = mid - 1
            else:
                left = mid + 1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/194685657/

83 / 83 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 15.3 MB

执行用时：24 ms, 在所有 Python 提交中击败了83.05%的用户
内存消耗：15.3 MB, 在所有 Python 提交中击败了71.19%的用户
"""
"""
估计是测试用例或者平台系统的原因，线性查找比二分查找还快。。。
"""
