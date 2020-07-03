class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        res = sorted(sum(matrix, []))
        return res[k - 1]
"""
https://leetcode-cn.com/submissions/detail/83979613/

85 / 85 个通过测试用例
状态：通过
执行用时：256 ms
内存消耗：19.7 MB
"""
