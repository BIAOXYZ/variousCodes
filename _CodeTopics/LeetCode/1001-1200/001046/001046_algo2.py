import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        # 大根堆实现。由于python的heapq只有小根堆，所以一般采用对元素取反的策略。

        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            weight1 = -heapq.heappop(stones)
            weight2 = -heapq.heappop(stones)
            if weight1 - weight2 != 0:
                heapq.heappush(stones, weight2 - weight1)
        if len(stones) == 0:
            return 0
        else:
            return -heapq.heappop(stones)
        
"""
https://leetcode-cn.com/submissions/detail/184915412/

70 / 70 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 13.1 MB

执行用时：24 ms, 在所有 Python 提交中击败了45.76%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了28.25%的用户
"""
