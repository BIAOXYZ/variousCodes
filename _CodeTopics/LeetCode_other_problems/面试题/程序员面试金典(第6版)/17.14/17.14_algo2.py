import heapq
class Solution(object):
    def smallestK(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """

        heapq.heapify(arr)
        res = []
        for i in range(k):
            res.append(heapq.heappop(arr))
        return res
        
"""
https://leetcode-cn.com/submissions/detail/214487023/

29 / 29 个通过测试用例
状态：通过
执行用时: 124 ms
内存消耗: 19.4 MB

执行用时：124 ms, 在所有 Python 提交中击败了34.92%的用户
内存消耗：19.4 MB, 在所有 Python 提交中击败了53.44%的用户
"""
