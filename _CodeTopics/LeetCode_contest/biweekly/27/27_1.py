class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        
        # 其实只要两个数组元素一样就总能翻转到一模一样。。。方法就是类似冒泡排序那样两两交换
        # 题目提示里已经有 target.length == arr.length，故不再判断
        
        length = len(arr)
        target.sort()
        arr.sort()
        
        for i in range(length):
            if arr[i] != target[i]:
                return False
        return True
    
"""
# https://leetcode-cn.com/contest/biweekly-contest-27/submissions/detail/74988226/

99 / 99 个通过测试用例
	状态：通过
执行用时：32 ms
内存消耗：12.8 MB
"""
