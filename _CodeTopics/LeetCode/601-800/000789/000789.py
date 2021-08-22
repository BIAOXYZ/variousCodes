class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """

        def calculate_distance(p1, p2):
            return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

        for ghost in ghosts:
            # 感觉其他拦截条件好像都和这条是类似的？
            if calculate_distance(ghost, target) <= abs(target[0]) + abs(target[1]):
                return False
        return True
        
"""
https://leetcode-cn.com/submissions/detail/209863645/

77 / 77 个通过测试用例
状态：通过
执行用时: 12 ms
内存消耗: 12.9 MB

执行用时：12 ms, 在所有 Python 提交中击败了90.00%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了80.00%的用户
"""
