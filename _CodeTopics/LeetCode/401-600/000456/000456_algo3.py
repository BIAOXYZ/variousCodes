import sortedcontainers
class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # 参考官方答案，（这是第二次）用到了 sortedcontainers 库。
        
        length = len(nums)
        # 左侧最小值
        left_min = nums[0]
        # 右侧所有元素
        right_all = sortedcontainers.SortedList(nums[2:])
        
        for j in range(1, length - 1):
            if left_min < nums[j]:
                index = right_all.bisect_right(left_min)
                if index < len(right_all) and right_all[index] < nums[j]:
                    return True
            left_min = min(left_min, nums[j])
            right_all.remove(nums[j + 1])
        return False
        
"""
https://leetcode-cn.com/submissions/detail/159003326/

101 / 101 个通过测试用例
状态：通过
执行用时: 92 ms
内存消耗: 14.6 MB

执行用时：92 ms, 在所有 Python 提交中击败了25.32%的用户
内存消耗：14.6 MB, 在所有 Python 提交中击败了5.06%的用户
"""
