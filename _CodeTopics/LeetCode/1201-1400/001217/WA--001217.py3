class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:

        n = len(position)
        res = float('inf')
        for i in range(n):
            tmp = 0
            for j in range(n):
                if (j - i) % 2 == 1:
                    tmp += 1
            res = min(res, tmp)
        return res
        
"""
https://leetcode.cn/submissions/detail/334362251/

15 / 51 个通过测试用例
状态：解答错误

输入：
[1,2,2,2,2]
输出：
2
预期结果：
1
"""
