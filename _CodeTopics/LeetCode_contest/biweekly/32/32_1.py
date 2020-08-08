class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        
        maxnum = arr[-1]
        lostlist = []
        for i in range(1,maxnum):
            if i not in arr:
                lostlist.append(i)
        
        if k <= len(lostlist):
            return lostlist[k-1]
        else:
            return maxnum + (k - len(lostlist))
        
"""
https://leetcode-cn.com/submissions/detail/96060859/

83 / 83 个通过测试用例
	状态：通过
执行用时：100 ms
内存消耗：12.8 MB
"""
