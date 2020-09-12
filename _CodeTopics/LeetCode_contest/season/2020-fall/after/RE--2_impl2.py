class Solution(object):
    def breakfastNumber(self, staple, drinks, x):
        """
        :type staple: List[int]
        :type drinks: List[int]
        :type x: int
        :rtype: int
        """

        def binary_search_right_most(arr, target):
            length = len(arr)
            left, right = 0, length - 1
            while left <= right:
                mid = (right + left) / 2
                if arr[mid] < target:
                    left = mid + 1
                elif arr[mid] > target:
                    right = mid - 1
                else:
                    while arr[mid+1] == target:
                        mid += 1
                    return True, mid
            return False, left

        lens, lend = len(staple), len(drinks)
        if lens >= lend:
            longer, shorter, lenlonger, lenshorter = staple, drinks, lens, lend
        else:
            longer, shorter, lenlonger, lenshorter = drinks, staple, lend, lens

        res = 0
        longer.sort()
        for num in shorter:
            obj = x - num
            isIn, ind = binary_search_right_most(longer, obj)
            if isIn:
                res = res + ind + 1
            else:
                res = res + ind
        return res % 1000000007
        

"""
https://leetcode-cn.com/submissions/detail/107380662/

10 / 65 个通过测试用例
状态：执行出错

执行出错信息：
Line 20: IndexError: list index out of range
最后执行的输入：
[7,7,9,8,7,5,4,2]
[9,4,8,2,8,5,3,1,1]
13
"""
