class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """

        def point_in_rectangle(point, rec):
            if rec[0] < point[0] < rec[2] and rec[1] < point[1] < rec[3]:
                return True
            return False
        
        points = [
            [rec1[0], rec1[1]], 
            [rec1[0], rec1[3]], 
            [rec1[2], rec1[1]], 
            [rec1[2], rec1[3]]]
        for point in points:
            if point_in_rectangle(point, rec2):
                return True
        return False
        
"""
https://leetcode-cn.com/submissions/detail/157639489/

44 / 54 个通过测试用例
状态：解答错误

输入：
[7,8,13,15]
[10,8,12,20]
输出：
false
预期：
true
"""
