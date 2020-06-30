class CQueue(object):

    def __init__(self):
        self.stackin, self.stackout = [], []

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stackin.append(value)

    def deleteHead(self):
        """
        :rtype: int
        """
        if self.stackout == [] and self.stackin == []:
            return -1

        if self.stackout == []:
            while self.stackin != []:
                self.stackout.append(self.stackin.pop())
        
        return self.stackout.pop()


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()

"""
https://leetcode-cn.com/submissions/detail/83459694/

55 / 55 个通过测试用例
状态：通过
执行用时：1644 ms
内存消耗：17.4 MB
"""
"""
# 为啥内存总是击败100%。。。这个比上一个消耗内存还多啊。。。上一个是17.3 MB

执行用时：1644 ms, 在所有 Python 提交中击败了89.11%的用户
内存消耗：17.4 MB, 在所有 Python 提交中击败了100.00%的用户
"""
