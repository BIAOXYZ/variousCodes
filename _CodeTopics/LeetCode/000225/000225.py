class MyStack(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.stack.pop()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.stack[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if not self.stack:
            return True
        return False

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

"""
https://leetcode-cn.com/submissions/detail/109365867/

16 / 16 个通过测试用例
状态：通过
执行用时: 32 ms
内存消耗: 12.6 MB

执行用时：32 ms, 在所有 Python 提交中击败了9.11%的用户
内存消耗：12.6 MB, 在所有 Python 提交中击败了17.93%的用户
"""
