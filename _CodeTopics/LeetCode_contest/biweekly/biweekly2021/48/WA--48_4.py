class Solution(object):
    def maxScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def gcd(a, b):
            if a < b:
                a, b = b, a
            while b!=0:
                a, b = b, a%b
            return a
        def find_max_of_matrix(mtx):
            ind = [0, 0]
            currMax = 1
            for i, row in enumerate(mtx):
                tmp = max(row)
                if tmp > currMax:
                    ind = [i, row.index(tmp)]
                    currMax = tmp
            return ind
        def delete_row_and_col(mtx, rowInd, colInd):
            del mtx[rowInd]
            for row in mtx:
                del row[colInd]
            
        n = len(nums)
        dp = [[1 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                dp[i][j] = gcd(nums[i], nums[j])
        
        res = 0
        for i in range(n/2, 0, -1):
            ##print dp
            ind = find_max_of_matrix(dp)
            res += i * dp[ind[0]][ind[1]]
            delete_row_and_col(dp, ind[0], ind[1])
        return res
    
"""
https://leetcode-cn.com/submissions/detail/157716412/

36 / 66 个通过测试用例
状态：解答错误

输入：
[697035,181412,384958,575458]
输出：
899
预期：
869
"""
