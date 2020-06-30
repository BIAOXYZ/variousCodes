class CQueue(object):

    def __init__(self):
        self.queue = []

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.queue.append(value)

    def deleteHead(self):
        """
        :rtype: int
        """
        if self.queue != []:
            rt = self.queue[0]
            self.queue.remove(rt)
            return rt
        else:
            return -1


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()

"""
https://leetcode-cn.com/submissions/detail/83273557/

55 / 55 个通过测试用例
状态：通过
执行用时：1620 ms
内存消耗：17.3 MB
"""
"""
执行用时：1620 ms, 在所有 Python 提交中击败了96.86%的用户
内存消耗：17.3 MB, 在所有 Python 提交中击败了100.00%的用户
"""
