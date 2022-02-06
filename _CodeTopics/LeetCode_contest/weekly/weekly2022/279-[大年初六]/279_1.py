class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        odd, even = [], []
        for i, num in enumerate(nums):
            if i & 1 == 1:
                odd.append(num)
            else:
                even.append(num)
        odd.sort(reverse=True)
        even.sort()
        
        res = []
        while True:
            if even:
                res.append(even.pop(0))
            if odd:
                res.append(odd.pop(0))
            if not even and not odd:
                return res
    
"""
https://leetcode-cn.com/submissions/detail/265098916/

218 / 218 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 12.9 MB
"""
