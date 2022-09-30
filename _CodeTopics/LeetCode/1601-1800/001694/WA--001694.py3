class Solution:
    def reformatNumber(self, number: str) -> str:

        lis = [ch for ch in number if ch.isdigit()]
        n = len(lis)
        lengthTwoBlocks = 0
        if n % 3 == 1:
            lengthTwoBlocks = 2
        elif n % 3 == 2:
            lengthTwoBlocks = 1
        
        res = []
        if lengthTwoBlocks != 2:
            for i in range(n):
                if i != 0 and i % 3 == 0:
                    res.append('-')
                res.append(lis[i])
        else:
            for i in range(n-4):
                if i != 0 and i % 3 == 0:
                    res.append('-')
                res.append(lis[i])
            res.append('-');res.append(lis[-4]);res.append(lis[-3])
            res.append('-');res.append(lis[-2]);res.append(lis[-1])
        
        return ''.join(res)
        
"""
https://leetcode.cn/submissions/detail/368907526/

105 / 108 个通过测试用例
状态：解答错误

输入：
"9964-"
输出：
"-99-64"
预期结果：
"99-64"
"""
