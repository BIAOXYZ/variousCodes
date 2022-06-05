class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # 参考了这个：
        # https://github.com/BIAOXYZ/variousCodes/blob/master/_CodeTopics/LeetCode/801-1000/000912/000912_QuickSort.py
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
            nums[pivot], nums[i] = nums[i], nums[pivot]
            return i

        length = len(nums)
        quicksort(nums, 0, length - 1)
        return nums
        """

        def quick_select(nums, left, right):
            if left >= right:
                return
            pivot = partition(nums, left, right)
            n = len(nums)
            # 从这里可以看出来，快速选择之所以渐进能达到 O(n)，比快速排序的 O(nlogn) 快，
            # 就是因为只要 partition 一次后，它只需要找半边；而快排两边都不能省。
            if pivot == n - k:
                return nums[pivot]
            elif pivot < n - k:
                return quick_select(nums, pivot+1, right)
            elif pivot > n - k:
                return quick_select(nums, left, pivot-1)

        def partition(nums, left, right):
            pivot = left
            i, j = left, right
            while i < j:
                while i < j and nums[j] > nums[pivot]:
                    j -= 1
                while i < j and nums[i] <= nums[pivot]:
                    i += 1
                nums[i], nums[j] = nums[j], nums[i]
            nums[pivot], nums[i] = nums[i], nums[pivot]
            return i

        return quick_select(nums, 0, len(nums)-1)
        
"""
https://leetcode.cn/submissions/detail/322051649/

20 / 32 个通过测试用例
状态：解答错误

输入：
[1]
1
输出：
null
预期结果：
1
"""
