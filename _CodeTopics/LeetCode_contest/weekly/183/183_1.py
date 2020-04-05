class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        length = len(nums)
        
        def sumOfSubList(inputList, subListIndex):
            summation = 0
            for i in range(subListIndex + 1):
                summation += inputList[i]
            return summation
        
        # 直接求个总和，后面每次比较直接用总和减，省的每次都算
        sumOfAll = 0
        for i in range(length):
            sumOfAll += nums[i]
            
        # python list的sort方法默认 reverse = False，也就是升序排列。这里应该显式指定排成降序
        # https://www.runoob.com/python/att-list-sort.html
        """
        这里巨坑，虽然提交前我已经发现了，但是故意提交一次错的，长记性。
        原来的语句是：
        orderedNums = nums.sort(reverse=True)
        
        这里实际上python列表的sort后返回值就是None，也就是nums=[4,3,10,9,8]
        排序后变成nums=[10,9,8,4,3]，而不是搞个新数组可以返回- -
        """
        nums.sort(reverse=True)
   
        i = 0
        while i < int(length//2) + 1:
            if sumOfAll < 2 * sumOfSubList(nums, i):
                break
            i += 1
        return nums[:i+1]
            
