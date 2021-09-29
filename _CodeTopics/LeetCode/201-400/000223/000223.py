class Solution(object):
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        """
        :type ax1: int
        :type ay1: int
        :type ax2: int
        :type ay2: int
        :type bx1: int
        :type by1: int
        :type bx2: int
        :type by2: int
        :rtype: int
        """

        s1 = (ax2 - ax1) * (ay2 - ay1)
        s2 = (bx2 - bx1) * (by2 - by1)
        # 以横坐标为例，应该是两个左边的（也就是较小的）横坐标里取较大的；两个右边的横坐标里取较小的。
        # 纵坐标也是类似的，只不过从左边变成上下。但是为了防止差为负值（也就是根本不相交的情况），至少也得是0。
        s3_x = min(ax2, bx2) - max(ax1, bx1)
        s3_y = min(ay2, by2) - max(ay1, by1)
        s3 = max(s3_x, 0) * max(s3_y, 0)
        return s1 + s2 - s3
        
"""
https://leetcode-cn.com/submissions/detail/224592959/

3080 / 3080 个通过测试用例
状态：通过
执行用时: 76 ms
内存消耗: 13 MB

执行用时：76 ms, 在所有 Python 提交中击败了91.49%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了60.64%的用户
"""
