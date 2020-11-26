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
        dic = {}
        res = 0

        for numa in A:
            for numb in B:
                tmpsum = numa + numb
                if tmpsum in dic:
                    dic[tmpsum] += 1
                else:
                    dic[tmpsum] = 1

        for numc in C:
            for numd in D:
                tmpsum = numc + numd
                if -tmpsum in dic:
                    res += dic[-tmpsum]
        return res
        
"""
https://leetcode-cn.com/submissions/detail/126558057/

48 / 48 个通过测试用例
状态：通过
执行用时: 228 ms
内存消耗: 34.9 MB

执行用时：228 ms, 在所有 Python 提交中击败了90.70%的用户
内存消耗：34.9 MB, 在所有 Python 提交中击败了17.68%的用户
"""
