class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """

        """
        # 这个实现已经没办法了，下面这些除了第一个都能过，但是看来只能用单调栈了。

        "bcabc"
        "cbacdcbc"
        "x"
        "xyzyx"
        "leetcode"
        "leatcode"
        "leetcodfe"
        """

        def exist_smaller_character(lis, letter):
            for ch in lis:
                if ch < letter:
                    return True
            return False

        length = len(s)
        res = []
        for i in range(length):
            if s[i] not in res:
                res.append(s[i])
            else:
                ind = res.index(s[i])
                if exist_smaller_character(res[ind+1:], s[i]):
                    if res[ind+1] < s[i]:
                        res.remove(s[i])
                        res.append(s[i])
                else:
                    continue
        return ''.join(res)
        
"""
https://leetcode-cn.com/submissions/detail/132897339/

275 / 289 个通过测试用例
状态：解答错误

输入：
"bcabc"
输出：
"bac"
预期：
"abc"
"""
