class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """

        # 一时没想到动态规划，但是先想到记忆化搜索了。

        lens, lent = len(s), len(t)
        if lens < lent or (lens == lent and s != t):
            return 0
        
        dic = {}
        # 这个字典里key = (start, start2) 的含义是：在字符串 s 的子串 s[start:] 中，字符串 t 的子串 t[start2:] 出现的次数。
        def memorize_search(start, start2):
            ##print start, start2
            key = tuple([start, start2])
            if dic.has_key(key):
                return dic[key]
            elif s[start] != t[start2] or lens - start < lent - start2:
                dic[key] = 0
                return dic[key]
            elif s[start] == t[start2]:
                if start2 == lent - 1:
                    dic[key] = 1
                    return dic[key]
                else:
                    tmpNum = 0
                    # 下面两行是优化点1
                    leftLength = lent - 1 - start2
                    for i in range(start+1, lens - leftLength + 1):
                        if s[i] == t[start2+1]:
                            tmpNum += memorize_search(i, start2+1)
                    dic[key] = tmpNum
                    return dic[key]

        res = 0
        # 下面一行是优化点2
        for i in range(lens-lent+1):
            if s[i] == t[0]:
                res += memorize_search(i, 0)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/156393012/

62 / 62 个通过测试用例
状态：通过
执行用时: 68 ms
内存消耗: 14.1 MB

执行用时：68 ms, 在所有 Python 提交中击败了7.00%的用户
内存消耗：14.1 MB, 在所有 Python 提交中击败了5.00%的用户
"""
