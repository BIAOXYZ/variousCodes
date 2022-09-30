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
            if n == 4:
                res.append(lis[-4]);res.append(lis[-3])
            else:
                res.append('-');res.append(lis[-4]);res.append(lis[-3])
            res.append('-');res.append(lis[-2]);res.append(lis[-1])
        
        return ''.join(res)
        
"""
https://leetcode.cn/submissions/detail/368907689/

执行用时：
32 ms
, 在所有 Python3 提交中击败了
87.96%
的用户
内存消耗：
15.1 MB
, 在所有 Python3 提交中击败了
10.65%
的用户
通过测试用例：
108 / 108
"""
