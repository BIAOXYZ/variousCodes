class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        # 通过观察可以发现，替换的规律是这样的：
        ## （旧的）第 i 行会变成（新的）第 n-1-i 列；（旧的）第 j 列会变成（新的）第 j 行。
        # 比如例子里那个四阶矩阵：
        ## 第0行会变成第3列；第1行会变成第2列；依次类推。。。
        ## 第3列会变成第3行；第2列会变成第2行；依次类推。。。
        ## 所以原来第 i 行第 j 列的元素，会跑到新的第 j 行第 n-1-i 列处。
        
        # 这里先流氓一下，申请一个同样大小的矩阵，从而避免变量覆盖的问题。但是有可能空间会超？
        n = len(matrix)
        tmp = [[-1 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                tmp[j][n-1-i] = matrix[i][j]
        
        for i in range(n):
            for j in range(n):
                matrix[i][j] = tmp[i][j]
        
"""
https://leetcode-cn.com/submissions/detail/132109553/

21 / 21 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13 MB

执行用时：20 ms, 在所有 Python 提交中击败了56.97%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了28.13%的用户
"""
