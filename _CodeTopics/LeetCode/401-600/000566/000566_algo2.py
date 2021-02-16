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
        
        res = []
        for i in range(r):
            tmplis = []
            for j in range(c):
                # 这里i乘的应该是c，而不是r！理由和两处都取cols类似！
                rowNum, colNum = (i*c+j) / cols, (i*c+j) % cols
                tmplis.append(nums[rowNum][colNum])
            res.append(tmplis)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/146165957/

56 / 56 个通过测试用例
状态：通过
执行用时: 88 ms
内存消耗: 14.2 MB

执行用时：88 ms, 在所有 Python 提交中击败了35.76%的用户
内存消耗：14.2 MB, 在所有 Python 提交中击败了38.41%的用户
"""
