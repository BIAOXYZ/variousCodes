class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        def bisect_with_dynamic_right(arr, r):
            left, right = 0, r
            newRight = right
            while left <= right:
                mid = left + (right - left) / 2
                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    left = mid + 1
                else:  # arr[mid] > target
                    right = mid - 1
                    newRight = right
            return newRight

        col = len(matrix[0])
        currRight = col - 1 
        for row in matrix:
            tmpSearchRes = bisect_with_dynamic_right(row, currRight)
            if tmpSearchRes == True:
                return True
            else:
                currRight = tmpSearchRes
        return False
        
"""
https://leetcode-cn.com/submissions/detail/232010040/

114 / 129 个通过测试用例
状态：解答错误

输入：
[[1,1]]
2
输出：
true
预期结果：
false
"""
