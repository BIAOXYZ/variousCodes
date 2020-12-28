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
        orderedNums = nums.sort(reverse=True)
   
        i = 0
        while i < int(length//2) + 1:
            if sumOfAll < 2 * sumOfSubList(orderedNums, i):
                break
            i += 1
        return orderedNums[:i+1]

"""
提交结果：执行出错
0 / 103 个通过测试用例
执行错误信息：Line 13: TypeError: 'NoneType' object has no attribute '__getitem__'
最后执行的输入：[4,3,10,9,8]
"""
