class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hs = set()

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.hs.add(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.hs.remove(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return key in self.hs


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

"""
https://leetcode-cn.com/submissions/detail/154479548/

1 / 32 个通过测试用例
状态：执行出错

执行出错信息：
Line 21: KeyError: 19
最后执行的输入：
["MyHashSet","add","remove","add","remove","remove","add","add","add","add","remove"]
[[],[9],[19],[14],[19],[9],[0],[3],[4],[0],[9]]
"""
