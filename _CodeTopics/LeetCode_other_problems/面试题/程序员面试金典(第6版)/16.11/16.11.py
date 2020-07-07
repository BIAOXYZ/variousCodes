class Solution(object):
    def divingBoard(self, shorter, longer, k):
        """
        :type shorter: int
        :type longer: int
        :type k: int
        :rtype: List[int]
        """

        if k == 0:
            return []

        first = shorter * k
        res = [first]

        # 不然 1，1，10000 这个用例过不了。。。
        if longer == shorter:
            return res

        for i in range(k):
            res.append(res[-1] + longer - shorter)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/85701711/

60 / 60 个通过测试用例
状态：通过
执行用时：72 ms
内存消耗：19.7 MB
"""
"""
执行用时：72 ms, 在所有 Python 提交中击败了43.31%的用户
内存消耗：19.7 MB, 在所有 Python 提交中击败了100.00%的用户
"""
