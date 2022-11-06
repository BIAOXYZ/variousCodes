class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """

        res = []
        n, i = len(command), 0
        while i < n:
            ch = command[i]
            if ch == "G":
                res.append(ch)
                i += 1
            elif ch == "(":
                if command[i+1] == ")":
                    res.append("o")
                    i += 2
                else:
                    res.append("al")
                    i += 4
        return "".join(res)
        
"""
https://leetcode.cn/submissions/detail/379750062/

执行用时：
16 ms
, 在所有 Python 提交中击败了
79.49%
的用户
内存消耗：
12.9 MB
, 在所有 Python 提交中击败了
79.49%
的用户
通过测试用例：
105 / 105
"""
