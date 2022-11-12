class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """

        ddic = defaultdict(int)
        for i, ch in enumerate(order):
            ddic[ch] = i + 1
        # str 没有 .sort() 方法，只能用更通用的 sorted() 函数，此时排序完出来的是个 list
        return ''.join(sorted(s, key = lambda x : ddic[x]))
        
"""
https://leetcode.cn/submissions/detail/381560005/

执行用时：
12 ms
, 在所有 Python 提交中击败了
97.06%
的用户
内存消耗：
13.2 MB
, 在所有 Python 提交中击败了
17.65%
的用户
通过测试用例：
39 / 39
"""
