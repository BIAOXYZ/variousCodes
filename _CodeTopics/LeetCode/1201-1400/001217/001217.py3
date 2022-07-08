class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:

        n = len(position)
        res = float('inf')
        for i in range(n):
            tmp = 0
            for j in range(n):
                if (position[j] - position[i]) % 2 == 1:
                    tmp += 1
            res = min(res, tmp)
        return res
        
"""
https://leetcode.cn/submissions/detail/334468442/

执行用时：
56 ms
, 在所有 Python3 提交中击败了
6.92%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
58.93%
的用户
通过测试用例：
51 / 51
"""
