class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hm = dict()

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.hm[key] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        return self.hm.get(key, -1)

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key in self.hm:
            del self.hm[key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

"""
https://leetcode-cn.com/submissions/detail/154832300/

36 / 36 个通过测试用例
状态：通过
执行用时: 160 ms
内存消耗: 17.3 MB

执行用时：160 ms, 在所有 Python3 提交中击败了99.80%的用户
内存消耗：17.3 MB, 在所有 Python3 提交中击败了93.11%的用户
"""
