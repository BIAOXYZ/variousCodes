class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """

        """
        # 典型的边界条件已经包含在内，可省。
        if not moves:
            return True
        """

        mapTable = {"R":[1,0], "L":[-1,0], "U":[0,1], "D":[0,-1]}
        tmp = [0, 0]
        for elem in moves:
            tmp[0] += mapTable[elem][0]
            tmp[1] += mapTable[elem][1]
        
        if tmp == [0, 0]:
            return True
        return False
        
"""
https://leetcode-cn.com/submissions/detail/102373851/

63 / 63 个通过测试用例
状态：通过
执行用时: 120 ms
内存消耗: 12.8 MB
"""
"""
执行用时：120 ms, 在所有 Python 提交中击败了23.68%的用户
内存消耗：12.8 MB, 在所有 Python 提交中击败了62.92%的用户
"""
