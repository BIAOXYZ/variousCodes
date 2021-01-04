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
        return res
        
"""
https://leetcode-cn.com/submissions/detail/136015056/

137 / 202 个通过测试用例
状态：解答错误

输入：
"aaa"
输出：
[]
预期：
[[0,2]]
"""
