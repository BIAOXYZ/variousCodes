class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        
        n = len(tickets)
        res = 0
        while tickets[k] > 0:
            for i in range(n):
                if tickets[i] > 0:
                    tickets[i] -= 1
                    res += 1
                    if tickets[k] == 0:
                        return res
        
"""
https://leetcode-cn.com/submissions/detail/238418727/

65 / 65 个通过测试用例
状态：通过
执行用时: 32 ms
内存消耗: 13.1 MB
"""
