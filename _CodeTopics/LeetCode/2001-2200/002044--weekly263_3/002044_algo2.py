from functools import reduce
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:

        maxVal = reduce(lambda x, y : x | y, nums)
        res = 0
        n = len(nums)

        for bitmap in range(1 << n):
            subset = []
            for i in range(n):
                if bitmap & (1 << i):
                    subset.append(nums[i])
            # 也可以用下面这一行，也就是用 or_ 来代替上面的 lambda 匿名函数。
            # 但是注意不管哪种写法，reduce 的起始值 0 都不能省略了，因为 subset 可能为空。
            # reduce 的 iterable 参数如果为空，必须有起始值，不然会报错。
            # if reduce(or_, subset, 0) == maxVal:
            if reduce(lambda x, y : x | y, subset, 0) == maxVal:
                res += 1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/285058971/

执行用时：3540 ms, 在所有 Python3 提交中击败了8.24%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了27.60%的用户
通过测试用例：
111 / 111
"""
