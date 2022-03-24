class Solution:
    def trailingZeroes(self, n: int) -> int:

        totalTwo = totalFive = 0
        for i in range(2, n+1):
            tmpNumOfTwo = 1
            tmpTwo = 2**tmpNumOfTwo
            while tmpTwo <= n and i % tmpTwo == 0:
                tmpNumOfTwo += 1
                tmpTwo *= 2
            totalTwo += tmpNumOfTwo - 1

            tmpNumOfFive = 1
            tmpFive = 5**tmpNumOfFive
            while tmpFive <= n and i % tmpFive == 0:
                tmpNumOfFive += 1
                tmpFive *= 5
            totalFive += tmpNumOfFive - 1
        return min(totalTwo, totalFive)
        
"""
https://leetcode-cn.com/submissions/detail/289000244/

执行用时：1264 ms, 在所有 Python3 提交中击败了10.20%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了58.91%的用户
通过测试用例：
500 / 500
"""
