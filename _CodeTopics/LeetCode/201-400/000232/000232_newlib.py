from collections import deque
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque([])

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.queue.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.queue.popleft()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.queue[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.queue == deque([])


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

"""
https://leetcode-cn.com/submissions/detail/151205906/

20 / 20 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 12.9 MB

执行用时：16 ms, 在所有 Python 提交中击败了78.47%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了74.50%的用户
"""
