class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """

        flag = 1 if s[0] == 'L' else -1
        res = 0
        for i in range(1, len(s)):
            if s[i] == 'L':
                flag += 1
            else:
                flag -= 1
            if flag == 0:
                res += 1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/216089769/

40 / 40 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13.2 MB

执行用时：20 ms, 在所有 Python 提交中击败了59.50%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了15.70%的用户
"""
