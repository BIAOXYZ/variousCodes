class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        se = set()
        for num in nums:
            if num in se:
                se.remove(num)
            else:
                se.add(num)
        return list(se)
        
"""
https://leetcode-cn.com/submissions/detail/233657327/

执行用时：20 ms, 在所有 Python 提交中击败了69.37%的用户
内存消耗：14 MB, 在所有 Python 提交中击败了47.75%的用户
通过测试用例：
32 / 32
"""
