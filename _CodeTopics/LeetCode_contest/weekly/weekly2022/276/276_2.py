class Solution(object):
    def minMoves(self, target, maxDoubles):
        """
        :type target: int
        :type maxDoubles: int
        :rtype: int
        """
        
        res = 0
        while target > 1:
            if maxDoubles > 0:
                if target & 1 == 1:
                    target = (target - 1) / 2
                    res += 2
                else:
                    target /= 2
                    res += 1
                maxDoubles -= 1
            else:
                return res + target - 1
        return res
    
"""
https://leetcode-cn.com/submissions/detail/258927907/

145 / 145 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13.2 MB
"""
