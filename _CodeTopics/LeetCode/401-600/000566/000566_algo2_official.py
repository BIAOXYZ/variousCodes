class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """

        rows, cols = len(nums), len(nums[0])
        if rows * cols != r * c:
            return nums
        
        res = [[0 for _ in range(c)] for _ in range(r)]
        # 类似官方答案，下面这个小技巧不错。
        for i in range(rows * cols):
            res[i/c][i%c] = nums[i/cols][i%cols]
        return res
        
"""
https://leetcode-cn.com/submissions/detail/146169036/

56 / 56 个通过测试用例
状态：通过
执行用时: 80 ms
内存消耗: 14.1 MB

执行用时：80 ms, 在所有 Python 提交中击败了69.54%的用户
内存消耗：14.1 MB, 在所有 Python 提交中击败了68.21%的用户
"""
