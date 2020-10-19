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
        ##print nums
        res = []
        for i in range(length):
            ##print "i= %d, nums[i]=%d" % (i,nums[i])
            # 如果下一个元素和前一个相等，肯定不用再考虑。考虑了反而会造成重复。
            if i > 0 and nums[i] == nums[i-1]:
                ##print "continue i"
                continue
            for j in range(i+1, length):
                ##print "j= %d, nums[j]=%d" % (j,nums[j])
                if j > i+1 and nums[j] == nums[j-1]:
                    ##print "continue j"
                    continue
                for k in range(j+1, length):
                    ##print "k= %d, nums[k]=%d" % (k,nums[k])
                    if k > j+1 and nums[k] == nums[k-1]:
                        ##print "continue k"
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.append([nums[i], nums[j], nums[k]])
                        ##print "res = ",res
                        break      
        return res
        
"""
https://leetcode-cn.com/submissions/detail/78471536/

311 / 313 个通过测试用例
状态：超出时间限制

最后执行的输入：
[82597,-9243,62390,83030,-97960,-26521,-61011,83390,-38677,12333,75987,46091,83794,19355,-71037,-6242,-28801,324,12...
"""
