from collections import Counter
class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """

        ctr1, ctr2 = Counter(s1.split()), Counter(s2.split())
        res = []
        for w in ctr1:
            if ctr1[w] == 1 and w not in ctr2:
                res.append(w)
        for w in ctr2:
            if ctr2[w] == 1 and w not in ctr1:
                res.append(w)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/263732291/

执行用时：12 ms, 在所有 Python 提交中击败了97.83%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了45.65%的用户
通过测试用例：
55 / 55
"""
