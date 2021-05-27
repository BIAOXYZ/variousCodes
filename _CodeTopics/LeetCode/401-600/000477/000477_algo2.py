class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 普通的而二重循环会超时，只能另辟蹊径。目前想到的是这样： 统计（整个数组里所有数的）每个位上一共有多少个1和多少个0，然后直接计算。
        # 由于最大的数也就10^9，只需要2的三十多次方应该就够了。就在这里试了下：
        # print 2**30 > 10**9, 2**29 > 10**9  的结果是  True False，所以用31就行。

        length = len(nums)
        highestPos = 31
        tmp = [0] * highestPos
        for num in nums:
            i = 0
            while num > 0:
                if num % 2 != 0:
                    tmp[i] += 1
                num >>= 1
                i += 1
        
        res = 0
        for numOfOne in tmp:
            res += numOfOne * (length - numOfOne)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/181522102/

46 / 46 个通过测试用例
状态：通过
执行用时: 460 ms
内存消耗: 14.2 MB

执行用时：460 ms, 在所有 Python 提交中击败了33.33%的用户
内存消耗：14.2 MB, 在所有 Python 提交中击败了41.67%的用户
"""
