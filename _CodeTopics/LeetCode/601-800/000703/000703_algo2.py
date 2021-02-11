import heapq
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.hp = nums
        heapq.heapify(self.hp)
        self.ind = k

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.hp, val)
        # return heapq.nlargest(self.ind, self.hp)[-1]
        # 其实是没必要用上面那句，因为堆里其实只要保持前k个最大的元素就够了。
        while len(self.hp) > self.ind:
            heapq.heappop(self.hp)
        return self.hp[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

"""
https://leetcode-cn.com/submissions/detail/145316270/

10 / 10 个通过测试用例
状态：通过
执行用时: 268 ms
内存消耗: 16.9 MB
提交时间：几秒前

执行用时：268 ms, 在所有 Python 提交中击败了43.40%的用户
内存消耗：16.9 MB, 在所有 Python 提交中击败了59.75%的用户
"""
