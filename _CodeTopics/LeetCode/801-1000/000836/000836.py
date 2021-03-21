class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """

        def has_overlap_for_line_segment(lineseg1, lineseg2):
            if lineseg1[0] >= lineseg2[1] or lineseg2[0] >= lineseg1[1]:
                return False
            return True
        
        """
        # 艹，傻逼死了。他么都说了是矩形了，还搞是一个线段的用例。。。
        [-1,0,1,1]
        [0,-1,0,1]
        """
        if rec1[0] == rec1[2] or rec1[1] == rec1[3] or rec2[0] == rec2[2] or rec2[1] == rec2[3]:
            return False
        return has_overlap_for_line_segment([rec1[0], rec1[2]], [rec2[0], rec2[2]]) and has_overlap_for_line_segment([rec1[1], rec1[3]], [rec2[1], rec2[3]])
        
"""
https://leetcode-cn.com/submissions/detail/157848077/

54 / 54 个通过测试用例
状态：通过
执行用时: 12 ms
内存消耗: 12.9 MB

执行用时：12 ms, 在所有 Python 提交中击败了93.88%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了73.47%的用户
"""
