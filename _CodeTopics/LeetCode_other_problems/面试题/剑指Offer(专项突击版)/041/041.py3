class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.n = size
        self.lis = deque()
        self.sum = 0

    def next(self, val: int) -> float:
        if len(self.lis) < self.n:
            self.lis.append(val)
            self.sum += val
            return self.sum / len(self.lis)
        else:
            elem = self.lis.popleft()
            self.sum -= elem
            self.lis.append(val)
            self.sum += val
            return self.sum / self.n


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

"""
https://leetcode.cn/submissions/detail/337442060/

执行用时：
64 ms
, 在所有 Python3 提交中击败了
83.00%
的用户
内存消耗：
18 MB
, 在所有 Python3 提交中击败了
73.70%
的用户
通过测试用例：
11 / 11
"""
