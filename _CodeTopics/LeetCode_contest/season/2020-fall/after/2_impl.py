class Solution(object):
    def breakfastNumber(self, staple, drinks, x):
        """
        :type staple: List[int]
        :type drinks: List[int]
        :type x: int
        :rtype: int
        """

        lens, lend = len(staple), len(drinks)
        if lens >= lend:
            longer, shorter, lenlonger, lenshorter = staple, drinks, lens, lend
        else:
            longer, shorter, lenlonger, lenshorter = drinks, staple, lend, lens

        res = 0
        longer.sort()
        for num in shorter:
            obj = x - num
            ind = bisect_right(longer, obj)
            res = res + ind
        return res % 1000000007
        

"""
https://leetcode-cn.com/submissions/detail/107352065/

65 / 65 个通过测试用例
状态：通过
执行用时: 540 ms
内存消耗: 23.5 MB
"""
"""
执行用时：540 ms, 在所有 Python 提交中击败了100.00% 的用户
内存消耗：23.5 MB, 在所有 Python 提交中击败了100.00% 的用户
"""
