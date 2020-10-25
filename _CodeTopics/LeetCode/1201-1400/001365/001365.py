class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        length = len(nums)
        res, dic = [], {}

        for i in range(length):
            if dic.has_key(nums[i]):
                res.append(dic[nums[i]])
            else:
                tmp = 0
                for j in range(i) + range(i+1,length):
                    if nums[j] < nums[i]:
                        tmp += 1
                res.append(tmp)
                dic[nums[i]] = tmp
        return res
        
"""
https://leetcode-cn.com/submissions/detail/118591018/

103 / 103 个通过测试用例
状态：通过
执行用时: 88 ms
内存消耗: 13.1 MB

执行用时：88 ms, 在所有 Python 提交中击败了60.84%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了6.13%的用户
"""
