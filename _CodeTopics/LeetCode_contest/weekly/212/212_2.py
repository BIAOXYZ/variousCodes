class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        
        # 感觉要超时的命。。。
        def is_arithmetic_progression(newlist):
            newlist.sort()
            length = len(newlist)
            if length == 1:
                return False
            sub = newlist[1] - newlist[0]
            for i in range(length-1,0,-1):
                if sub != newlist[i] - newlist[i-1]:
                    return False
            return True
        
        n, m = len(nums), len(r)
        res = []
        for i in range(m):
            newlist = nums[l[i]:r[i]+1]
            if is_arithmetic_progression(newlist):
                res.append(True)
            else:
                res.append(False)
        return res
    
"""
https://leetcode-cn.com/submissions/detail/118412987/

101 / 101 个通过测试用例
状态：通过
执行用时: 88 ms
内存消耗: 13.4 MB
"""
