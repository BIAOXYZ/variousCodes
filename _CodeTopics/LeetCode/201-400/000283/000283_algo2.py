class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        """
        # 双指针解法：
        # currPos负责记录全局循环的位置，currNonzeroPos负责记录当前非零元素的位置。
        # 第一遍循环一旦碰到非零的元素，直接往可能的最靠前位置（这个位置当然由currNonzeroPos负责）
        # 挪，等非零元素都挪完了，从最后一个非零元素的下一个位置开始，全赋值成0即可。
        """
        length = len(nums)
        currPos, currNonzeroPos = 0, 0

        for currPos in range(length):
            if nums[currPos] != 0:
                nums[currNonzeroPos] = nums[currPos]
                currNonzeroPos += 1
        for i in range(currNonzeroPos, length):
            nums[i] = 0
        return nums
        
"""
https://leetcode-cn.com/submissions/detail/77940529/

21 / 21 个通过测试用例
状态：通过
执行用时：28 ms
内存消耗：13.8 MB
"""
