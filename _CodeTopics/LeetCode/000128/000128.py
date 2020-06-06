class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if nums == []:
            return 0
        else:
            # 这里去一下重，以防万一。其实一个题目没事就设边缘情况挺没意思的。
            nums = set(nums)
        
        maxlongest = 1
        # 注意这里不能用 for i in range(len(nums)): 了。
        for k in nums:
            # 比如当前元素是3，如果2在这个集合里，那么到时候直接考察2开头的就行了。
            if k - 1 in nums:
                continue
            else:
                currlongest = 1
                currnum = k
                while currnum + 1 in nums:
                    currlongest += 1
                    currnum += 1
                maxlongest = max(maxlongest, currlongest)
        return maxlongest
        
"""
# https://leetcode-cn.com/submissions/detail/76785312/

68 / 68 个通过测试用例
	状态：通过
执行用时：20 ms
内存消耗：13.7 MB
"""
"""
真没觉得这题是hard。。。
"""
