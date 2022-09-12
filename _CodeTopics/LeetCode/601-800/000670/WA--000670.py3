class Solution:
    def maximumSwap(self, num: int) -> int:

        lis = list(str(num))
        n = len(lis)
        for toBeReplaceInd in range(n-1):
            leftLis = lis[toBeReplaceInd+1:]
            maxElem = max(leftLis)
            if maxElem > lis[toBeReplaceInd]:
                ind = lis.index(maxElem, toBeReplaceInd)
                lis[toBeReplaceInd], lis[ind] = lis[ind], lis[toBeReplaceInd]
                return int("".join(lis))
        return num
        
"""
https://leetcode.cn/submissions/detail/362214836/

86 / 111 个通过测试用例
状态：解答错误

输入：
1993
输出：
9193
预期结果：
9913
"""
