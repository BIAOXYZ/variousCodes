class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # 上一个随便写的朴素三重循环竟然没超时。。。看来这个题和LC15的差距还是有一些：
        # 尽管看起来似乎这个还更难一点（毕竟这个是近似）。
        # 虽然朴素三重循环没超时，但双指针降低复杂度到O(n^2)的实现还是要写的。
        length = len(nums)
        mindiff = nums[0] + nums[1] + nums[2] - target
        nums.sort()

        for i in range(length-2):
            j, k = i + 1, length - 1
            # 这俩flag的作用主要是一旦正的和负的都出现过了，其他的就不用再看了：
            # 因为要么就是“更负”，要么就是“更正”。
            flag_positive, flag_negative = 0, 0
            while j < k:
                currdiff = nums[i] + nums[j] + nums[k] - target
                # 我猜是因为测试用例里有很多恰好等于target的，所以好多人直接能返回，所以快很多？
                if currdiff == 0:
                    return target
                if abs(currdiff) < abs(mindiff):
                    mindiff = currdiff
                if currdiff < 0:
                    flag_negative = -1
                    while j + 1 <= length - 2 and nums[j+1] == nums[j]:
                        j += 1
                    j += 1
                else:
                    flag_positive = 1
                    while k - 1 >= j + 1 and nums[k-1] == nums[k]:
                        k -= 1
                    k -= 1
                if flag_positive * flag_positive == -1:
                    break
        return mindiff + target

"""
https://leetcode-cn.com/submissions/detail/82216837/

131 / 131 个通过测试用例
状态：通过
执行用时：148 ms
内存消耗：12.6 MB
"""
"""
# 加了24，25行的那个优化，快了些，但是还是不太对啊，应该还有别的算法吧。

执行用时：148 ms, 在所有 Python 提交中击败了20.13%的用户
内存消耗：12.6 MB, 在所有 Python 提交中击败了12.50%的用户
"""
