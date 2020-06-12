class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        length = len(nums)
        if length <= 2:
            return []

        nums.sort()
        res = []
        for i in range(length):
            ##print "i= %d, nums[i]=%d" % (i,nums[i])
            # 如果下一个元素和前一个相等，肯定不用再考虑。考虑了反而会造成重复。
            if i > 0 and nums[i] == nums[i-1]:
                ##print "continue"
                continue
            for j in range(i+1, length):
                ##print "j= %d, nums[j]=%d" % (j,nums[j])
                for k in range(j+1, length):
                    ##print "k= %d, nums[k]=%d" % (k,nums[k])
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.append([nums[i], nums[j], nums[k]])
                        ##print "res = ",res
                        break
        return res
        
"""
https://leetcode-cn.com/submissions/detail/78448742/

84 / 313 个通过测试用例
状态：解答错误

输入：[0,0,0,0]
输出：[[0,0,0],[0,0,0]]
预期：[[0,0,0]]
"""
