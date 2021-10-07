class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        length = len(s)
        if length <= 10:
            return []
        
        dic = {}
        for end in range(10, length+1):
            subStr = s[end-10:end]
            dic[subStr] = dic.setdefault(subStr, 0) + 1
        
        res = []
        for k, v in dic.items():
            if v > 1:
                res.append(k)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/226612166/

31 / 31 个通过测试用例
状态：通过
执行用时: 60 ms
内存消耗: 39.4 MB

执行用时：60 ms, 在所有 Python 提交中击败了28.27%的用户
内存消耗：39.4 MB, 在所有 Python 提交中击败了5.23%的用户
"""
