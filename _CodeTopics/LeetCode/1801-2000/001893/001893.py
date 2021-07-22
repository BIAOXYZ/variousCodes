class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """

        for num in range(left, right+1):
            flag = False
            for lnum, rnum in ranges:
                if lnum <= num <= rnum:
                    flag = True
                    break
            if not flag:
                return False
        return True
        
"""
https://leetcode-cn.com/submissions/detail/198784046/

105 / 105 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 13.1 MB

执行用时：16 ms, 在所有 Python 提交中击败了97.30%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了54.05%的用户
"""
