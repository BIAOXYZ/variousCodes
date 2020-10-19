
# -*- coding: utf-8 -*-
import sys
"""
https://leetcode.com/problems/two-sum/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
"""
https://leetcode.com/submissions/detail/182946828/
"""
"""
https://leetcode-cn.com/problems/two-sum/
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # 一次遍历哈希表法    
        ## 实际上可以只遍历一次，也就是在第一次构造哈希表的时候就先查是否满足和的条件
        ## 这种方法不会有问题，因为最终实际上每个元素和任意其他元素都还是“匹配”过的

        # 下面这句等价于 dic = {}
        dic = dict()
        # 这里用 enumerate() 替代之前用过的 range()
        ## enumerate() 会同时返回index和值，也就是省点事而已
        for i, num in enumerate(nums):
            # 这里不用像两次遍历哈希表那样再判断两个索引不相等了，因为不会存在这种情况
            ## 原因是某个数nums[i]如果没放进字典，则不会被匹配到；一旦被放入字典，则只可能
            ## 被别的不等于它的元素匹配到。所以同一个元素不可能和自己匹配了。
            num2 = target - num
            if num2 in dic:
                # 其实把返回值的 i 和 dic[num2] 换下位置更好。因为 dic[num2] 肯定严格小于 i。
                ## 但是反正这样也能过，无所谓了。
                return [i, dic[num2]]
            dic[num] = i

class Test():
    def run(self, listofnums, targetvalue):
        sol = Solution()
        res = sol.twoSum(listofnums, targetvalue)
        print ("The indices for the list %s to obtain %s is %s" % (listofnums, targetvalue, res))

if  __name__ == '__main__':
    print("------------------------------\nThe main program will start!\n------------------------------\n")
    print("The default coding is:", sys.getdefaultencoding())
    print("\n")

    nums1 = [1, 4, 34, 9, 10, 123]; target1 = 124
    nums2 = [8, 12, 100]; target2 = 500
    nums3 = [3, 2, 4]; target3 = 6

    test = Test()
    test.run(nums1, target1)
    test.run(nums2, target2)
    test.run(nums3, target3)

    print("\n")
    print("------------------------------\nThe main program has ended!\n------------------------------\n")
