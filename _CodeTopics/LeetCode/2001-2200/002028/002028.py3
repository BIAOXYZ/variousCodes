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
            i += 1
            leftNum -= 1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/290000865/

执行用时：
176 ms
, 在所有 Python3 提交中击败了
25.93%
的用户
内存消耗：
19.8 MB
, 在所有 Python3 提交中击败了
7.41%
的用户
通过测试用例：
64 / 64
"""
