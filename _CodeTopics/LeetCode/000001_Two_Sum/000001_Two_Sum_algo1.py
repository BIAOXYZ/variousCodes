
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

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

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

    test = Test()
    test.run(nums1, target1)
    test.run(nums2, target2)

    print("\n")
    print("------------------------------\nThe main program has ended!\n------------------------------\n")
