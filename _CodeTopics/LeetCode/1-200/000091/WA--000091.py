class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        if s[0] == "0":
            return 0
        length = len(s)
        res = [0]

        def backtrack(startPos):
            if startPos >= length:
                res[0] += 1
                return
            if s[startPos] == "0":
                return
            for i in [1, 2]:
                if i == 1:
                    backtrack(startPos + 1)
                if i == 2:
                    if startPos < length - 2 and int(s[startPos+1:startPos+3]) <= 26:
                        backtrack(startPos + 2)
        
        backtrack(0)
        backtrack(1)
        return res[0]
        
"""
https://leetcode-cn.com/submissions/detail/170234477/

12 / 269 个通过测试用例
状态：解答错误

输入：
"1"
输出：
2
预期：
1
"""
