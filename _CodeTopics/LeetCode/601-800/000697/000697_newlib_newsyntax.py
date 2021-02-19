import collections
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 用Counter直接代替手写版本
        dic = collections.Counter(nums)
        maxFreq = max(dic.values())
        # 用filter一行搞定，前面的要四行。。。
        degreeKeys = filter(lambda k:dic[k] == maxFreq, dic.keys())

        length = len(nums)
        minLen = length
        for k in degreeKeys:
            left, right = 0, length - 1
            while nums[left] != k:
                left += 1
            while nums[right] != k:
                right -= 1
            minLen = min(minLen, right - left + 1)
        return minLen
        
"""
https://leetcode-cn.com/submissions/detail/146941471/

89 / 89 个通过测试用例
状态：通过
执行用时: 1768 ms
内存消耗: 13.4 MB

执行用时：1768 ms, 在所有 Python 提交中击败了8.06%的用户
内存消耗：13.4 MB, 在所有 Python 提交中击败了100.00%的用户
"""
"""
慢是慢，空间倒混了个百分之百。。。
"""
