class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def list_to_dict_v2(l):
            dic = {}
            for elem in l:
                dic[elem] = dic.setdefault(elem, 0) + 1
            return dic
        
        dic = list_to_dict_v2(nums)
        maxFreq = max(dic.values())
        degreeKeys = []
        for k, v in dic.items():
            if v == maxFreq:
                degreeKeys.append(k)
        
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
https://leetcode-cn.com/submissions/detail/146939112/

89 / 89 个通过测试用例
状态：通过
执行用时: 1752 ms
内存消耗: 13.7 MB

执行用时：1752 ms, 在所有 Python 提交中击败了8.13%的用户
内存消耗：13.7 MB, 在所有 Python 提交中击败了88.62%的用户
"""
