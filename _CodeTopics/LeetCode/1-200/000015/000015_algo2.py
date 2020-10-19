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
            k = length - 1
            for j in range(i+1, length):
                ##print "j= %d, nums[j]=%d" % (j,nums[j])
                if j > i+1 and nums[j] == nums[j-1]:
                    ##print "continue j"
                    continue
                # 双指针的逻辑体现：不断把k往前移（下标变小），
                # 如果还是不行，跳出来开始把j往后移一下（下标变大），接着继续。
                while j < k and nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                if j == k:
                    break
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i], nums[j], nums[k]])     
        return res

"""
https://leetcode-cn.com/submissions/detail/78482391/

313 / 313 个通过测试用例
状态：通过
执行用时：732 ms
内存消耗：18.3 MB
"""
