class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        dic = {}
        for string in strs:
            k = tuple(sorted(list(string)))
            if dic.has_key(k):
                dic[k].append(string)
            else:
                dic[k] = [string]
        return dic.values()
        
"""
https://leetcode-cn.com/submissions/detail/130846935/

112 / 112 个通过测试用例
状态：通过
执行用时: 60 ms
内存消耗: 17 MB

执行用时：60 ms, 在所有 Python 提交中击败了43.46%的用户
内存消耗：17 MB, 在所有 Python 提交中击败了44.32%的用户
"""
