class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        dic = {}
        for s in strs:
            tmp = tuple(sorted(s))
            if dic.has_key(tmp):
                dic[tmp].append(s)
            else:
                dic[tmp] = [s]
        return dic.values()
        
"""
https://leetcode-cn.com/submissions/detail/196898218/

101 / 101 个通过测试用例
状态：通过
执行用时: 44 ms
内存消耗: 17.2 MB

执行用时：44 ms, 在所有 Python 提交中击败了77.14%的用户
内存消耗：17.2 MB, 在所有 Python 提交中击败了17.14%的用户
"""
