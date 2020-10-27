class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        dic = dict()
        for num in arr:
            if dic.has_key(num):
                dic[num] += 1
            else:
                dic[num] = 1
        return len(dic.values()) == len(set(dic.values()))
        
"""
https://leetcode-cn.com/submissions/detail/119114238/

63 / 63 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13.2 MB

执行用时：20 ms, 在所有 Python 提交中击败了90.54%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了5.55%的用户
"""
