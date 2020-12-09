class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """

        # 20块是累赘，因为最大面值就是它，收了就找不出去了。此外，找钱的时候，能优先找10块的
        # 就优先找10块的，因为两张5块在灵活性方面严格大于一张10块。这是这道题贪心思想的体现。

        dic = {5:0, 10:0}
        for bill in bills:
            if bill == 5:
                dic[5] += 1
            elif bill == 10:
                if dic[5] == 0:
                    return False
                dic[5] -= 1; dic[10] += 1
            else:
                if dic[5] == 0 or 10*dic[10] + 5*dic[5] < 15:
                    return False
                if dic[10] > 0:
                    dic[10] -= 1; dic[5] -= 1
                else:
                    dic[5] -= 3
        return True
        
"""
https://leetcode-cn.com/submissions/detail/129904851/

45 / 45 个通过测试用例
状态：通过
执行用时: 120 ms
内存消耗: 13.3 MB

执行用时：120 ms, 在所有 Python 提交中击败了90.60%的用户
内存消耗：13.3 MB, 在所有 Python 提交中击败了11.16%的用户
"""
