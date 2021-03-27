import heapq
class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """

        if not arr:
            return []
        
        heapq.heapify(arr)
        res = []
        for i in range(k):
            res.append(heapq.heappop(arr))
        return res
        
"""
https://leetcode-cn.com/submissions/detail/160706712/

38 / 38 个通过测试用例
状态：通过
执行用时: 192 ms
内存消耗: 14.4 MB

执行用时：192 ms, 在所有 Python 提交中击败了20.71%的用户
内存消耗：14.4 MB, 在所有 Python 提交中击败了36.51%的用户
"""
