class Solution:
    def maximumSwap(self, num: int) -> int:

        lis = list(str(num))
        n = len(lis)
        for toBeReplaceInd in range(n-1):
            leftLis = lis[toBeReplaceInd+1:]
            maxElem = max(leftLis)
            if maxElem > lis[toBeReplaceInd]:
                for ind in range(n-1, toBeReplaceInd, -1):
                    if lis[ind] == maxElem:
                        lis[toBeReplaceInd], lis[ind] = lis[ind], lis[toBeReplaceInd]
                        break
                return int("".join(lis))
        return num
        
"""
https://leetcode.cn/submissions/detail/362217598/

执行用时：
32 ms
, 在所有 Python3 提交中击败了
88.71%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
48.12%
的用户
通过测试用例：
111 / 111
"""
