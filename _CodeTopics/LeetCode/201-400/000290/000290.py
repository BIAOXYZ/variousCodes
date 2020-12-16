class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        lis = s.split()
        if len(pattern) != len(lis):
            return False
        
        dic = {}
        alreadyUsedValue = set([])
        for i in range(len(pattern)):
            if dic.has_key(pattern[i]):
                if lis[i] != dic[pattern[i]]:
                    return False
            else:
                if lis[i] in alreadyUsedValue:
                    return False
                dic[pattern[i]] = lis[i]
                alreadyUsedValue.add(lis[i])
        return True
        
"""
https://leetcode-cn.com/submissions/detail/131479650/

36 / 36 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13.1 MB

执行用时：20 ms, 在所有 Python 提交中击败了51.33%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了9.62%的用户
"""
