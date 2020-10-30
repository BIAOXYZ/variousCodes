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
        if not self.dic.has_key(val):
            return False
        if val == self.arr[-1]:
            self.arr.pop()
            self.dic[val].pop()
            self.length -= 1
        else:
            ind = self.dic[val][-1]
            val2 = self.arr[-1]
            # 其实交换元素也不必，只要给 ind 位置赋值成 val2 就行。不过为了更易阅读，就这么写吧。
            self.arr[ind], self.arr[-1] = self.arr[-1], self.arr[ind]
            self.arr.pop()
            self.dic[val].pop()
            self.length -= 1
            self.dic[val2].pop(); self.dic[val2].append(ind)
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
https://leetcode-cn.com/submissions/detail/119877562/

10 / 30 个通过测试用例
状态：执行出错

执行出错信息：
Line 43: IndexError: list index out of range
最后执行的输入：
["RandomizedCollection","insert","insert","insert","insert","insert","remove","remove","remove","insert","remove","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom"]
[[],[1],[1],[2],[2],[2],[1],[1],[2],[1],[2],[],[],[],[],[],[],[],[],[],[]]
"""
