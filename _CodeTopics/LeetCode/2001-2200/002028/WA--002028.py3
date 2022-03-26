class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:

        m = len(rolls)
        sum1 = sum(rolls)
        sum2 = mean*(m+n) - sum1
        if sum2 / n < 1 or sum2 / n > 6:
            return []
        
        res = [sum2 // n for _ in range(n)]
        i = 0
        leftNum = sum2 % n
        while leftNum > 0:
            res[i] += 1
            leftNum -= 1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/289999331/

35 / 64 个通过测试用例
状态：解答错误

输入：
[4,5,6,2,3,6,5,4,6,4,5,1,6,3,1,4,5,5,3,2,3,5,3,2,1,5,4,3,5,1,5]
4
40
输出：
[11,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]
预期结果：
[4,4,4,4,4,4,5,5,4,4,4,5,4,4,4,4,4,4,4,4,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,5,5]
"""
