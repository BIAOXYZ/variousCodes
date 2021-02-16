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
        
        def flatten_2dlist_to_1dlist(list2d):
            return [elem for sublis in list2d for elem in sublis]
        
        newNums = flatten_2dlist_to_1dlist(nums)
        res = []
        for i in range(r):
            tmplis = []
            for j in range(c):
                tmplis.append(newNums.pop(0))
            res.append(tmplis)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/146161465/

56 / 56 个通过测试用例
状态：通过
执行用时: 92 ms
内存消耗: 13.9 MB

执行用时：92 ms, 在所有 Python 提交中击败了29.93%的用户
内存消耗：13.9 MB, 在所有 Python 提交中击败了92.52%的用户
"""
