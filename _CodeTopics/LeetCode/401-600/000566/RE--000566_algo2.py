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
                rowNum, colNum = (i*r+j) / cols, (i*r+j) % cols
                tmplis.append(nums[rowNum][colNum])
            res.append(tmplis)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/146164621/

2 / 56 个通过测试用例
状态：执行出错

执行出错信息：
Line 19: IndexError: list index out of range
最后执行的输入：
[[1,2],[3,4]]
4
1
"""
