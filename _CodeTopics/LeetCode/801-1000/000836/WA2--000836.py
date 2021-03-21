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
        
        return has_overlap_for_line_segment([rec1[0], rec1[2]], [rec2[0], rec2[2]]) and has_overlap_for_line_segment([rec1[1], rec1[3]], [rec2[1], rec2[3]])
        
"""
https://leetcode-cn.com/submissions/detail/157845725/

43 / 54 个通过测试用例
状态：解答错误

输入：
[-1,0,1,1]
[0,-1,0,1]
输出：
true
预期：
false
"""
