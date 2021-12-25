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
        
        res = set()
        for i in range(2, length):
            if t[i-2] == first and t[i-1] == second:
                res.add(t[i])
        return list(res)
        
"""
https://leetcode-cn.com/submissions/detail/252049714/

18 / 30 个通过测试用例
状态：解答错误

输入：
"jkypmsxd jkypmsxd kcyxdfnoa jkypmsxd kcyxdfnoa jkypmsxd kcyxdfnoa kcyxdfnoa jkypmsxd kcyxdfnoa"
"kcyxdfnoa"
"jkypmsxd"
输出：
["kcyxdfnoa"]
预期结果：
["kcyxdfnoa","kcyxdfnoa","kcyxdfnoa"]
"""
