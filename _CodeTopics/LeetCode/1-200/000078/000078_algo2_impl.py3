class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        res = []
        for bitmap in range(1 << n):
            currSubset = []
            for i in range(n):
                # 除了每个 for 循环里把 1 左移 i 位，然后和 bitmap 按位与的写法外，
                ## 另一种思路是每个 for 循环里把 bitmap 不断右移 i 位，然后每次都和 1 按位与。
                ## 其实两种写法都可以不用小括号，因为移位运算的优先级更高。
                ## if bitmap & (1 << i):
                if bitmap >> i & 1:
                    currSubset.append(nums[i])
            # 这里也可以直接 append 进 currSubset，不用 copy。
            ## res.append(currSubset[:])
            res.append(currSubset)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/283973456/

执行用时：36 ms, 在所有 Python3 提交中击败了59.95%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了95.49%的用户
通过测试用例：
10 / 10
"""
