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
                    return [True, 'placeholder']
                elif arr[mid] < target:
                    left = mid + 1
                else:  # arr[mid] > target
                    right = mid - 1
                    newRight = right
            return [False, newRight]

        col = len(matrix[0])
        currRight = col - 1 
        for row in matrix:
            tmpSearchRes = bisect_with_dynamic_right(row, currRight)
            # 问题在这里，如果返回的 tmpSearchRes 为 1，python里认为 1 == True。。。
            # 所以对于这个用例 [[1,1]], 2 会走错分支。
            """
            >>> print(1 == True)
            True
            >>> 
            >>> print(2 == True)
            False
            >>> 
            """
            if tmpSearchRes[0] == True:
                return True
            else:
                currRight = tmpSearchRes[1]
        return False
        
"""
https://leetcode-cn.com/submissions/detail/232013520/

执行用时：128 ms, 在所有 Python 提交中击败了82.59%的用户
内存消耗：18.9 MB, 在所有 Python 提交中击败了89.06%的用户
通过测试用例：
129 / 129
"""
