class MapSum(object):

    def __init__(self):
        self.dic = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        self.dic[key] = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        # 没用字典树，感觉也太简单了，有种要超时的预感。。。但是输入规模确实不大啊。
        res = 0
        for k, v in self.dic.items():
            if k.startswith(prefix):
                res += v
        return res


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

"""
https://leetcode-cn.com/submissions/detail/238385990/

执行用时：20 ms, 在所有 Python 提交中击败了84.00%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了32.00%的用户
通过测试用例：
35 / 35
"""
