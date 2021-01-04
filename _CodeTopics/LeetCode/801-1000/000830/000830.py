class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """

        res = []
        num = 1

        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                num += 1
            else:
                if num >= 3:
                    res.append([i-num, i-1])
                num = 1
        if num >= 3:
            res.append([len(s)-num, len(s)-1])
        return res
        
"""
https://leetcode-cn.com/submissions/detail/136015756/

202 / 202 个通过测试用例
状态：通过
执行用时: 32 ms
内存消耗: 13.1 MB

执行用时：32 ms, 在所有 Python 提交中击败了14.29%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了22.22%的用户
"""
