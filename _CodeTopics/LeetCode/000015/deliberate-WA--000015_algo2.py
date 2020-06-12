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
        print nums
        res = []
        for i in range(length):
            print "i= %d, nums[i]=%d" % (i,nums[i])
            # 如果下一个元素和前一个相等，肯定不用再考虑。考虑了反而会造成重复。
            if i > 0 and nums[i] == nums[i-1]:
                print "continue i"
                continue
            k = length - 1
            for j in range(i+1, length):
                print "j= %d, nums[j]=%d" % (j,nums[j])
                if j > i+1 and nums[j] == nums[j-1]:
                    print "continue j"
                    continue
                # 双指针的逻辑体现：不断把k往前移（下标变小），
                # 如果还是不行，跳出来开始把j往后移一下（下标变大），接着继续。
                while j < k and nums[i] + nums[j] + nums[k] > 0:
                    print "k= %d, nums[k]=%d" % (k,nums[k])
                    k -= 1
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    print "res= ",res
                    break   
        return res

"""
https://leetcode-cn.com/submissions/detail/78495397/

62 / 313 个通过测试用例
状态：解答错误

输入：[-1,0,1,2,-1,-4]
输出：[[-4,2,2],[-1,-1,2]]
预期：[[-1,-1,2],[-1,0,1]]
"""
"""
# 这个WA是我故意的，明显连题目描述里的例子[-1,0,1,2,-1,-4]都通不过但还是提交了，其和正确代码的区别其实就
# 只有 “k -= 1”后面的部分。仔细对比下想想为什么。

输出
[[-4,2,2],[-1,-1,2]]
预期结果
[[-1,-1,2],[-1,0,1]]
stdout
[-4, -1, -1, 0, 1, 2]
i= 0, nums[i]=-4
j= 1, nums[j]=-1
j= 2, nums[j]=-1
continue j
j= 3, nums[j]=0
j= 4, nums[j]=1
j= 5, nums[j]=2
res=  [[-4, 2, 2]]
i= 1, nums[i]=-1
j= 2, nums[j]=-1
res=  [[-4, 2, 2], [-1, -1, 2]]
i= 2, nums[i]=-1
continue i
i= 3, nums[i]=0
j= 4, nums[j]=1
k= 5, nums[k]=2
j= 5, nums[j]=2
i= 4, nums[i]=1
j= 5, nums[j]=2
i= 5, nums[i]=2
"""
