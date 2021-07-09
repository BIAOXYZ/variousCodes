class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 先写个plain的，不管空间复杂度。

        threshold = len(nums) / 2
        dic = {}
        for num in nums:
            dic[num] = dic.setdefault(num, 0) + 1
            if dic[num] > threshold:
                return num
        return -1
        
"""
https://leetcode-cn.com/submissions/detail/193976346/

46 / 46 个通过测试用例
状态：通过
执行用时: 40 ms
内存消耗: 13.9 MB

执行用时：40 ms, 在所有 Python 提交中击败了36.30%的用户
内存消耗：13.9 MB, 在所有 Python 提交中击败了88.15%的用户
"""
