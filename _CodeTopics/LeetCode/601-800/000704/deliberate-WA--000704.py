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
        while left < right:
            mid = (left + right) / 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1

"""
https://leetcode-cn.com/submissions/detail/83483850/

23 / 46 个通过测试用例
状态：解答错误

输入：[5]
      5
输出：-1
预期：0
"""
"""
# 故意的，因为估计第18行while循环那里不取等号的话，这组输入：nums = [-1,2,3,5,9,12], target = 2
# 就会返回-1（也就是找不到），但是实际是可以找到的。
# 结果一提交发现一个更简单的用例也过不了。。。
"""
