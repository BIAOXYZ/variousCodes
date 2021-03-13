class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.modulus = 769
        self.hm = [[] for _ in range(self.modulus)]

    def hash_value(self, key):
        return key % self.modulus

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        h = self.hash_value(key)
        for kvPair in self.hm[h]:
            if kvPair[0] == key:
                kvPair[1] = value
                return
        self.hm[h].append([key, value])

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        h = self.hash_value(key)
        for kvPair in self.hm[h]:
            if kvPair[0] == key:
                return kvPair[1]
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        h = self.hash_value(key)
        for kvPair in self.hm[h]:
            if kvPair[0] == key:
                self.hm[h].remove(kvPair)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

"""
https://leetcode-cn.com/submissions/detail/154836498/

36 / 36 个通过测试用例
状态：通过
执行用时: 184 ms
内存消耗: 17.9 MB

执行用时：184 ms, 在所有 Python3 提交中击败了98.63%的用户
内存消耗：17.9 MB, 在所有 Python3 提交中击败了64.96%的用户
"""
