class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """

        s = str(bin(num))[2:]
        res = ''
        for ch in s:
            if ch == '0':
                res += '1'
            else:
                res += '0'
        return int(res, 2)
        
"""
https://leetcode-cn.com/submissions/detail/229815633/

149 / 149 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13.1 MB

执行用时：20 ms, 在所有 Python 提交中击败了31.96%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了35.05%的用户
"""
