class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.lis = nums
        self.ind = k

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.lis.append(val)
        self.lis.sort(reverse=True)
        return self.lis[self.ind - 1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

"""
https://leetcode-cn.com/submissions/detail/145312705/

10 / 10 个通过测试用例
状态：通过
执行用时: 1368 ms
内存消耗: 17.2 MB
提交时间：几秒前

执行用时：1368 ms, 在所有 Python 提交中击败了18.24%的用户
内存消耗：17.2 MB, 在所有 Python 提交中击败了11.95%的用户
"""
