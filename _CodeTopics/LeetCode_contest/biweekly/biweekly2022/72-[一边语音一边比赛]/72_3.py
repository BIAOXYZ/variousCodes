class Solution(object):
    def maximumEvenSplit(self, finalSum):
        """
        :type finalSum: int
        :rtype: List[int]
        """
        
        # 首先一定得有 2，不然假定某个符合要求的结果从小到大排列是 [x1,x2,...,xn]，
        ## 那么 x1 一定可以拆成 2 + x1'，但是这个结论对 4 不成立。
        # 后来想到用贪心就可以了，最后剩余的部分加到最大的那个上面。
        
        if finalSum & 1 == 1:
            return []
        
        res = []
        curr = 2
        while finalSum >= curr:
            res.append(curr)
            finalSum -= curr
            curr += 2
        if finalSum > 0:
            res[-1] += finalSum
        return res
    
"""
https://leetcode-cn.com/submissions/detail/270503404/

56 / 56 个通过测试用例
状态：通过
执行用时: 124 ms
内存消耗: 27 MB
"""
