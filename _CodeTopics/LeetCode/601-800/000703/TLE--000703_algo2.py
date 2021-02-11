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
        return heapq.nlargest(self.ind, self.hp)[-1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

"""
https://leetcode-cn.com/submissions/detail/145315620/

9 / 10 个通过测试用例
状态：超出时间限制
"""
"""
没明白为啥普通的排序都没超时，用堆反而超时了。。。应该还是使用问题。
"""
