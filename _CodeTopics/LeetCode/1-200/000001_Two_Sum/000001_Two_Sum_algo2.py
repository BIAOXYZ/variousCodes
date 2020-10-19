
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

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # 两次遍历哈希表法（python叫字典，对这两种说法不做区分）
        ## 第一次遍历把元素的值作为key，元素的索引作为valve插入哈希表
        ## 第二次遍历测试找出满足条件的那一对元素，并返回其索引
        
        diction = {}
        # range(len(nums)) 等价于 range(0, len(nums), 1)
        for i in range(len(nums)):
            diction[nums[i]] = i
        for i in range(0, len(nums), 1):
            j = diction.get(target - nums[i])
            # 这里一定要加上 j != i 这半边条件，不然比如[3,2,4]和6，会直接返回[0,0]。但是实际上数字3只能用一次！
            ## 如果是算法1中直接暴力两重循环遍历则不存在这个问题。
            if j is not None and j != i:
                return [i, j]

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
    
    # 这个用例吃了一点小亏，必须额外判断一下返回的index j和原来的index i不能是一个
    ## 否则num3的返回值会是[0,0]。但是3不能用两次，所以正确结果应该是[1,2]
    nums3 = [3, 2, 4]; target3 = 6

    test = Test()
    #test.run(nums1, target1)
    #test.run(nums2, target2)
    test.run(nums3, target3)

    print("\n")
    print("------------------------------\nThe main program has ended!\n------------------------------\n")
