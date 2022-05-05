from collections import deque
class RecentCounter:

    def __init__(self):
        self.q = deque([])

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

"""
https://leetcode-cn.com/submissions/detail/309735484/

执行用时：
196 ms
, 在所有 Python3 提交中击败了
100.00%
的用户
内存消耗：
19.7 MB
, 在所有 Python3 提交中击败了
92.43%
的用户
通过测试用例：
68 / 68
"""
