class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """

        # 哈希表法，AB为一组，CD为一组。
        # 参考官方答案，利用了一下collections里的Counter。但是初始化Counter时用了列表推导式。

        counterAB = Counter([numa + numb for numa in A for numb in B])
        res = 0
        for numc in C:
            for numd in D:
                if -numc-numd in counterAB:
                    res += counterAB[-numc-numd]
        return res
        
"""
https://leetcode-cn.com/submissions/detail/126729109/

48 / 48 个通过测试用例
状态：通过
执行用时: 364 ms
内存消耗: 38.8 MB

执行用时：364 ms, 在所有 Python 提交中击败了19.64%的用户
内存消耗：38.8 MB, 在所有 Python 提交中击败了13.13%的用户
"""
