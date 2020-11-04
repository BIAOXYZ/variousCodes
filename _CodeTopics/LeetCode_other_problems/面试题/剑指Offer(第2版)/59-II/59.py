class MaxQueue(object):

    def __init__(self):
        self.arr = []
        self.quickFindMax = []

    def max_value(self):
        """
        :rtype: int
        """
        if not self.arr:
            return -1
        return self.quickFindMax[0]

    def push_back(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.arr.append(value)
        while self.quickFindMax and self.quickFindMax[-1] < value:
            self.quickFindMax.pop()
        self.quickFindMax.append(value)

    def pop_front(self):
        """
        :rtype: int
        """
        if not self.arr:
            return -1
        # 其实用list的remove方法来代替pop(0)删除第一个元素时间复杂度好像还是O(n)。
        # 不过这里就是表示一下吧。。。表示知道这点，但是又不想用deque或者Queue。
        res = self.arr[0]; self.arr.remove(res)
        if res == self.quickFindMax[0]:
            self.quickFindMax.remove(res)
        return res

# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()

"""
https://leetcode-cn.com/submissions/detail/120988143/

34 / 34 个通过测试用例
状态：通过
执行用时: 624 ms
内存消耗: 17.6 MB

执行用时：624 ms, 在所有 Python 提交中击败了99.70%的用户
内存消耗：17.6 MB, 在所有 Python 提交中击败了5.22%的用户
"""
