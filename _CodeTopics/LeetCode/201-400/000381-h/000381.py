import random
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.dic = {}
        self.length = 0

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.arr.append(val)
        self.length += 1
        if not self.dic.has_key(val) or self.dic[val] == []:
            self.dic[val] = [self.length - 1]
            return True
        else:
            self.dic[val].append(self.length - 1)
            return False

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if not self.dic.has_key(val) or self.dic[val] == []:
            return False
        if val == self.arr[-1]:
            self.dic[val].remove(self.length-1)
        else:
            ind = self.dic[val][-1]
            val2 = self.arr[-1]
            self.arr[ind], self.arr[-1] = self.arr[-1], self.arr[ind]
            self.dic[val].pop()
            self.dic[val2].remove(self.length-1); self.dic[val2].append(ind)
        self.arr.pop()
        self.length -= 1
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return random.choice(self.arr)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

"""
https://leetcode-cn.com/submissions/detail/119878581/

30 / 30 个通过测试用例
状态：通过
执行用时: 272 ms
内存消耗: 18.1 MB

执行用时：272 ms, 在所有 Python 提交中击败了100.00%的用户
内存消耗：18.1 MB, 在所有 Python 提交中击败了30.44%的用户
"""
