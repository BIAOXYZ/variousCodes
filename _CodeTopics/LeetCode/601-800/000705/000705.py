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
        if key in self.hs:
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
https://leetcode-cn.com/submissions/detail/154481010/

32 / 32 个通过测试用例
状态：通过
执行用时: 464 ms
内存消耗: 18.2 MB

执行用时：464 ms, 在所有 Python 提交中击败了87.96%的用户
内存消耗：18.2 MB, 在所有 Python 提交中击败了74.07%的用户
"""
