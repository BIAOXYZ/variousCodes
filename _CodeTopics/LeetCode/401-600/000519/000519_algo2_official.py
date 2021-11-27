import random
class Solution(object):

    # 参见官方答案。除了压缩（二维）坐标到单个数之外，更核心的是交换操作。

    def __init__(self, m, n):
        """
        :type m: int
        :type n: int
        """
        self.m = m
        self.n = n
        self.total = m * n
        self.map = {}

    def flip(self):
        """
        :rtype: List[int]
        """
        x = random.randint(0, self.total - 1)
        self.total -= 1
        # 查找位置 x 对应的映射
        idx = self.map.get(x, x)
        # 将位置 x 对应的映射设置为位置 total 对应的映射
        self.map[x] = self.map.get(self.total, self.total)
        return [idx // self.n, idx % self.n]

    def reset(self):
        """
        :rtype: None
        """
        self.total = self.m * self.n
        self.map.clear()


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()

"""
https://leetcode-cn.com/submissions/detail/242872657/

执行用时：60 ms, 在所有 Python 提交中击败了50.00%的用户
内存消耗：13.4 MB, 在所有 Python 提交中击败了50.00%的用户
通过测试用例：
20 / 20
"""
