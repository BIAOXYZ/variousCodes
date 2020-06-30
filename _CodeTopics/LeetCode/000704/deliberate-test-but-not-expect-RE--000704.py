class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        length = len(nums)

        # 这里right是不是也可以考虑取length？因为好像看过说C++标准库里就是用
        # 左闭右开的取值，据说好处最多。不过先用左闭右闭试试吧。
        left, right = 0, length
        
        # 取不取等号似乎也值得讨论下？一般是要有的吧，不然对于
        # nums = [-1,2,3,5,9,12], target = 2，
        # 最后就搜不到正确结果2了。
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1
        
"""
https://leetcode-cn.com/submissions/detail/83489450/

15 / 46 个通过测试用例
状态：执行出错

执行出错信息：Line 20: IndexError: list index out of range
最后执行的输入：[-1,0,3,5,9,12]
               13
"""
"""
# 和上一个能过的代码对比，只有第13行有一点不同：
# right的初始值从（实际上可以取到的最大值）length-1 改成了（类似开区间，取不到的）length。
# 这个RE真没想到，虽然我确实只是想试试把最初的right设成开区间会怎样，但我其实预期应该是会过的。。。
"""
