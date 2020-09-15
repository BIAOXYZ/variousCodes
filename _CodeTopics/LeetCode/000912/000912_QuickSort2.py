class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        def quicksort(nums, left, right):
            if left >= right:
                return
            pivot = partition_of_quicksort(nums, left, right)
            quicksort(nums, left, pivot - 1)
            quicksort(nums, pivot + 1, right)

        def partition_of_quicksort(nums, left, right):
            pivot = left
            i, j = left, right
            while i < j:
                # 如果选了left为基准pivot，则从右边先出发会更方便！
                while i < j and nums[j] > nums[pivot]:
                    j -= 1
                while i < j and nums[i] <= nums[pivot]:
                    i += 1
                # 两边都不能再向中心移动的时候交换一次。
                nums[i], nums[j] = nums[j], nums[i]
            """
            # 和前一个提交唯一一点不一样的就是这里用三个j，替换之前三个i。其实就是想再验证下
            # 最后i和j肯定是一样的，所以下面这步换的时候用i或者j都可以。
            """
            nums[pivot], nums[j] = nums[j], nums[pivot]
            return j

        length = len(nums)
        quicksort(nums, 0, length - 1)
        return nums
        
"""
https://leetcode-cn.com/submissions/detail/108396200/

11 / 11 个通过测试用例
状态：通过
执行用时: 132 ms
内存消耗: 17.9 MB
"""
"""
执行用时：132 ms, 在所有 Python 提交中击败了86.85%的用户
内存消耗：17.9 MB, 在所有 Python 提交中击败了61.51%的用户
"""
