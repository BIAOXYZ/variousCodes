class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """

        t = text.split()
        length = len(t)
        if length < 3:
            return []
        
        res = []
        for i in range(2, length):
            if t[i-2] == first and t[i-1] == second:
                res.append(t[i])
        return res
        
"""
https://leetcode-cn.com/submissions/detail/252050212/

执行用时：8 ms, 在所有 Python 提交中击败了95.74%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了8.51%的用户
通过测试用例：
30 / 30
"""
