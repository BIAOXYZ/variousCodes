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
        left, right = 0, length-1
        
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
https://leetcode-cn.com/submissions/detail/83484197/

46 / 46 个通过测试用例
状态：通过
执行用时：252 ms
内存消耗：13.7 MB
"""
"""
# 和上一个故意提交的有错误的代码（`deliberate-WA--000704.py `）只差了一个等号，
# 也就是第18行while条件那里从 < 改成 <= 。

执行用时：252 ms, 在所有 Python 提交中击败了59.37%的用户
内存消耗：13.7 MB, 在所有 Python 提交中击败了14.29%的用户
"""
