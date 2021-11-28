from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        lens, lenp = len(s), len(p)
        if lens < lenp:
            return []
        
        ctrP = Counter(p)
        ctr = Counter(s[:lenp])
        res = [0] if ctr == ctrP else []

        for i in range(1, lens - lenp + 1):
            newch, oldch = s[i+lenp-1], s[i-1]
            ctr[newch] = ctr.setdefault(newch, 0) + 1
            ctr[oldch] -= 1
            if ctr[oldch] == 0:
                del ctr[oldch]
            if ctr == ctrP:
                res.append(i)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/243173770/

执行用时：168 ms, 在所有 Python 提交中击败了9.92%的用户
内存消耗：14.3 MB, 在所有 Python 提交中击败了20.89%的用户
通过测试用例：
61 / 61
"""
