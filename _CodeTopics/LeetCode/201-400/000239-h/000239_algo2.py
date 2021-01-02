import heapq
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # 这次用堆/优先队列实现。
        # 由于python的heapq里用的是小根堆，但是这里需要的是大根堆。所以往里push元素的时候要push相反数。
        # 此外为了判断当前最大的元素是否合法，干脆堆里的元素还包含index。

        res = []
        length = len(nums)

        minhp = [[-nums[i], i] for i in range(k)]
        heapq.heapify(minhp)
        res.append(-minhp[0][0])

        for i in range(k, length):
            heapq.heappush(minhp, [-nums[i], i])
            while minhp[0][1] < i - k + 1:
                heapq.heappop(minhp)
            res.append(-minhp[0][0])

        return res
        
"""
https://leetcode-cn.com/submissions/detail/135388101/

60 / 60 个通过测试用例
状态：通过
执行用时: 940 ms
内存消耗: 38.5 MB

执行用时：940 ms, 在所有 Python 提交中击败了14.65%的用户
内存消耗：38.5 MB, 在所有 Python 提交中击败了5.15%的用户
"""
