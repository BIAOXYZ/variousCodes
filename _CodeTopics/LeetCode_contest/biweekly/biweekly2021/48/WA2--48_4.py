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
        def delete_two_rows(mtx, rowInd1, rowInd2):
            for i in range(len(mtx)-1, -1, -1):
                if i == rowInd1 or i == rowInd2:
                    del mtx[i]
        def delete_two_cols(mtx, colInd1, colInd2):
            for row in mtx:
                for i in range(len(row)-1, -1, -1):
                    if i == colInd1 or i == colInd2:
                        del row[i]
            
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
            if i != 1:
                delete_two_rows(dp, ind[0], ind[1])
                delete_two_cols(dp, ind[0], ind[1])
        return res
    
"""
https://leetcode-cn.com/submissions/detail/157723593/

65 / 66 个通过测试用例
状态：解答错误

输入：
[109497,983516,698308,409009,310455,528595,524079,18036,341150,641864,913962,421869,943382,295019]
输出：
525
预期：
527
"""
