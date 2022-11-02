class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """

        m, n = len(word), len(sequence)
        i = j = 0
        res = 0
        while j < n:
            if word[i] == sequence[j]:
                i += 1
                if i == m:
                    res += 1
                    i = 0
            else:
                i = 0
            j += 1
        return res
        
"""
https://leetcode.cn/submissions/detail/378851684/

169 / 212 个通过测试用例
状态：解答错误

输入：
"aaabaaaabaaabaaaabaaaabaaaabaaaaba"
"aaaba"
输出：
2
预期结果：
5
"""
