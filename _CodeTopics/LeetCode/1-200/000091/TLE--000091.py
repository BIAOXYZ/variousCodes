class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

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
                    if startPos <= length - 2 and int(s[startPos:startPos+2]) <= 26:
                        backtrack(startPos + 2)
        
        backtrack(0)
        return res[0]
        
"""
https://leetcode-cn.com/submissions/detail/170236443/

23 / 269 个通过测试用例
状态：超出时间限制

最后执行的输入：
"111111111111111111111111111111111111111111111"
"""
