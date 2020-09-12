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
                    while mid < length - 1 and arr[mid+1] == target:
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
https://leetcode-cn.com/submissions/detail/107381431/

65 / 65 个通过测试用例
状态：通过
执行用时: 1416 ms
内存消耗: 23.3 MB
"""
"""
执行用时：1416 ms, 在所有 Python 提交中击败了100.00% 的用户
内存消耗：23.3 MB, 在所有 Python 提交中击败了100.00% 的用户
"""
