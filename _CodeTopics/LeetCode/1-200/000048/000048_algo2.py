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
        
        """
        # 这次不打算用取巧的办法，而是就靠硬代码一轮轮交换。
        ## 基本思想就是：每次把最外面一圈旋转交换就行。以一个4*4矩阵最外圈为例，为了完成这个矩阵最外圈的
        ## 旋转交换，需要做三轮，每轮涉及4个数字。比如 5--11--16--15--5。
        ## 当要交换的圈的宽度为0和1时，直接返回。
        """
        
        def rotate_one_level(width, startInd):
            if width == 1 or width == 0:
                return
            for i in range(width - 1):
                x = startInd
                y = startInd + i
                matrix[x][y], matrix[y][length-1-x], matrix[length-1-x][length-1-y], matrix[length-1-y][x] = matrix[length-1-y][x], matrix[x][y], matrix[y][length-1-x], matrix[length-1-x][length-1-y]
                
        wid = length = len(matrix)
        startInd = 0
        while wid >= 0:
            rotate_one_level(wid, startInd)
            wid -= 2
            startInd += 1
        
"""
https://leetcode-cn.com/submissions/detail/133140241/

21 / 21 个通过测试用例
状态：通过
执行用时: 12 ms
内存消耗: 13 MB

执行用时：12 ms, 在所有 Python 提交中击败了94.06%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了43.62%的用户
"""
