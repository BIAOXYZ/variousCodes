class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.modulus = 769
        self.hs = [[]] * self.modulus

    def hash_value(self, key):
        return key % self.modulus

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        h = self.hash_value(key)
        if key not in self.hs[h]:
            self.hs[h].append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        h = self.hash_value(key)
        for hashKey in self.hs[h]:
            if hashKey == key:
                self.hs[h].remove(hashKey)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        h = self.hash_value(key)
        return key in self.hs[h]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

"""
https://leetcode-cn.com/submissions/detail/154486143/

32 / 32 个通过测试用例
状态：通过
执行用时: 1840 ms
内存消耗: 17.6 MB

执行用时：1840 ms, 在所有 Python 提交中击败了7.41%的用户
内存消耗：17.6 MB, 在所有 Python 提交中击败了83.33%的用户
"""
