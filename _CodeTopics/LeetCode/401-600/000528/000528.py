import random
import bisect
class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.prefixSum = [w[0]]
        for i in range(1, len(w)):
            self.prefixSum.append(self.prefixSum[-1] + w[i])

    def pickIndex(self):
        """
        :rtype: int
        """
        num = random.randint(1, self.prefixSum[-1])
        ind = bisect.bisect_left(self.prefixSum, num)
        return ind


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

"""
https://leetcode-cn.com/submissions/detail/212810879/

57 / 57 个通过测试用例
状态：通过
执行用时: 416 ms
内存消耗: 18.1 MB

执行用时：416 ms, 在所有 Python 提交中击败了94.44%的用户
内存消耗：18.1 MB, 在所有 Python 提交中击败了5.55%的用户
"""
