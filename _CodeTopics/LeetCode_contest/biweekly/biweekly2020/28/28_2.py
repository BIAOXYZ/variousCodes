class SubrectangleQueries(object):

    def __init__(self, rectangle):
        """
        :type rectangle: List[List[int]]
        """
        self.rec = rectangle
        ##self.rows = len(rectangle)
        ##self.cols = len(rectangle[0])


    def updateSubrectangle(self, row1, col1, row2, col2, newValue):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :type newValue: int
        :rtype: None
        """
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                self.rec[i][j] = newValue
        
    def getValue(self, row, col):
        """
        :type row: int
        :type col: int
        :rtype: int
        """
        return self.rec[row][col]


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
"""
https://leetcode-cn.com/submissions/detail/78717492/

52 / 52 个通过测试用例
	状态：通过
执行用时：196 ms
内存消耗：14.6 MB
"""
